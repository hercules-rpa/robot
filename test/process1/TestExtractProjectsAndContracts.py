import sys
import os
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(os.path.dirname(currentdir))
sys.path.insert(1, parentdir)
print(currentdir, parentdir)
import unittest
import json
import model.process.Process1.Subprocess.ProcessExtractProjectsAndContracts as ProcessExtractProjectsAndContracts

class TestExtractProjectsAndContracts(unittest.TestCase):

    def test_extract_projects_contracts_without_results(self):
        process = ProcessExtractProjectsAndContracts.ProcessExtractProjectsAndContracts(
            id_schedule=None, id_log=None, id_robot="1", priority="1", log_file_path=None, parameters=None)
    
        results = process.process_results(None, False)
        self.assertEqual(results[0][1], 0) #projects
        self.assertEqual(results[0][0],'<b>PROYECTOS: No se han obtenido proyectos. </b><br>')
        self.assertEqual(results[1][1], 0)
        self.assertEqual(results[1][0], '<b>CONTRATOS: No se han obtenido contratos. </b><br>')

    def test_extract_projects_contracts_with_results1(self):
        file = open("hercules-rpa/test/files/projects/projects1.txt", "r")
        response_text = file.read()
        file.close()
        process = ProcessExtractProjectsAndContracts.ProcessExtractProjectsAndContracts(
            id_schedule=None, id_log=None, id_robot="1", priority="1", log_file_path=None, parameters=None)
    
        results = process.process_results(response_text, False)
        self.assertEqual(results[0][1], 3) #projects
        self.assertEqual(results[1][1], 0)

    def test_extract_projects_contracts_2(self):
        file = open("hercules-rpa/test/files/projects/projects-2.txt", "r")
        response_text = file.read()
        file.close()
        process = ProcessExtractProjectsAndContracts.ProcessExtractProjectsAndContracts(
            id_schedule=None, id_log=None, id_robot="1", priority="1", log_file_path=None, parameters=None)
    
        results = process.process_results(response_text, False)
        self.assertEqual(results[0][1], 3) #projects
        self.assertEqual(results[1][1], 0)

    def test_extract_projects_contracts_1(self):
        file = open("hercules-rpa/test/files/projects/projects1.txt", "r")
        response_text = file.read()
        file.close()
        process = ProcessExtractProjectsAndContracts.ProcessExtractProjectsAndContracts(
            id_schedule=None, id_log=None, id_robot="1", priority="1", log_file_path=None, parameters=None)
    
        results = process.process_results(response_text, False)
        self.assertEqual(results[0][1], 3) 
        self.assertEqual(results[1][1], 0)
    
    def test_extract_projects_contracts_3(self):
        file = open("hercules-rpa/test/files/projects/project-3.txt", "r")
        response_text = file.read()
        file.close()
        process = ProcessExtractProjectsAndContracts.ProcessExtractProjectsAndContracts(
            id_schedule=None, id_log=None, id_robot="1", priority="1", log_file_path=None, parameters=None)
    
        results = process.process_results(response_text, False)
        self.assertEqual(results[0][1], 0) 
        self.assertEqual(results[1][1], 1)
    
    def test_extract_projects_contracts_4(self):
        file = open("hercules-rpa/test/files/projects/project-4.txt", "r")
        response_text = file.read()
        file.close()
        process = ProcessExtractProjectsAndContracts.ProcessExtractProjectsAndContracts(
            id_schedule=None, id_log=None, id_robot="1", priority="1", log_file_path=None, parameters=None)
    
        results = process.process_results(response_text, False)
        self.assertEqual(results[0][1], 1) 
        self.assertEqual(results[1][1], 0)
    
    def test_extract_projects_contracts_5(self):
        file = open("hercules-rpa/test/files/projects/project-5.txt", "r")
        response_text = file.read()
        file.close()
        process = ProcessExtractProjectsAndContracts.ProcessExtractProjectsAndContracts(
            id_schedule=None, id_log=None, id_robot="1", priority="1", log_file_path=None, parameters=None)
    
        results = process.process_results(response_text, False)
        self.assertEqual(results[0][1], 2) 
        self.assertEqual(results[1][1], 1)

    def test_extract_projects_contracts_6(self):
        file = open("hercules-rpa/test/files/projects/project-6.txt", "r")
        response_text = file.read()
        file.close()
        process = ProcessExtractProjectsAndContracts.ProcessExtractProjectsAndContracts(
            id_schedule=None, id_log=None, id_robot="1", priority="1", log_file_path=None, parameters=None)
    
        results = process.process_results(response_text, False)
        self.assertEqual(results[0][1], 1) 
        self.assertEqual(results[1][1], 2)
    
    def test_extract_projects_contracts_7(self):
        file = open("hercules-rpa/test/files/projects/project-7.txt", "r")
        response_text = file.read()
        file.close()
        process = ProcessExtractProjectsAndContracts.ProcessExtractProjectsAndContracts(
            id_schedule=None, id_log=None, id_robot="1", priority="1", log_file_path=None, parameters=None)
    
        results = process.process_results(response_text, False)
        self.assertEqual(results[0][1], 1) 
        self.assertEqual(results[1][1], 1)

    def test_extract_projects_contracts_8(self):
        file = open("hercules-rpa/test/files/projects/projects-8.txt", "r")
        response_text = file.read()
        file.close()
        process = ProcessExtractProjectsAndContracts.ProcessExtractProjectsAndContracts(
            id_schedule=None, id_log=None, id_robot="1", priority="1", log_file_path=None, parameters=None)
    
        results = process.process_results(response_text, False)
        self.assertEqual(results[0][1], 3) 
        self.assertEqual(results[1][1], 1)

    def test_extract_projects_contracts_2016_2020(self):
        file = open("hercules-rpa/test/files/projects/projects-2016-2020.txt", "r")
        response_text = file.read()
        file.close()
        process = ProcessExtractProjectsAndContracts.ProcessExtractProjectsAndContracts(
            id_schedule=None, id_log=None, id_robot="1", priority="1", log_file_path=None, parameters=None)
    
        results = process.process_results(response_text, False)
        self.assertEqual(results[0][1], 1) 
        self.assertEqual(results[1][1], 0)
    
    def test_extract_projects_contracts_2021(self):
        file = open("hercules-rpa/test/files/projects/projects-2021.txt", "r")
        response_text = file.read()
        file.close()
        process = ProcessExtractProjectsAndContracts.ProcessExtractProjectsAndContracts(
            id_schedule=None, id_log=None, id_robot="1", priority="1", log_file_path=None, parameters=None)
    
        results = process.process_results(response_text, False)
        self.assertEqual(results[0][1], 2) 
        self.assertEqual(results[1][1], 1)
    
    def test_extract_projects_contracts_2020_2022(self):
        file = open("hercules-rpa/test/files/projects/projects-2020-2022.txt", "r")
        response_text = file.read()
        file.close()
        process = ProcessExtractProjectsAndContracts.ProcessExtractProjectsAndContracts(
            id_schedule=None, id_log=None, id_robot="1", priority="1", log_file_path=None, parameters=None)
    
        results = process.process_results(response_text, False)
        self.assertEqual(results[0][1], 8) 
        self.assertEqual(results[1][1], 5)
    
    def test_extract_projects_contracts_2022(self):
        file = open("hercules-rpa/test/files/projects/projects-2022.txt", "r")
        response_text = file.read()
        file.close()
        process = ProcessExtractProjectsAndContracts.ProcessExtractProjectsAndContracts(
            id_schedule=None, id_log=None, id_robot="1", priority="1", log_file_path=None, parameters=None)
    
        results = process.process_results(response_text, False)
        self.assertEqual(results[0][1], 3) 
        self.assertEqual(results[1][1], 1)


    def test_extract_projects_contracts_errors(self):
        file = open("hercules-rpa/test/files/projects/projects-error.txt", "r")
        response_text = file.read()
        file.close()
        process = ProcessExtractProjectsAndContracts.ProcessExtractProjectsAndContracts(
            id_schedule=None, id_log=None, id_robot="1", priority="1", log_file_path=None, parameters=None)
        
        json_dict = json.loads(response_text)
        msg = process.msg_element(json_dict[0], False, True)
        self.assertEqual(msg,'Título: pueba<br>Fecha inicio: 15/03/2022<br>Fecha fin: 31/03/2022<br>')
        

if __name__ == '__main__':
    unittest.main()