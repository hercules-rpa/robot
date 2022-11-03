import sys
import os
import json
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(os.path.dirname(currentdir))
sys.path.insert(1, parentdir)
print(currentdir, parentdir)
import unittest
from model.process.ProcessExtractAward import ProcessExtractAward

class TestExtractAwards(unittest.TestCase):
# Pruebas realizadas a través de la convocatoria resuelta: https://www.infosubvenciones.es/bdnstrans/GE/es/convocatoria/525644

    def test_get_valid_requests(self):        
        process = ProcessExtractAward(id_schedule = None, id_log = None, id_robot = "1", priority = "1", log_file_path = None, parameters=None)
        file = open("hercules-rpa/test/files/p3-award/requests.txt", "r")
        response_text = file.read()
        file.close()
        result = process.get_valid_forms(response_text)
        self.assertEqual(len(result),7)

    def not_valid_requests(self, forms):
        list_awards = []
        if forms:
            for form in json.loads(forms):
                if not form['estado']['estado'] != "BORRADOR" and not form['estado']['estado'] != "CONCEDIDA" and not form['estado']['estado'] != "DENEGADA" and not form['estado']['estado'] != "DESISTIDA" and not form['estado']['estado'] != "EXCLUIDA":
                    list_awards.append(form)
        return list_awards

    def test_get_not_valid_requests(self):        
        process = ProcessExtractAward(id_schedule = None, id_log = None, id_robot = "1", priority = "1", log_file_path = None, parameters=None)
        file = open("hercules-rpa/test/files/p3-award/requests.txt", "r")
        response_bad = file.read()
        file.close()
        response_text = self.not_valid_requests(response_bad)
        result = process.get_valid_forms(json.dumps(response_text))
        self.assertEqual(len(result),0)

    def test_get_valid_requests_bad_forms(self):        
        process = ProcessExtractAward(id_schedule = None, id_log = None, id_robot = "1", priority = "1", log_file_path = None, parameters=None)
        file = open("hercules-rpa/test/files/projects/projects1.txt", "r")
        response_text = file.read()
        file.close()
        result = process.get_valid_forms(response_text)
        self.assertEqual(len(result),0)

    def test_get_valid_requests_bad_input(self):        
        process = ProcessExtractAward(id_schedule = None, id_log = None, id_robot = "1", priority = "1", log_file_path = None, parameters=None)
        file = open("hercules-rpa/test/files/projects/projects1.txt", "r")
        response_text = file.read()
        file.close()
        result = process.get_valid_forms("")
        self.assertEqual(len(result),0)

    def test_get_bdns_525644(self):
        process = ProcessExtractAward(id_schedule = None, id_log = None, id_robot = "1", priority = "1", log_file_path = None, parameters=None)
        response = [{"fecha_inicio": "", "id": 96, "fecha_definitiva": "", "_from": "BDNS", "entidad_gestora": "MINISTERIO DE CIENCIA E INNOVACI\u00d3N", "entidad_convocante": "AGENCIA ESTATAL DE INVESTIGACI\u00d3N", "observaciones": "", "notificada": True, "modelo_ejecucion": "Subvencion", "fecha_publicacion": 1601244000.0, "fecha_fin": "", "fecha_creacion": 1664367977.954702, "titulo": "Resoluci\u00f3n de 30 de septiembre de 2020, de la Presidencia de la Agencia Estatal de Investigaci\u00f3n, por la que se aprueba la convocatoria 2020 de ayudas para contratos predoctorales en el marco del Plan Estatal de I+D+i 2017-2020.", "url": "https://www.pap.hacienda.gob.es/bdnstrans/GE/es/convocatoria/525644", "area_tematica": "", "id_sgi": "113", "unidad_gestion": "OTRI UGI"}]
        result = process.get_bdns_t(response)
        self.assertEqual(result,525644)

    def test_get_bdns_644545(self):
        process = ProcessExtractAward(id_schedule = None, id_log = None, id_robot = "1", priority = "1", log_file_path = None, parameters=None)
        response = [{"fecha_inicio": "", "id": 96, "fecha_definitiva": "", "_from": "BDNS", "entidad_gestora": "MINISTERIO DE CIENCIA E INNOVACI\u00d3N", "entidad_convocante": "AGENCIA ESTATAL DE INVESTIGACI\u00d3N", "observaciones": "", "notificada": True, "modelo_ejecucion": "Subvencion", "fecha_publicacion": 1601255000.0, "fecha_fin": "", "fecha_creacion": 1664334477.954702, "titulo": "Resoluci\u00f3n de 30 de septiembre de 2020, de la Presidencia de la Agencia Estatal de Investigaci\u00f3n, por la que se aprueba la convocatoria 2020 de ayudas para contratos predoctorales en el marco del Plan Estatal de I+D+i 2017-2020.", "url": "https://www.pap.hacienda.gob.es/bdnstrans/GE/es/convocatoria/644545", "area_tematica": "", "id_sgi": "113", "unidad_gestion": "OTRI UGI"}]
        result = process.get_bdns_t(response)
        self.assertEqual(result,644545)

    def test_get_bdns_non_existent(self):
        process = ProcessExtractAward(id_schedule = None, id_log = None, id_robot = "1", priority = "1", log_file_path = None, parameters=None)
        response = ""
        result = process.get_bdns_t(response)
        self.assertEqual(result,0)

    def test_get_bdns_bad_request(self):
        process = ProcessExtractAward(id_schedule = None, id_log = None, id_robot = "1", priority = "1", log_file_path = None, parameters=None)
        result = process.get_bdns_t('')
        self.assertEqual(result,0)
    
    def test_get_bdns_bad_request_none(self):
        process = ProcessExtractAward(id_schedule = None, id_log = None, id_robot = "1", priority = "1", log_file_path = None, parameters=None)
        result = process.get_bdns_t(None)
        self.assertEqual(result,0)

    def test_formatting_nifs(self):
        process = ProcessExtractAward(id_schedule = None, id_log = None, id_robot = "1", priority = "1", log_file_path = None, parameters=None)
        array =  [ { "nif": "9238472" }, { "nif": "19827349" }, { "nif": "7928374" }, { "nif": "123423" } ]
        result = process.nif_array(array)
        self.assertEqual(len(result),4)
        self.assertEqual(result[0], "9238472")
        self.assertEqual(result[1], "19827349")

    def test_formatting_nifs_none(self):
        process = ProcessExtractAward(id_schedule = None, id_log = None, id_robot = "1", priority = "1", log_file_path = None, parameters=None)
        array =  [ { "nif": "" } ]
        result = process.nif_array(array)
        self.assertEqual(len(result),1)
        self.assertEqual(result[0], "")

    def test_formatting_nifs_bad(self):
        process = ProcessExtractAward(id_schedule = None, id_log = None, id_robot = "1", priority = "1", log_file_path = None, parameters=None)
        array =  []
        result = process.nif_array(array)
        self.assertEqual(len(result),0)

    def test_formatting_nifs_bad_form_int(self):
        process = ProcessExtractAward(id_schedule = None, id_log = None, id_robot = "1", priority = "1", log_file_path = None, parameters=None)
        array =  [ 9238472, 9238472]
        result = process.nif_array(array)
        self.assertEqual(len(result),0)

    def test_formatting_nifs_bad_form(self):
        process = ProcessExtractAward(id_schedule = None, id_log = None, id_robot = "1", priority = "1", log_file_path = None, parameters=None)
        array =  [ "9238472", "9238472"]
        result = process.nif_array(array)
        self.assertEqual(len(result),0)
    
    def test_get_persona_antonio(self):
        process = ProcessExtractAward(id_schedule = None, id_log = None, id_robot = "1", priority = "1", log_file_path = None, parameters=None)
        list_awards = [{'createdBy': '00391433', 'creationDate': '2022-05-05T09:02:28.475Z', 'lastModifiedBy': '00391433', 'lastModifiedDate': '2022-05-05T09:04:35.943Z', 'id': 23, 'titulo': '', 'convocatoriaId': 35, 'codigoExterno': 'PID2019-106498GB-I00', 'codigoRegistroInterno': 'SGI_SLC2320220505', 'estado': {'createdBy': '00391433', 'creationDate': '2022-05-05T09:04:35.941Z', 'lastModifiedBy': '00391433', 'lastModifiedDate': '2022-05-05T09:04:35.941Z', 'id': 47, 'solicitudId': 23, 'estado': 'SOLICITADA', 'fechaEstado': '2022-05-05T09:02:37.084Z', 'comentario': ''}, 'creadorRef': '00391433', 'solicitanteRef': '28710458', 'observaciones': '', 'convocatoriaExterna': '', 'unidadGestionRef': '3', 'formularioSolicitud': 'PROYECTO', 'tipoSolicitudGrupo': None, 'activo': True},{"createdBy":"00391433","creationDate":"2022-05-09T14:20:32.068Z","lastModifiedBy":"00391433","lastModifiedDate":"2022-05-09T14:20:57.238Z","id":25,"titulo":"","convocatoriaId":35,"codigoExterno":"","codigoRegistroInterno":"SGI_SLC2520220509","estado":{"createdBy":"00391433","creationDate":"2022-05-09T14:20:57.238Z","lastModifiedBy":"00391433","lastModifiedDate":"2022-05-09T14:20:57.238Z","id":52,"solicitudId":25,"estado":"SOLICITADA","fechaEstado":"2022-05-09T14:20:42.496Z","comentario":""},"creadorRef":"00391433","solicitanteRef":"48495234","observaciones":"","convocatoriaExterna":"","unidadGestionRef":"3","formularioSolicitud":"PROYECTO","tipoSolicitudGrupo":None,"activo":True}]
        result = process.get_person_forms_t(list_awards, '{"nombre":"ANTONIO FERNANDO","id":"28710458","numeroDocumento":"28710458H","tipoDocumento":{"id":"D","nombre":"DOCUMENTO NACIONAL DE IDENTIDAD"},"apellidos":"SKARMETA GOMEZ","sexo":{"id":"V","nombre":"Varon"},"personalPropio":true,"activo":true,"entidadPropiaRef":"Q3018001","emails":[{"email":"skarmeta@um.es","principal":true}]}')
        self.assertEqual(list(result.keys()), ["PID2019-106498GB-I00"])
        self.assertEqual(list(result.values()), ["SKARMETA GOMEZ"])

    def test_get_persona_palma(self):
        process = ProcessExtractAward(id_schedule = None, id_log = None, id_robot = "1", priority = "1", log_file_path = None, parameters=None)
        list_awards = [{'createdBy': '00391433', 'creationDate': '2022-05-05T09:02:28.475Z', 'lastModifiedBy': '00391433', 'lastModifiedDate': '2022-05-05T09:04:35.943Z', 'id': 23, 'titulo': '', 'convocatoriaId': 35, 'codigoExterno': 'PID2019-106498GB-I00', 'codigoRegistroInterno': 'SGI_SLC2320220505', 'estado': {'createdBy': '00391433', 'creationDate': '2022-05-05T09:04:35.941Z', 'lastModifiedBy': '00391433', 'lastModifiedDate': '2022-05-05T09:04:35.941Z', 'id': 47, 'solicitudId': 23, 'estado': 'SOLICITADA', 'fechaEstado': '2022-05-05T09:02:37.084Z', 'comentario': ''}, 'creadorRef': '00391433', 'solicitanteRef': '28710458', 'observaciones': '', 'convocatoriaExterna': '', 'unidadGestionRef': '3', 'formularioSolicitud': 'PROYECTO', 'tipoSolicitudGrupo': None, 'activo': True},{"createdBy":"00391433","creationDate":"2022-05-09T14:20:32.068Z","lastModifiedBy":"00391433","lastModifiedDate":"2022-05-09T14:20:57.238Z","id":25,"titulo":"","convocatoriaId":35,"codigoExterno":"","codigoRegistroInterno":"SGI_SLC2520220509","estado":{"createdBy":"00391433","creationDate":"2022-05-09T14:20:57.238Z","lastModifiedBy":"00391433","lastModifiedDate":"2022-05-09T14:20:57.238Z","id":52,"solicitudId":25,"estado":"SOLICITADA","fechaEstado":"2022-05-09T14:20:42.496Z","comentario":""},"creadorRef":"00391433","solicitanteRef":"48495234","observaciones":"","convocatoriaExterna":"","unidadGestionRef":"3","formularioSolicitud":"PROYECTO","tipoSolicitudGrupo":None,"activo":True}]
        result = process.get_person_forms_t(list_awards, '{"nombre":"JOSE FRANCISCO","id":"28710458","numeroDocumento":"28710458H","tipoDocumento":{"id":"D","nombre":"DOCUMENTO NACIONAL DE IDENTIDAD"},"apellidos":"PALMA MENDEZ","sexo":{"id":"V","nombre":"Varon"},"personalPropio":true,"activo":true,"entidadPropiaRef":"Q3018001","emails":[{"email":"skarmeta@um.es","principal":true}]}')
        self.assertEqual(list(result.keys()), ["PID2019-106498GB-I00"])
        self.assertEqual(list(result.values()), ["PALMA MENDEZ"])

    def test_get_persona_no_awards(self):
        process = ProcessExtractAward(id_schedule = None, id_log = None, id_robot = "1", priority = "1", log_file_path = None, parameters=None)
        list_awards = [{'createdBy': '00391433', 'creationDate': '2022-05-05T09:02:28.475Z', 'lastModifiedBy': '00391433', 'lastModifiedDate': '2022-05-05T09:04:35.943Z', 'id': 23, 'titulo': '', 'convocatoriaId': 35, 'codigoExterno': '', 'codigoRegistroInterno': 'SGI_SLC2320220505', 'estado': {'createdBy': '00391433', 'creationDate': '2022-05-05T09:04:35.941Z', 'lastModifiedBy': '00391433', 'lastModifiedDate': '2022-05-05T09:04:35.941Z', 'id': 47, 'solicitudId': 23, 'estado': 'SOLICITADA', 'fechaEstado': '2022-05-05T09:02:37.084Z', 'comentario': ''}, 'creadorRef': '00391433', 'solicitanteRef': '', 'observaciones': '', 'convocatoriaExterna': '', 'unidadGestionRef': '3', 'formularioSolicitud': 'PROYECTO', 'tipoSolicitudGrupo': None, 'activo': True},{"createdBy":"00391433","creationDate":"2022-05-09T14:20:32.068Z","lastModifiedBy":"00391433","lastModifiedDate":"2022-05-09T14:20:57.238Z","id":25,"titulo":"","convocatoriaId":35,"codigoExterno":"","codigoRegistroInterno":"SGI_SLC2520220509","estado":{"createdBy":"00391433","creationDate":"2022-05-09T14:20:57.238Z","lastModifiedBy":"00391433","lastModifiedDate":"2022-05-09T14:20:57.238Z","id":52,"solicitudId":25,"estado":"SOLICITADA","fechaEstado":"2022-05-09T14:20:42.496Z","comentario":""},"creadorRef":"00391433","solicitanteRef":"48495234","observaciones":"","convocatoriaExterna":"","unidadGestionRef":"3","formularioSolicitud":"PROYECTO","tipoSolicitudGrupo":None,"activo":True}]
        result = process.get_person_forms_t(list_awards, '{"nombre":"ANTONIO FERNANDO","id":"28710458","numeroDocumento":"28710458H","tipoDocumento":{"id":"D","nombre":"DOCUMENTO NACIONAL DE IDENTIDAD"},"apellidos":"SKARMETA GOMEZ","sexo":{"id":"V","nombre":"Varon"},"personalPropio":true,"activo":true,"entidadPropiaRef":"Q3018001","emails":[{"email":"skarmeta@um.es","principal":true}]}')
        self.assertEqual(list(result.keys()), [])
        self.assertEqual(list(result.values()), [])

    def test_get_persona_bad_request(self):
        process = ProcessExtractAward(id_schedule = None, id_log = None, id_robot = "1", priority = "1", log_file_path = None, parameters=None)
        list_awards = [{'createdBy': '00391433', 'creationDate': '2022-05-05T09:02:28.475Z', 'lastModifiedBy': '00391433', 'lastModifiedDate': '2022-05-05T09:04:35.943Z', 'id': 23, 'titulo': '', 'convocatoriaId': 35, 'codigoExterno': '', 'codigoRegistroInterno': 'SGI_SLC2320220505', 'estado': {'createdBy': '00391433', 'creationDate': '2022-05-05T09:04:35.941Z', 'lastModifiedBy': '00391433', 'lastModifiedDate': '2022-05-05T09:04:35.941Z', 'id': 47, 'solicitudId': 23, 'estado': 'SOLICITADA', 'fechaEstado': '2022-05-05T09:02:37.084Z', 'comentario': ''}, 'creadorRef': '00391433', 'solicitanteRef': '', 'observaciones': '', 'convocatoriaExterna': '', 'unidadGestionRef': '3', 'formularioSolicitud': 'PROYECTO', 'tipoSolicitudGrupo': None, 'activo': True},{"createdBy":"00391433","creationDate":"2022-05-09T14:20:32.068Z","lastModifiedBy":"00391433","lastModifiedDate":"2022-05-09T14:20:57.238Z","id":25,"titulo":"","convocatoriaId":35,"codigoExterno":"","codigoRegistroInterno":"SGI_SLC2520220509","estado":{"createdBy":"00391433","creationDate":"2022-05-09T14:20:57.238Z","lastModifiedBy":"00391433","lastModifiedDate":"2022-05-09T14:20:57.238Z","id":52,"solicitudId":25,"estado":"SOLICITADA","fechaEstado":"2022-05-09T14:20:42.496Z","comentario":""},"creadorRef":"00391433","solicitanteRef":"48495234","observaciones":"","convocatoriaExterna":"","unidadGestionRef":"3","formularioSolicitud":"PROYECTO","tipoSolicitudGrupo":None,"activo":True}]
        result = process.get_person_forms_t(None, '')
        self.assertEqual(list(result.keys()), [])
        self.assertEqual(list(result.values()), [])

    def test_get_persona_list_none(self):
        process = ProcessExtractAward(id_schedule = None, id_log = None, id_robot = "1", priority = "1", log_file_path = None, parameters=None)
        list_awards = [{'createdBy': '00391433', 'creationDate': '2022-05-05T09:02:28.475Z', 'lastModifiedBy': '00391433', 'lastModifiedDate': '2022-05-05T09:04:35.943Z', 'id': 23, 'titulo': '', 'convocatoriaId': 35, 'codigoExterno': 'PID2019-106498GB-I00', 'codigoRegistroInterno': 'SGI_SLC2320220505', 'estado': {'createdBy': '00391433', 'creationDate': '2022-05-05T09:04:35.941Z', 'lastModifiedBy': '00391433', 'lastModifiedDate': '2022-05-05T09:04:35.941Z', 'id': 47, 'solicitudId': 23, 'estado': 'SOLICITADA', 'fechaEstado': '2022-05-05T09:02:37.084Z', 'comentario': ''}, 'creadorRef': '00391433', 'solicitanteRef': '28710458', 'observaciones': '', 'convocatoriaExterna': '', 'unidadGestionRef': '3', 'formularioSolicitud': 'PROYECTO', 'tipoSolicitudGrupo': None, 'activo': True},{"createdBy":"00391433","creationDate":"2022-05-09T14:20:32.068Z","lastModifiedBy":"00391433","lastModifiedDate":"2022-05-09T14:20:57.238Z","id":25,"titulo":"","convocatoriaId":35,"codigoExterno":"","codigoRegistroInterno":"SGI_SLC2520220509","estado":{"createdBy":"00391433","creationDate":"2022-05-09T14:20:57.238Z","lastModifiedBy":"00391433","lastModifiedDate":"2022-05-09T14:20:57.238Z","id":52,"solicitudId":25,"estado":"SOLICITADA","fechaEstado":"2022-05-09T14:20:42.496Z","comentario":""},"creadorRef":"00391433","solicitanteRef":"48495234","observaciones":"","convocatoriaExterna":"","unidadGestionRef":"3","formularioSolicitud":"PROYECTO","tipoSolicitudGrupo":None,"activo":True}]
        result = process.get_person_forms_t(None, '{"nombre":"ANTONIO FERNANDO","id":"28710458","numeroDocumento":"28710458H","tipoDocumento":{"id":"D","nombre":"DOCUMENTO NACIONAL DE IDENTIDAD"},"apellidos":"SKARMETA GOMEZ","sexo":{"id":"V","nombre":"Varon"},"personalPropio":true,"activo":true,"entidadPropiaRef":"Q3018001","emails":[{"email":"skarmeta@um.es","principal":true}]}')
        self.assertEqual(list(result.keys()), [])
        self.assertEqual(list(result.values()), [])

    def test_get_persona_no_list(self):
        process = ProcessExtractAward(id_schedule = None, id_log = None, id_robot = "1", priority = "1", log_file_path = None, parameters=None)
        list_awards = [{'createdBy': '00391433', 'creationDate': '2022-05-05T09:02:28.475Z', 'lastModifiedBy': '00391433', 'lastModifiedDate': '2022-05-05T09:04:35.943Z', 'id': 23, 'titulo': '', 'convocatoriaId': 35, 'codigoExterno': '', 'codigoRegistroInterno': 'SGI_SLC2320220505', 'estado': {'createdBy': '00391433', 'creationDate': '2022-05-05T09:04:35.941Z', 'lastModifiedBy': '00391433', 'lastModifiedDate': '2022-05-05T09:04:35.941Z', 'id': 47, 'solicitudId': 23, 'estado': 'SOLICITADA', 'fechaEstado': '2022-05-05T09:02:37.084Z', 'comentario': ''}, 'creadorRef': '00391433', 'solicitanteRef': '', 'observaciones': '', 'convocatoriaExterna': '', 'unidadGestionRef': '3', 'formularioSolicitud': 'PROYECTO', 'tipoSolicitudGrupo': None, 'activo': True},{"createdBy":"00391433","creationDate":"2022-05-09T14:20:32.068Z","lastModifiedBy":"00391433","lastModifiedDate":"2022-05-09T14:20:57.238Z","id":25,"titulo":"","convocatoriaId":35,"codigoExterno":"","codigoRegistroInterno":"SGI_SLC2520220509","estado":{"createdBy":"00391433","creationDate":"2022-05-09T14:20:57.238Z","lastModifiedBy":"00391433","lastModifiedDate":"2022-05-09T14:20:57.238Z","id":52,"solicitudId":25,"estado":"SOLICITADA","fechaEstado":"2022-05-09T14:20:42.496Z","comentario":""},"creadorRef":"00391433","solicitanteRef":"48495234","observaciones":"","convocatoriaExterna":"","unidadGestionRef":"3","formularioSolicitud":"PROYECTO","tipoSolicitudGrupo":None,"activo":True}]
        result = process.get_person_forms_t("", '{"nombre":"ANTONIO FERNANDO","id":"28710458","numeroDocumento":"28710458H","tipoDocumento":{"id":"D","nombre":"DOCUMENTO NACIONAL DE IDENTIDAD"},"apellidos":"SKARMETA GOMEZ","sexo":{"id":"V","nombre":"Varon"},"personalPropio":true,"activo":true,"entidadPropiaRef":"Q3018001","emails":[{"email":"skarmeta@um.es","principal":true}]}')
        self.assertEqual(list(result.keys()), [])
        self.assertEqual(list(result.values()), [])

if __name__ == '__main__':
    print('testExtractAwards')
    unittest.main()