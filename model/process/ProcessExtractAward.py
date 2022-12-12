from rpa_robot.ControllerSettings import ControllerSettings
from model.process.UtilsProcess import UtilsProcess
from model.process.Process3.Adapter_BDNS import Adapter_BDNS
from model.process.ProcessCommand import ProcessCommand
from model.process.ProcessCommand import Pstatus as pstatus
from model.process.ProcessCommand import ProcessID
from model.process.ProcessExtractInfoPDF import ProcessExtractInfoPDF
from model.SGI import SGI

import time
import requests
import json
import os

NAME            = "Extract Convocatorias"
DESCRIPTION     = "Proceso que extrae las últimas convocatorias de las fuentes de datos dadas"
REQUIREMENTS    = ['rpaframework','playwright','selenium','bs4']
ID              = ProcessID.EXTRACT_AWARD.value
cs = ControllerSettings()

class ProcessExtractAward(ProcessCommand):
    def __init__(self,id_schedule, id_log, id_robot, priority, log_file_path, parameters = None, ip_api=None, port_api=None):
        ProcessCommand.__init__(self,ID,NAME, REQUIREMENTS, DESCRIPTION, id_schedule, id_log,id_robot, priority, log_file_path, parameters, ip_api, port_api)    
    
    def execute(self):
        """
        Ejecución del subproceso de extracción de una concesión.
        """
        self.state = pstatus.RUNNING
        self.log.state = "OK"
        self.log.start_log(time.time())
        self.update_log("El proceso de extracción de concesiones ha empezado", True)
        self.log.completed = 0

        list_awards = {}
        param_info_pdf = {}
        adapter_bdns = Adapter_BDNS(self.ip_api, self.port_api)
        sgi = cs.get_sgi(self.ip_api, self.port_api)
        if sgi:
            list_awards = self.get_valid_forms(forms=sgi.get_forms()) 
            self.update_log("Lista de concesiones: " + str(list_awards), True)
            list_persons_form = self.get_person_forms(list_awards, sgi)
            self.update_log("Lista de solicitantes: " + str(list_persons_form), True)
            
            if len(list_awards) > 0:
                self.update_log("Obteniendo parámetros de acceso a base de datos.", True)
                for item in list_awards:
                    self.log.completed += 100/len(list_awards)
                    BDNS_NUM = self.get_bdns(item['convocatoriaId'])
                    self.update_log("Número de la BDNS: " + str(BDNS_NUM), True)
                    #Buscamos la solicitudes que hay.
                    if BDNS_NUM:
                        self.update_log("Empezamos con la convocatoria BDNS: "+ str(BDNS_NUM), True)
                        param_info_pdf['paths'] = adapter_bdns.obtain_resources_award(BDNS_NUM)
                        param_info_pdf['nif_universidad'] = self.nif_array(self.parameters['nif_universidad'])
                        param_info_pdf['solicitudes'] = list_persons_form 
                        param_info_pdf['keywords'] = self.parameters['keywords'] 
                        pExtractPdf = ProcessExtractInfoPDF(self.log.id_schedule, self.log.id, self.id_robot, "1", None, param_info_pdf)
                        pExtractPdf.add_data_listener(self)
                        pExtractPdf.execute()
                        for f in param_info_pdf['paths']:
                            if os.path.exists(f):
                                os.remove(f)
                        if pExtractPdf.result:
                            self.update_log("Enviamos la información obtenida de la concesión "+ str(item['codigoRegistroInterno']), True)
                            
                            state = self.send_mail(str(BDNS_NUM), pExtractPdf.result, self.parameters['emails'])
                            if state =="ERROR":
                                self.log.completed = 100
                                self.state = pstatus.FINISHED
                                self.update_log("Error enviando el correo. Proceso finalizado. ",True)
                                self.log.state = "ERROR"
                                self.log.end_log(time.time())
                                return
                            
                        else:
                            self.update_log("No se ha generado el PDF con ninguna ocurrencia. Fin del proceso",True)
                    else:
                        self.update_log("No se ha encontrado ninguna información que el robot haya sido capaz de inferir de la concesión ", True)
            else:
                self.update_log("No hay concesiones que tengan un estado distinto a: BORRADOR, CONCEDIDA, DENEGADA, DESISTIDA ó EXCLUIDA", True)
        else:
            self.update_log('ERROR al obtener la información relacionada con Hércules-SGI.', True)
            self.log.state = 'ERROR'

        self.log.completed = 100
        self.log.end_log(time.time())
        self.state = pstatus.FINISHED

    def get_valid_forms(self, forms: str) -> list:
        """
        Método para seleccionar de las solicitudes recogidas por el SGI las que cumplan las condiciones de no estar en estado borrador, concedida, denegada, desistida ó excluida.

        :param forms str: Solicitudes en formato JSON a analizar.
        :return list Lista de solicitudes tratadas que cumplen el criterio.
        """
        list_awards = []
        if forms:
            try:
                for form in json.loads(forms):
                    if form['estado'] and form['estado']['estado'] != "BORRADOR" and form['estado']['estado'] != "CONCEDIDA" and form['estado']['estado'] != "DENEGADA" and form['estado']['estado'] != "DESISTIDA" and form['estado']['estado'] != "EXCLUIDA":
                        list_awards.append(form)
            except Exception as e:
                self.update_log("Error al extraer el json de los formularios válidos. " + str(e), True)
        return list_awards

    def get_person_forms(self, person_forms: str, sgi: SGI) -> list:
        """
        Método para recuperar los solicitantes de las solicitudes dadas.

        :param solicitudes str: Solicitudes en formato JSON.
        :param sgi SGI: Objeto SGI para consultar los datos en el sistema.
        :return list Lista de solicitantes.
        """
        list_persons_form =  {}
        if person_forms:
            for person_form in person_forms:
                if person_form['codigoExterno'] != '':
                    try:
                        list_persons_form[person_form['codigoExterno']] = json.loads(sgi.get_person(person_form['solicitanteRef']))['apellidos']
                    except Exception as e:
                        self.update_log("Error al extraer el solicitante a través del SGI. " + str(e), True)
            return list_persons_form
        return list_persons_form

    def get_person_forms_t(self, person_forms: str, forms: list) -> list:
        """
        Método para recuperar los solicitantes de las solicitudes dadas.

        :param solicitudes str: Solicitudes en formato JSON.
        :param sgi SGI: Objeto SGI para consultar los datos en el sistema.
        :return list Lista de solicitantes.
        """
        list_persons_form =  {}
        if person_forms:
            for person_form in person_forms:
                if person_form['codigoExterno'] != '':
                    list_persons_form[person_form['codigoExterno']] = json.loads(forms)['apellidos']
            return list_persons_form
        return list_persons_form

    def get_bdns(self, id_sgi_convocatoria: int):
        """
        Método para obtener desde la base de datos interna el código BDNS que tiene asignado.

        :param id_sgi_convocatoria int: Número de id que tiene la convocatoria en el sistema SGI.
        :return int El código de la BDNS que tiene asignado. Sino, 0.
        """
        #titulo_codificado = titulo.split(' ', 1)[1].encode("gb2312").decode('utf_8')
        bbdd_url = self.ip_api + ":" + self.port_api + "/api/orchestrator/register/convocatorias?_from=BDNS&id_sgi=" + str(id_sgi_convocatoria) + "&entidad_convocante=AGENCIA ESTATAL DE INVESTIGACIÓN"
        response = requests.get(bbdd_url)
        if response and response.status_code == 200:
            return int(json.loads(response.text)[0]['url'].split("/")[-1])    
        return 0

    def get_bdns_t(self, response: str):
        """
        Método para obtener desde la base de datos interna el código BDNS que tiene asignado.

        :param id_sgi_convocatoria int: Número de id que tiene la convocatoria en el sistema SGI.
        :param response str: Respuesta
        :return int El código de la BDNS que tiene asignado. Sino, 0.
        """
        #titulo_codificado = titulo.split(' ', 1)[1].encode("gb2312").decode('utf_8')
        return 0 if response == None or response == '' else (int((response)[0]['url'].split("/")[-1]))

    def send_mail(self, id_bdns: int, message: dict, emails: list) -> str:
        """
        Método para enviar un email. Se llama a la rutina Send Mail.
        :param id_bdns int: Número de la BDNS que hace referencia a una convocatoria.
        :param message dict: Diccionario con el contenido del mensaje.
        :param emails list: Lista de emails a los que hay que enviar mensaje.
        :return str: Estado del proceso Send Mail.
        """
        body = message['content']
        files = []
        if 'files' in message:
            files = message['files'] #array de paths, deberian estar en files dentro de robot
        utils = UtilsProcess(self.log.id_schedule, self.log.id, self.id_robot, self.priority, self.log.log_file_path)
        state = utils.send_email(emails, body, "Concesión BDNS "+id_bdns, files, self)
        return state

    def nif_array(self, nifs: list) -> list:
        """
        Método para formatear el NIF.

        :param nifs list: Lista de los NIFs a transformar
        """
        nif_array = []
        for nif in nifs:
            if nif and isinstance(nif, dict):
                nif_array.append(nif['nif'])
        return nif_array

    def pause(self):
        pass

    def kill(self):
        pass
    
    def resume(self):
        pass
