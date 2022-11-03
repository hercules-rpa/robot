import sys
import os
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(os.path.dirname(currentdir))
sys.path.insert(1, parentdir)
print(currentdir, parentdir)
import unittest
import model.process.Process1.Subprocess.ProcessExtractArticles as ProcessExtractArticles
import model.process.ProcessGenerateTransferReport as ProcessGenerateTransferReport
import json
import pandas as pd


class TestExtractArticles(unittest.TestCase):
    def test_extract_articles_without_results(self):
        file = open("hercules-rpa/test/files/articles/articles-notresults.txt", "r")
        response_text = file.read()
        json_dict = json.loads(response_text)
        file.close()
        processArticles = ProcessExtractArticles.ProcessExtractArticles(id_schedule = None, id_log = None, id_robot = None, priority ="1", log_file_path = None, parameters=None)
        results = processArticles.process_results(pd.json_normalize(json_dict["results"]["bindings"]))
        self.assertEqual(len(results),0)  

    def test_extract_articles_janfeb_2021(self):
        file = open("hercules-rpa/test/files/articles/january-feb2021.txt", "r")
        response_text = file.read()
        json_dict = json.loads(response_text)
        file.close()
        processArticles = ProcessExtractArticles.ProcessExtractArticles(id_schedule = None, id_log = None, id_robot = None, priority = "1", log_file_path = None, parameters=None)
        results = processArticles.process_results(pd.json_normalize(json_dict["results"]["bindings"]))
        self.assertEqual(len(results), 472)    

    def test_extract_articles_january2021_march2022(self):
        file = open("hercules-rpa/test/files/articles/articles-enero2021-marzo2022.txt", "r")
        response_text = file.read()
        json_dict = json.loads(response_text)
        file.close()
        processArticles = ProcessExtractArticles.ProcessExtractArticles(id_schedule = None, id_log = None, id_robot = None, priority = "1", log_file_path = None, parameters=None)
        results = processArticles.process_results(pd.json_normalize(json_dict["results"]["bindings"]))
        self.assertEqual(len(results), 59)  

    def test_extract_articles_april2021(self):
        file = open("hercules-rpa/test/files/articles/april2021.txt", "r")
        response_text = file.read()
        json_dict = json.loads(response_text)
        file.close()
        processArticles = ProcessExtractArticles.ProcessExtractArticles(id_schedule = None, id_log = None, id_robot = None, priority = "1", log_file_path = None, parameters=None)
        results = processArticles.process_results(pd.json_normalize(json_dict["results"]["bindings"]))
        self.assertEqual(len(results), 35)  

    def test_extract_articles_mayjun_2021(self):
        file = open("hercules-rpa/test/files/articles/may-jun2021.txt", "r")
        response_text = file.read()
        json_dict = json.loads(response_text)
        file.close()
        processArticles = ProcessExtractArticles.ProcessExtractArticles(id_schedule = None, id_log = None, id_robot = None, priority = "1", log_file_path = None, parameters=None)
        results = processArticles.process_results(pd.json_normalize(json_dict["results"]["bindings"]))
        self.assertEqual(len(results), 72)   

    def test_extract_articles_janfeb_2022(self):
        file = open("hercules-rpa/test/files/articles/january-feb2022.txt", "r")
        response_text = file.read()
        json_dict = json.loads(response_text)
        file.close()
        processArticles = ProcessExtractArticles.ProcessExtractArticles(id_schedule = None, id_log = None, id_robot = None, priority = "1", log_file_path = None, parameters=None)
        results = processArticles.process_results(pd.json_normalize(json_dict["results"]["bindings"]))
        self.assertEqual(len(results), 232)    

    def test_extract_articles_april_2022(self):
        file = open("hercules-rpa/test/files/articles/april2022.txt", "r")
        response_text = file.read()
        json_dict = json.loads(response_text)
        file.close()
        processArticles = ProcessExtractArticles.ProcessExtractArticles(id_schedule = None, id_log = None, id_robot = None, priority = "1", log_file_path = None, parameters=None)
        results = processArticles.process_results(pd.json_normalize(json_dict["results"]["bindings"]))
        self.assertEqual(len(results), 29)  

    def test_extract_articles_maroct_2022(self):
        file = open("hercules-rpa/test/files/articles/mar-oct2022.txt", "r")
        response_text = file.read()
        json_dict = json.loads(response_text)
        file.close()
        processArticles = ProcessExtractArticles.ProcessExtractArticles(id_schedule = None, id_log = None, id_robot = None, priority = "1", log_file_path = None, parameters=None)
        results = processArticles.process_results(pd.json_normalize(json_dict["results"]["bindings"]))
        self.assertEqual(len(results), 156) 

    def test_extract_articles_may_2022(self):
        file = open("hercules-rpa/test/files/articles/may2022.txt", "r")
        response_text = file.read()
        json_dict = json.loads(response_text)
        file.close()
        processArticles = ProcessExtractArticles.ProcessExtractArticles(id_schedule = None, id_log = None, id_robot = None, priority = "1", log_file_path = None, parameters=None)
        results = processArticles.process_results(pd.json_normalize(json_dict["results"]["bindings"]))
        self.assertEqual(len(results), 14)     

    def test_extract_articles_junjul_2022(self):
        file = open("hercules-rpa/test/files/articles/jun-jul2022.txt", "r")
        response_text = file.read()
        json_dict = json.loads(response_text)
        file.close()
        processArticles = ProcessExtractArticles.ProcessExtractArticles(id_schedule = None, id_log = None, id_robot = None, priority = "1", log_file_path = None, parameters=None)
        results = processArticles.process_results(pd.json_normalize(json_dict["results"]["bindings"]))
        self.assertEqual(len(results), 41)               

    def test_extract_articles_with_results(self):
        file = open("hercules-rpa/test/files/articles/articles-results.txt", "r")
        response_text = file.read()
        json_dict = json.loads(response_text)
        file.close()
        processArticles = ProcessExtractArticles.ProcessExtractArticles(id_schedule = None, id_log = None, id_robot = None, priority = "1", log_file_path = None, parameters=None)
        results = processArticles.process_results(pd.json_normalize(json_dict["results"]["bindings"]))
        self.assertEqual(len(results), 3)
        self.assertEqual(len(results[0].authors),2)
        self.assertEqual(results[0].authors[0].name, 'Antonio Fernando Skarmeta Gomez')
        self.assertEqual(results[0].authors[1].name, 'Nombre Apellidos aaa')
        self.assertEqual(len(results[1].authors),1)
        self.assertEqual(results[1].authors[0].name, 'Antonio Fernando Skarmeta Gomez')
        self.assertEqual(len(results[2].authors),7)
        self.assertEqual(results[2].authors[0].name, 'Pablo Fernandez Saura')
        self.assertEqual(results[2].authors[1].name, 'Jorge Bernal Bernabe')
        self.assertEqual(results[2].authors[2].name, 'Antonio Fernando Skarmeta Gomez')
        self.assertEqual(results[2].authors[3].name, 'Jose Luis Hernandez Ramos')
        self.assertEqual(results[2].authors[4].name, 'Enrique Marmol Campos')
        self.assertEqual(results[2].authors[5].name, 'Aurora Gonzalez Vidal')
        self.assertEqual(results[2].authors[6].name, 'Gianmarco Baldini')

        process = ProcessGenerateTransferReport.ProcessGenerateTransferReport(id_schedule = None, id_log = None, id_robot = None, priority = "1", log_file_path = None, parameters=None)  
        msg_process = process.msg_articles(results)
        msg_test = '<b>ARTÍCULOS CIENTÍFICOS: Se han obtenido 3 artículos científicos.</b><br><b>ARTÍCULO CIENTÍFICO 1: </b><br>Nombre: AAATítulo de la publicación -otros<br>Autores: <br>- Antonio Fernando Skarmeta Gomez ORCID: 0000-0002-5525-1259<br>- Nombre Apellidos aaa<br>Fecha: 24/02/2022<br>Url: <a href="http://edma.gnoss.com/comunidad/hercules/recurso/art/C6D8CADB-BACA-4B77-9C14-E786ED62E66C" target="_blank">articulo1</a><br><b>ARTÍCULO CIENTÍFICO 2: </b><br>Nombre: Título de la publicación -revista<br>Nombre revista: Harm Reduction Journal<br>Autores: <br>- Antonio Fernando Skarmeta Gomez ORCID: 0000-0002-5525-1259<br>Fecha: 24/02/2022<br>Url: <a href="http://edma.gnoss.com/comunidad/hercules/recurso/art/75BCED58-A7A3-4CFB-896B-E623C1998105" target="_blank">articulo2</a><br><b>ARTÍCULO CIENTÍFICO 3: </b><br>Nombre: p Evaluating Federated Learning for intrusion detection in Internet of Things: Review and challengesXY<br>Autores: <br>- Pablo Fernandez Saura<br>- Jorge Bernal Bernabe ORCID: 0000-0002-7538-4788<br>- Antonio Fernando Skarmeta Gomez ORCID: 0000-0002-5525-1259<br>- Jose Luis Hernandez Ramos ORCID: 0000-0001-7697-116X<br>- Enrique Marmol Campos<br>- Aurora Gonzalez Vidal ORCID: 0000-0002-4398-0243<br>- Gianmarco Baldini<br>Fecha: 11/02/2022<br>Áreas científicas: Multidisciplinary, General Artificial Intelligence, General Medicine, Hardware and Architecture, General Medicine<br>Url: <a href="http://edma.gnoss.com/comunidad/hercules/recurso/art/9F89A166-B7D4-4AC8-91CC-68D4B6D7F82A" target="_blank">articulo3</a><br>'
        self.assertEqual(msg_test, str(msg_process))

    def test_extract_articles_january_march_2022(self):
        file = open("hercules-rpa/test/files/articles/articles-enero-marzo2022.txt", "r")
        response_text = file.read()
        json_dict = json.loads(response_text)
        file.close()
        processArticles = ProcessExtractArticles.ProcessExtractArticles(id_schedule = None, id_log = None, id_robot = None, priority = "1", log_file_path = None, parameters=None)
        results = processArticles.process_results(pd.json_normalize(json_dict["results"]["bindings"]))
        self.assertEqual(len(results), 7)        
        
    def test_articles_num_authors(self):
        file = open("hercules-rpa/test/files/articles/articles-authors.txt", "r")
        response_text = file.read()
        json_dict = json.loads(response_text)
        file.close()
        processArticles = ProcessExtractArticles.ProcessExtractArticles(id_schedule = None, id_log = None, id_robot = None, priority ="1", log_file_path = None, parameters=None)
        results = processArticles.process_results(pd.json_normalize(json_dict["results"]["bindings"]))
        self.assertEqual(results[0].doc, 'p Evaluating Federated Learning for intrusion detection in Internet of Things: Review and challengesXY')
        self.assertIsNone(results[0].magazine)
        self.assertEqual(results[0].date, '11/02/2022')
        self.assertEqual(results[0].areas, 'Multidisciplinary, General Artificial Intelligence, General Medicine, Hardware and Architecture, General Medicine')
        self.assertEqual(results[0].url, 'http://edma.gnoss.com/comunidad/hercules/recurso/art/9F89A166-B7D4-4AC8-91CC-68D4B6D7F82A')
        self.assertEqual(len(results[0].authors),7)   

if __name__ == '__main__':
    unittest.main()