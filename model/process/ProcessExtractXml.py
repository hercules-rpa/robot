from pathlib import Path
import time
import requests, os
from model.process.ProcessCommand import ProcessCommand, ProcessID, Pstatus
import xml.dom.minidom

NAME            = "Extract XML"
DESCRIPTION     = "Proceso para extraer información de un fichero xml."
REQUIREMENTS    = []
ID              = ProcessID.EXTRACT_XML.value

class InfoResultado:
    def __init__(self, nodos_tratados, hijos):
        self.nodos_tratados = nodos_tratados
        self.hijos = hijos

class ProcessExtractXml(ProcessCommand):
    def __init__(self, id_schedule, id_log, id_robot, priority, log_file_path, parameters=None):
        ProcessCommand.__init__(self, ID, NAME, REQUIREMENTS, DESCRIPTION,
                                id_schedule, id_log, id_robot, priority, log_file_path, parameters)
  

    def traer_documento(self, origen, destino):
        if origen and destino:
            self.update_log('Solicitando ' + origen, True)
            file = requests.get(origen, allow_redirects=True)

            dirname = os.path.dirname(destino)
            if not os.path.exists(dirname):
                path = Path(dirname)
                path.mkdir(parents=True)

            if os.path.exists(destino):
                os.remove(destino)
            
            with open(destino, 'wb') as f:
                f.write(file.content)

            return file.status_code
        return 404

    def obtener_hijos(self, nodos:dict, raiz, npadre) -> InfoResultado:
        result = []
        tratados = []
        if nodos:
            hijos = nodos[raiz]
            tratados.append(raiz)
            if hijos:
                for hijo in hijos:
                    nhijo = npadre.getElementsByTagName(hijo)
                    if hijo in nodos:
                        info = self.obtener_hijos(nodos, hijo, nhijo)
                        result = result + info.hijos
                        tratados.append(info.nodos_tratados)
                    else:
                        result.append((nhijo, []))
        
        return InfoResultado(tratados, result)
    
    def obtener_diccionario(self, filename:str, rootname:str, atribname:str, childsname:list):
        result =  {}
        if rootname and childsname:
            mydoc = xml.dom.minidom.parse(filename)
            collection = mydoc.documentElement  # -> Objeto raíz
            if collection.localName != 'error':
                nodos_padres = collection.getElementsByTagName(rootname)
                for root in nodos_padres:
                    childs = []
                    if childsname:
                        for child in childsname:
                            childs += root.getElementsByTagName(child)
                    
                    result.setdefault(root.attributes[atribname].value, childs)
                    #result[root.attributes[atribname].value] = childs
        return result 

    def obtener_nodos(self, nodos:dict, filename:str):
        count = 0
        result = []
        if nodos:
            nodos_tratados = []
            keys = nodos.keys()
            mydoc = xml.dom.minidom.parse(filename)
            collection = mydoc.documentElement  # -> Objeto raíz
            if collection.localName != 'error':
                # Obtiene una lista de los objetos con la etiqueta padre
                for key in keys:
                    if key not in nodos_tratados:
                        nodos_padres = collection.getElementsByTagName(key)
                        if nodos_padres:
                            for npadre in nodos_padres: 
                                count+=1
                                infoHijos:InfoResultado = self.obtener_hijos(nodos, key, npadre)
                                if infoHijos:
                                    if infoHijos.nodos_tratados:
                                        nodos_tratados = nodos_tratados + infoHijos.nodos_tratados
                                    if infoHijos.hijos:
                                        result.append((npadre, infoHijos.hijos))

        return result                                               

    def execute(self):
        self.state = Pstatus.RUNNING
        self.log.state = "OK"
        start = time.time()
        self.log.start_log(start)
        self.notificar_actualizacion("El proceso de extracción de información de fichero xml ha comenzado.")
        self.log.completed = 0
        url:str = None
        
        try:
            url = self.parameters['url']           
        except:
            self.notificar_actualizacion('No se ha obtenido el parámetro url.')
                
        filename = self.parameters['filename']
        if url:            
            status_code = self.traer_documento(url, filename)
            self.log.completed = 33

            if status_code != 200:
                self.notificar_actualizacion('No ha sido posible descargar el fichero xml.')
        else:
            self.log.completed = 33

        if os.path.getsize(filename) < 10:
            self.notificar_actualizacion('ERROR: fichero xml erróneo o incompleto.')
        else:
            self.log.completed = 66
            if 'nodos' in self.parameters:
                self.result =  self.obtener_nodos(self.parameters['nodos'], filename)

        #Solo eliminamos el fichero si no se ha pasado como parámetro la url, 
        #ya que si se pasa la url el fichero lo hemos descargado nosotros.
        delete_file = False
        if url:
            delete_file = True

        if delete_file and os.path.exists(filename):
            os.remove(filename)
            
        self.log.completed = 100
        self.notificar_actualizacion("El proceso de extracción de información del fichero xml ha finalizado.")        
        end_time = time.time()
        self.log.end_log(end_time)
        self.state = Pstatus.FINISHED


    def pause(self):
        pass

    def kill(self):
        pass
    
    def resume(self):
        pass