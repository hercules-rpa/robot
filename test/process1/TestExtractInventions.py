import json
import sys
import os
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(os.path.dirname(currentdir))
sys.path.insert(1, parentdir)
print(currentdir, parentdir)
import unittest
import model.process.Process1.Subprocess.ProcessExtractInventions as ProcessExtractInventions

class TestExtractInventions(unittest.TestCase):
    def test_invenciones1(self):
        file = open("hercules-rpa/test/files/invenciones/invenciones-1.txt", "r")
        response_text = file.read()
        file.close()
        process = ProcessExtractInventions.ProcessExtractInventions(
            id_schedule=None, id_log=None, id_robot="1", priority="1", log_file_path=None, parameters=None)
        result = process.process_results(response_text, False)
        self.assertEqual(result[0][0], 0)
        self.assertEqual(result[1][0], 1)

    def test_invenciones4(self):
        file = open("hercules-rpa/test/files/invenciones/invenciones-4.txt", "r")
        response_text = file.read()
        file.close()
        process = ProcessExtractInventions.ProcessExtractInventions(
            id_schedule=None, id_log=None, id_robot="1", priority="1", log_file_path=None, parameters=None)
        result = process.process_results(response_text, False)
        self.assertEqual(result[0][0], 3)
        self.assertEqual(result[1][0], 1)


    def test_invenciones_without_results(self):
        process = ProcessExtractInventions.ProcessExtractInventions(
            id_schedule=None, id_log=None, id_robot="1", priority="1", log_file_path=None, parameters=None)
        result = process.process_results(None, False)
        self.assertEqual(result[0][0], 0) #prop.industrial
        self.assertEqual(result[1][0], 0) #prop.intelectual

    def test_solicitud(self):
        file = open("hercules-rpa/test/files/invenciones/invenciones-solicitud-5.txt", "r")
        response_text = file.read()
        file.close()
        process = ProcessExtractInventions.ProcessExtractInventions(
            id_schedule=None, id_log=None, id_robot="1", priority="1", log_file_path=None, parameters=None)
        sol = process.msg_requests(json.loads(response_text)[0], 1)
        self.assertEqual(sol, 'SOLICITUD 1: <br>Título: Patente<br>Número solicitud: 123XTP<br>Fecha prioridad: 28/02/2022<br>Fecha fin prioridad: 31/03/2022<br>') #prop.industrial



if __name__ == '__main__':
    unittest.main()