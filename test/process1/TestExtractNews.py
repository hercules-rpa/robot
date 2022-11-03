import datetime
import sys
import os
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(os.path.dirname(currentdir))
sys.path.insert(1, parentdir)
print(currentdir, parentdir)
import model.process.Process1.Subprocess.ProcessExtractNews as ProcessExtractNews
import unittest


class TestExtractNews(unittest.TestCase):
    def test_extract_news_nodes(self):
        process = ProcessExtractNews.ProcessExtractNews(
            id_schedule=None, id_log=None, id_robot="1CLE", priority="1", log_file_path=None, parameters=None)

        params = {}
        params["filename"] = "hercules-rpa/test/files/news/notas-de-prensa.xml"
        # parámetros erróneos, no debe obtener nodos y tampoco crear excepciones
        params["nodos"] = {"entry": ["title", "id", "dc:creator", "dc:date"]}
        nodes = process.get_newsnodes(params)
        self.assertEqual(nodes, [])

        params["nodos"] = {"item": ["title", "id", "dc:creator", "dc:date"]}
        nodes = process.get_newsnodes(params)
        self.assertEqual(len(nodes), 20)

        params["filename"] = "hercules-rpa/test/files/news/ucc.xml"
        params["nodos"] = {"entry": ["title", "id", "dc:creator", "dc:date"]}
        nodes = process.get_newsnodes(params)
        self.assertEqual(len(nodes), 20)
    
    def test_extract_news_notas_oct(self):
        process = ProcessExtractNews.ProcessExtractNews(
            id_schedule=None, id_log=None, id_robot="1CLE", priority="1", log_file_path=None, parameters=None)

        params = {}
        params["filename"] = "hercules-rpa/test/files/news/notas-de-prensa-oct.xml"
        params["nodos"] = {"item": ["title", "id", "dc:creator", "dc:date"]}
        nodes = process.get_newsnodes(params)
        self.assertEqual(len(nodes), 20)
    
    def test_extract_news_notas_oct1(self):
        process = ProcessExtractNews.ProcessExtractNews(
            id_schedule=None, id_log=None, id_robot="1CLE", priority="1", log_file_path=None, parameters=None)

        params = {}
        params["filename"] = "hercules-rpa/test/files/news/notas-de-prensa-oct1.xml"
        params["nodos"] = {"item": ["title", "id", "dc:creator", "dc:date"]}
        nodes = process.get_newsnodes(params)
        self.assertEqual(len(nodes), 6)

    def test_extract_news_notas_oct2(self):
        process = ProcessExtractNews.ProcessExtractNews(
            id_schedule=None, id_log=None, id_robot="1CLE", priority="1", log_file_path=None, parameters=None)

        params = {}
        params["filename"] = "hercules-rpa/test/files/news/notas-de-prensa-oct2.xml"
        params["nodos"] = {"item": ["title", "id", "dc:creator", "dc:date"]}
        nodes = process.get_newsnodes(params)
        self.assertEqual(len(nodes), 2)

    def test_extract_news_notas_oct12(self):
        process = ProcessExtractNews.ProcessExtractNews(
            id_schedule=None, id_log=None, id_robot="1CLE", priority="1", log_file_path=None, parameters=None)

        params = {}
        params["filename"] = "hercules-rpa/test/files/news/notas-de-prensa-oct12.xml"
        params["nodos"] = {"item": ["title", "id", "dc:creator", "dc:date"]}
        nodes = process.get_newsnodes(params)
        self.assertEqual(len(nodes), 12)

    def test_extract_news_notas_oct9(self):
        process = ProcessExtractNews.ProcessExtractNews(
            id_schedule=None, id_log=None, id_robot="1CLE", priority="1", log_file_path=None, parameters=None)

        params = {}
        params["filename"] = "hercules-rpa/test/files/news/notas-de-prensa-oct9.xml"
        params["nodos"] = {"item": ["title", "id", "dc:creator", "dc:date"]}
        nodes = process.get_newsnodes(params)
        self.assertEqual(len(nodes), 9)
    
    def test_extract_news_notas_oct_without_results(self):
        process = ProcessExtractNews.ProcessExtractNews(
            id_schedule=None, id_log=None, id_robot="1CLE", priority="1", log_file_path=None, parameters=None)

        params = {}
        params["filename"] = "hercules-rpa/test/files/news/notas-de-prensa-oct-without-results.xml"
        params["nodos"] = {"item": ["title", "id", "dc:creator", "dc:date"]}
        nodes = process.get_newsnodes(params)
        self.assertEqual(len(nodes), 0)   

    def test_extract_news_ucc_oct(self):
        process = ProcessExtractNews.ProcessExtractNews(
            id_schedule=None, id_log=None, id_robot="1CLE", priority="1", log_file_path=None, parameters=None)

        params = {}
        params["filename"] = "hercules-rpa/test/files/news/ucc-oct.xml"
        params["nodos"] = {"entry": ["title", "id", "dc:creator", "dc:date"]}
        nodes = process.get_newsnodes(params)
        self.assertEqual(len(nodes), 20)

    def test_extract_news_ucc_oct1(self):
        process = ProcessExtractNews.ProcessExtractNews(
            id_schedule=None, id_log=None, id_robot="1CLE", priority="1", log_file_path=None, parameters=None)

        params = {}
        params["filename"] = "hercules-rpa/test/files/news/ucc-oct1.xml"
        params["nodos"] = {"entry": ["title", "id", "dc:creator", "dc:date"]}
        nodes = process.get_newsnodes(params)
        self.assertEqual(len(nodes), 16) 
    
    def test_extract_news_ucc_oct2(self):
        process = ProcessExtractNews.ProcessExtractNews(
            id_schedule=None, id_log=None, id_robot="1CLE", priority="1", log_file_path=None, parameters=None)

        params = {}
        params["filename"] = "hercules-rpa/test/files/news/ucc-oct2.xml"
        params["nodos"] = {"entry": ["title", "id", "dc:creator", "dc:date"]}
        nodes = process.get_newsnodes(params)
        self.assertEqual(len(nodes), 14)
    
    def test_extract_news_ucc_oct3(self):
        process = ProcessExtractNews.ProcessExtractNews(
            id_schedule=None, id_log=None, id_robot="1CLE", priority="1", log_file_path=None, parameters=None)

        params = {}
        params["filename"] = "hercules-rpa/test/files/news/ucc-oct3.xml"
        params["nodos"] = {"entry": ["title", "id", "dc:creator", "dc:date"]}
        nodes = process.get_newsnodes(params)
        self.assertEqual(len(nodes), 13)

    def test_extract_news_ucc_oct4(self):
        process = ProcessExtractNews.ProcessExtractNews(
            id_schedule=None, id_log=None, id_robot="1CLE", priority="1", log_file_path=None, parameters=None)

        params = {}
        params["filename"] = "hercules-rpa/test/files/news/ucc-oct4.xml"
        params["nodos"] = {"entry": ["title", "id", "dc:creator", "dc:date"]}
        nodes = process.get_newsnodes(params)
        self.assertEqual(len(nodes), 11)

    def test_extract_news_ucc_oct6(self):
        process = ProcessExtractNews.ProcessExtractNews(
            id_schedule=None, id_log=None, id_robot="1CLE", priority="1", log_file_path=None, parameters=None)

        params = {}
        params["filename"] = "hercules-rpa/test/files/news/ucc-oct6.xml"
        params["nodos"] = {"entry": ["title", "id", "dc:creator", "dc:date"]}
        nodes = process.get_newsnodes(params)
        self.assertEqual(len(nodes), 9)

    def test_extract_news_ucc_oct7(self):
        process = ProcessExtractNews.ProcessExtractNews(
            id_schedule=None, id_log=None, id_robot="1CLE", priority="1", log_file_path=None, parameters=None)

        params = {}
        params["filename"] = "hercules-rpa/test/files/news/ucc-oct7.xml"
        params["nodos"] = {"entry": ["title", "id", "dc:creator", "dc:date"]}
        nodes = process.get_newsnodes(params)
        self.assertEqual(len(nodes), 3)

    def test_extract_news_sala_ucc(self):
        process = ProcessExtractNews.ProcessExtractNews(
            id_schedule=None, id_log=None, id_robot="1", priority="1", log_file_path=None, parameters=None)
        params = {}
        params["filename"] = "hercules-rpa/test/files/news/ucc-2.xml"
        params["nodos"] = {"entry": ["title", "id", "dc:creator", "dc:date"]}
        nodes = process.get_newsnodes(params)
        self.assertEqual(len(nodes), 3)

        news = process.process_news(nodes, datetime.datetime(2022, 5, 1),
                                    datetime.datetime(2022, 5, 10))
        self.assertEqual(len(news), 3)

        self.assertEqual(news[0].title, 
                        'Una investigación de la UMU genera embriones porcinos editados genéticamente para hallar nuevas terapias en humanos')
        self.assertEqual(news[0].author, 'DELFINA')
        self.assertEqual(news[0].url, 'https://www.um.es/web/ucc/inicio/-/asset_publisher/qQfO4ukErIc3/content/id/30991266')

        self.assertEqual(news[1].title, 'La UMU estudia la transmisión de patógenos entre los polinizadores')
        self.assertEqual(news[1].author, 'DELFINA')
        self.assertEqual(news[1].url, 'https://www.um.es/web/ucc/inicio/-/asset_publisher/qQfO4ukErIc3/content/id/30970159')

        self.assertEqual(news[2].title, 
                        'Seis equipos se alzan con el premio del concurso Math_talentUM')
        self.assertEqual(news[2].author, 'PAULA')
        self.assertEqual(news[2].url, 'https://www.um.es/web/ucc/inicio/-/asset_publisher/qQfO4ukErIc3/content/id/30941985')

    def test_extract_news_nprensa(self):
        process = ProcessExtractNews.ProcessExtractNews(
            id_schedule=None, id_log=None, id_robot="1", priority="1", log_file_path=None, parameters=None)
        params = {}
        params["filename"] = "hercules-rpa/test/files/news/notas-de-prensa-2.xml"
        params["nodos"] = {"item": ["title", "link", "dc:creator", "dc:date"]}
        nodes = process.get_newsnodes(params)
        self.assertEqual(len(nodes), 2)

        news = process.process_news(nodes, datetime.datetime(year=2022, month=5, day=1),
                                    datetime.datetime(year=2022, month=5, day=10))
        self.assertEqual(len(news), 2)

        self.assertEqual(news[0].title,'La sala La Capilla de la UMU acoge una instalación de Javier Pividal')
        self.assertEqual(news[0].author, 'ANA SORO LAVELLA')
        self.assertEqual(news[1].title, 'Seis equipos se alzan con el premio del concurso Math_talentUM')
        self.assertEqual(news[1].author, 'DELFINA')


if __name__ == '__main__':
    unittest.main()
