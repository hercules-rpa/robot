import sys
import os
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(os.path.dirname(currentdir))
sys.path.insert(1, parentdir)
print(currentdir, parentdir)
import unittest
from datetime import datetime
import model.process.Process1.Subprocess.ProcessExtractThesis as ProcessExtractThesis
import json

class TestExtractThesis(unittest.TestCase):

    def test_extract_thesis_without_results(self):
        processThesis = ProcessExtractThesis.ProcessExtractThesis(id_schedule = None, id_log = None, id_robot = None, priority = "1", log_file_path = None, parameters=None)
        tupla = processThesis.process_results(None, datetime(2022,1,1), datetime(2022,5,10))
        self.assertEqual(tupla[0], 0)
        self.assertEqual(tupla[1],'<b>TESIS: No se ha obtenido ningún elemento.</b><br>')  

    def test_extract_thesis_january_march(self):
        file = open("hercules-rpa/test/files/thesis/tesis.txt", "r")
        response_text = file.read()
        json_dict = json.loads(response_text)
        file.close()
        processThesis = ProcessExtractThesis.ProcessExtractThesis(
            id_schedule=None, id_log=None, id_robot="1", priority="1", log_file_path=None, parameters=None)
    
        tupla = processThesis.process_results(json_dict,datetime(2022,1,1), datetime(2022,5,17))
        self.assertEqual(tupla[0], 0)  
        self.assertEqual(tupla[1],'<b>TESIS: No se ha obtenido ningún elemento.</b><br>')  

    def test_extract_thesis_1(self):
        file = open("hercules-rpa/test/files/thesis/thesis-4.txt", "r")
        response_text = file.read()
        json_dict = json.loads(response_text)
        file.close()
        processThesis = ProcessExtractThesis.ProcessExtractThesis(
            id_schedule=None, id_log=None, id_robot="1", priority="1", log_file_path=None, parameters=None)
    
        tupla = processThesis.process_results(json_dict,datetime(2022,1,1), datetime(2022,5,17))
        self.assertEqual(tupla[0], 11)  

    def test_extract_thesis_2(self):
        file = open("hercules-rpa/test/files/thesis/thesis-5.txt", "r")
        response_text = file.read()
        json_dict = json.loads(response_text)
        file.close()
        processThesis = ProcessExtractThesis.ProcessExtractThesis(
            id_schedule=None, id_log=None, id_robot="1", priority="1", log_file_path=None, parameters=None)
    
        tupla = processThesis.process_results(json_dict,datetime(2022,1,1), datetime(2022,5,17))
        self.assertEqual(tupla[0], 3) 
    
    def test_extract_thesis_2020(self):
        file = open("hercules-rpa/test/files/thesis/thesis2020.txt", "r")
        response_text = file.read()
        json_dict = json.loads(response_text)
        file.close()
        processThesis = ProcessExtractThesis.ProcessExtractThesis(
            id_schedule=None, id_log=None, id_robot="1", priority="1", log_file_path=None, parameters=None)
    
        tupla = processThesis.process_results(json_dict,datetime(2020,1,1), datetime(2020,12,31))
        self.assertEqual(tupla[0], 213)

    def test_extract_thesis_2020_may_december(self):
        file = open("hercules-rpa/test/files/thesis/thesis2020.txt", "r")
        response_text = file.read()
        json_dict = json.loads(response_text)
        file.close()
        processThesis = ProcessExtractThesis.ProcessExtractThesis(
            id_schedule=None, id_log=None, id_robot="1", priority="1", log_file_path=None, parameters=None)
    
        tupla = processThesis.process_results(json_dict,datetime(2020,5,1), datetime(2020,12,31))
        self.assertEqual(tupla[0], 178)  

    def test_extract_thesis_2021(self):
        file = open("hercules-rpa/test/files/thesis/thesis2021.txt", "r")
        response_text = file.read()
        json_dict = json.loads(response_text)
        file.close()
        processThesis = ProcessExtractThesis.ProcessExtractThesis(
            id_schedule=None, id_log=None, id_robot="1", priority="1", log_file_path=None, parameters=None)
    
        tupla = processThesis.process_results(json_dict,datetime(2021,1,1), datetime(2021,12,31))
        self.assertEqual(tupla[0], 300) 
    
    def test_extract_thesis_2021_july_october(self):
        file = open("hercules-rpa/test/files/thesis/thesis2021.txt", "r")
        response_text = file.read()
        json_dict = json.loads(response_text)
        file.close()
        processThesis = ProcessExtractThesis.ProcessExtractThesis(
            id_schedule=None, id_log=None, id_robot="1", priority="1", log_file_path=None, parameters=None)
    
        tupla = processThesis.process_results(json_dict,datetime(2021,7,1), datetime(2021,10,31))
        self.assertEqual(tupla[0], 87)
    
    def test_extract_thesis_2022(self):
        file = open("hercules-rpa/test/files/thesis/thesis2022.txt", "r")
        response_text = file.read()
        json_dict = json.loads(response_text)
        file.close()
        processThesis = ProcessExtractThesis.ProcessExtractThesis(
            id_schedule=None, id_log=None, id_robot="1", priority="1", log_file_path=None, parameters=None)
    
        tupla = processThesis.process_results(json_dict,datetime(2022,1,1), datetime(2022,12,31))
        self.assertEqual(tupla[0], 52) 
    
    def test_extract_thesis_2022_january_april(self):
        file = open("hercules-rpa/test/files/thesis/thesis2022.txt", "r")
        response_text = file.read()
        json_dict = json.loads(response_text)
        file.close()
        processThesis = ProcessExtractThesis.ProcessExtractThesis(
            id_schedule=None, id_log=None, id_robot="1", priority="1", log_file_path=None, parameters=None)
    
        tupla = processThesis.process_results(json_dict,datetime(2022,1,1), datetime(2022,4,30))
        self.assertEqual(tupla[0], 50) 

    def test_extract_thesis_2022_april_october(self):
        file = open("hercules-rpa/test/files/thesis/thesis2022.txt", "r")
        response_text = file.read()
        json_dict = json.loads(response_text)
        file.close()
        processThesis = ProcessExtractThesis.ProcessExtractThesis(
            id_schedule=None, id_log=None, id_robot="1", priority="1", log_file_path=None, parameters=None)
    
        tupla = processThesis.process_results(json_dict,datetime(2022,4,1), datetime(2022,10,30))
        self.assertEqual(tupla[0], 4) 

    def test_extract_thesis_2019(self):
        file = open("hercules-rpa/test/files/thesis/thesis2019.txt", "r")
        response_text = file.read()
        json_dict = json.loads(response_text)
        file.close()
        processThesis = ProcessExtractThesis.ProcessExtractThesis(
            id_schedule=None, id_log=None, id_robot="1", priority="1", log_file_path=None, parameters=None)
    
        tupla = processThesis.process_results(json_dict,datetime(2019,1,1), datetime(2019,12,31))
        self.assertEqual(tupla[0], 218)

    def test_extract_thesis_2019_october_december(self):
        file = open("hercules-rpa/test/files/thesis/thesis2019.txt", "r")
        response_text = file.read()
        json_dict = json.loads(response_text)
        file.close()
        processThesis = ProcessExtractThesis.ProcessExtractThesis(
            id_schedule=None, id_log=None, id_robot="1", priority="1", log_file_path=None, parameters=None)
    
        tupla = processThesis.process_results(json_dict,datetime(2019,10,1), datetime(2019,12,31))
        self.assertEqual(tupla[0], 109)

    def test_extract_thesis_2018(self):
        file = open("hercules-rpa/test/files/thesis/thesis2018.txt", "r")
        response_text = file.read()
        json_dict = json.loads(response_text)
        file.close()
        processThesis = ProcessExtractThesis.ProcessExtractThesis(
            id_schedule=None, id_log=None, id_robot="1", priority="1", log_file_path=None, parameters=None)
    
        tupla = processThesis.process_results(json_dict,datetime(2018,1,1), datetime(2018,12,31))
        self.assertEqual(tupla[0], 209) 
    
    def test_extract_thesis_2018_january_october(self):
        file = open("hercules-rpa/test/files/thesis/thesis2018.txt", "r")
        response_text = file.read()
        json_dict = json.loads(response_text)
        file.close()
        processThesis = ProcessExtractThesis.ProcessExtractThesis(
            id_schedule=None, id_log=None, id_robot="1", priority="1", log_file_path=None, parameters=None)
    
        tupla = processThesis.process_results(json_dict,datetime(2018,1,1), datetime(2018,10,31))
        self.assertEqual(tupla[0], 136) 



if __name__ == '__main__':
    unittest.main()