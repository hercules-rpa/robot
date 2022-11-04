import sys
import os
import datetime
import aspose.words as aw
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(os.path.dirname(currentdir))
sys.path.insert(1, parentdir)
from model.process.Process2.Entities.Enums.ResearcherIdentifyType import ResearcherIdentifyType
from model.process.Process2.Entities.Committee.Committee import Committee

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(os.path.dirname(currentdir))
sys.path.insert(1, parentdir)
print(currentdir, parentdir)
import unittest
from model.process.Process2.Entities.Report import Report
from model.process.Process2.Entities.ResearcherData import ResearcherData
from model.process.Process2.Entities.RO import RO
import model.process.ProcessSexenios as ProcessSexenios
from model.process.Process2.Entities.Evaluations.SexenioEvaluation import ClassificationInfo, SexenioEvaluation

import json
import pandas as pd

class TestSexenios(unittest.TestCase):

    def get_articles(self, filename) -> list:
        file = open(filename, "r")
        text = file.read()
        file.close()
        arts_json = json.loads(text)
        articles = []
        
        for element in arts_json['bindings']:
            df = pd.json_normalize(element)
            aux = df.iloc[0]
            article = RO(title=aux["titulo.value"],publication_type=aux["tipoProduccion.value"],
            publication_date=aux["fechaPublicacion.value"], wos_cites=aux["citasWos.value"],
            position=aux["publicationPosition.value"],num_magazines=aux["journalNumberInCat.value"],
            magazine=aux["nombreRevista.value"],impact=aux["indiceImpacto.value"],quartile=aux["cuartil.value"])
            
            if 'doi.value' in df:
                article.doi = aux['doi.value']
            if 'issn.value' in df:
                article.issn = aux["issn.value"]
            if 'paginaInicio.value' in df:
                article.start_page = aux["paginaInicio.value"]
            if 'paginaFin.value' in df:
                article.end_page = aux["paginaFin.value"]
            if 'volumen.value' in df:
                article.volume = aux["volumen.value"]
            if 'editorial.value' in df:
                article.editorial=aux["editorial.value"]
            if 'numero.value' in df:
                article.number = aux["numero.value"]
            if 'citasScopus.value' in df:
                article.scopus_cites = aux["citasScopus.value"]
            if 'citasSemanticScholar.value' in df:    
                article.ss_cites = aux["citasSemanticScholar.value"]
            
            #moqueo la posición del investigador en la lista de autores
            article.author_position = 1
            articles.append(article)
        return articles

    def test_period(self):
        processSexenios = ProcessSexenios.ProcessSexenios(id_schedule = None, id_log = None, id_robot="1", priority ="1", log_file_path = None, parameters=None)
        results = processSexenios.get_period_array("2012-2019")
        array= [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
        self.assertEqual(results,array)

    def test_period_formatter(self):
        processSexenios = ProcessSexenios.ProcessSexenios(id_schedule = None, id_log = None, id_robot="1", priority ="1", log_file_path = None, parameters=None)
        periodo="2012-2019"
        results = processSexenios.get_period(periodo)
        string= "2012,2013,2014,2015,2016,2017,2018,2019"
        self.assertEqual(results,string)
    
    def test_get_researcherInfo(self):
        params = {"investigador": "0000-0002-5525-1259"}
        process = ProcessSexenios.ProcessSexenios(id_schedule = None, id_log = None, id_robot="1", priority ="1", log_file_path = None, parameters=None)
        researcherInfo = process.get_researcher_info(params)        
        self.assertEqual(researcherInfo[1],"0000-0002-5525-1259")

        params = {"investigador": "prueba@treelogic.com"}
        researcherInfo = process.get_researcher_info(params)        
        self.assertEqual(researcherInfo[1],"prueba@treelogic.com")

        params = {"investigador": "prueba@treelogic.com"}
        researcherInfo = process.get_researcher_info(params)        
        self.assertEqual(researcherInfo[1],"prueba@treelogic.com")

        params = {"investigador": "12345678"}
        researcherInfo = process.get_researcher_info(params)        
        self.assertEqual(researcherInfo[1],"12345678")

        params = {"investigador": "1234567"}
        researcherInfo = process.get_researcher_info(params)      
        self.assertIsNone(researcherInfo[1])

        params = {"investigador": "prueba@"}
        researcherInfo = process.get_researcher_info(params)      
        self.assertIsNone(researcherInfo[1])

        params = {"investigador": "0000-0002-5525-12"}
        researcherInfo = process.get_researcher_info(params)      
        self.assertIsNone(researcherInfo[1])

    def test_print_researcher(self):
        """
        Test que evalúa la impresión de los datos del investigador.
        """
        #Parámetros
        params = {"investigador": "0000-0002-5525-1259", "comite": "7", 
        "periodo": "2016-2021" }

        #Informe
        informe = Report()
        informe.add_title('Informe de autoevaluación de la investigación para la preparación de un sexenio')
        document = informe.get_document()

        #Datos del investigador
        f = open("hercules-rpa/test/files/sexenios/researcher_info.json","r")
        df = pd.json_normalize(json.loads(f.read())["results"]["bindings"])
        researcherData = ResearcherData()
        researcherData.set_properties(df)
        f.close()

        process = ProcessSexenios.ProcessSexenios(id_schedule = None, id_log = None, id_robot="1", priority ="1", log_file_path = None, parameters=None)
        id_investigador = process.get_researcher_info(params)
        comite = process.get_committee(params['comite'])
        periodo = process.get_period("2016-2021")
        process.print_researcher_data(document, researcherData, id_investigador, comite, periodo)
        docname = process.save_report(document, researcherData.name, True)
        
        docA = aw.Document("hercules-rpa/test/process2/files/InformeSexeniosAntonioFernandoSkarmetaGomezInvestigador.docx")
        docB = aw.Document(docname)

        docA.compare(docB, "user", datetime.datetime.today())
        self.assertEqual(docA.revisions.count, 0)
        
    def test_print_scientific_production(self):
        """
        Test que evalúa la impresión de la baremación del investigador.
        """
        #Parámetros
        params = {"tipoId": 3, "investigador": "0000-0002-5525-1259", "comite": "7", "periodo": "2016-2021" }        #Informe
        report = Report()
        report.add_title('Informe de autoevaluación de la investigación para la preparación de un sexenio')
        document = report.get_document()

        #Datos del investigador
        f = open("hercules-rpa/test/files/sexenios/researcher_info.json","r")
        df = pd.json_normalize(json.loads(f.read())["results"]["bindings"])
        researcherData = ResearcherData()
        researcherData.set_properties(df)
        f.close()

        process = ProcessSexenios.ProcessSexenios(id_schedule = None, id_log = None, id_robot="1", priority ="1", log_file_path = None, parameters=None)
        committee = process.get_committee(params['comite'])
        articles = self.get_articles('hercules-rpa/test/test-execution/data.txt')

        process.print_scientific_production(document, articles, committee, 'principal', 2.1)
        docname = process.save_report(document, researcherData.name, True)
        docA = aw.Document("hercules-rpa/test/process2/files/InformeSexeniosAntonioFernandoSkarmetaGomezBaremo.docx")
        docB = aw.Document(docname)
        # DocA now contains changes as revisions.
        docA.compare(docB, "user", datetime.datetime.today())
        #print("Documents are equal" if (docA.revisions.count == 0) else "Documents are not equal")
        self.assertEqual(docA.revisions.count, 0, msg="Documents are not equal")

    def test_authors_list(self):
        file = open("hercules-rpa/test/files/sexenios/article_with_authors.json", "r")
        response_text = file.read()
        file.close()
        json_dict = json.loads(response_text)
        df = pd.json_normalize(json_dict["results"]["bindings"])
        
        processSexenios = ProcessSexenios.ProcessSexenios(id_schedule = None, id_log = None, id_robot="1", priority ="1", log_file_path = None, parameters=None)
        results = processSexenios.get_authors_formatted(df)
        autoresString = 'Miguel Angel Zamora Izquierdo, Jose Santa, Juan Antonio Martinez Navarro, Juan Vicente Rodado Martinez, Antonio Fernando Skarmeta Gomez'
        self.assertEqual(results,autoresString)

    def test_committee_quimica(self): 
        """
        Test que evalúa los criterios del comité de quimica (2)
        """        
        process = ProcessSexenios.ProcessSexenios(id_schedule=None, id_log=None, id_robot="1", priority="1", log_file_path=None, parameters=None)
        articles = self.get_articles("hercules-rpa/test/files/accreditations/data.txt")
        committee = process.get_committee("2")
        evaluation:SexenioEvaluation = committee.get_evaluation_sexenio(articles)
        self.assertEqual(evaluation.punctuation, 32.5)
        self.assertEqual(len(evaluation.main_production),5)
        self.assertEqual(len(evaluation.get_substitute_production()),135)

    def test_committee_biologia_celular(self): 
        """
        Test que evalúa los criterios del comité de biologia celular (3)
        """        
        process = ProcessSexenios.ProcessSexenios(id_schedule=None, id_log=None, id_robot="1", priority="1", log_file_path=None, parameters=None)
        articles = self.get_articles("hercules-rpa/test/files/accreditations/data.txt")
        committee = process.get_committee("3")
        evaluation:SexenioEvaluation = committee.get_evaluation_sexenio(articles)
        self.assertEqual(evaluation.punctuation, 47)

    def test_committee_ciencias_biomedicas(self): 
        """
        Test que evalúa los criterios del comité de ciencias biomedicas (4)
        """        
        process = ProcessSexenios.ProcessSexenios(id_schedule=None, id_log=None, id_robot="1", priority="1", log_file_path=None, parameters=None)
        articles = self.get_articles("hercules-rpa/test/files/accreditations/data.txt")
        committee = process.get_committee("4")
        evaluation:SexenioEvaluation = committee.get_evaluation_sexenio(articles)
        self.assertEqual(evaluation.punctuation, 30.5)
        self.assertEqual(len(evaluation.main_production),5)
    
    def test_committee_ciencias_naturaleza(self): 
        """
        Test que evalúa los criterios del comité de ciencias de la naturaleza (5)
        """        
        process = ProcessSexenios.ProcessSexenios(id_schedule=None, id_log=None, id_robot="1", priority="1", log_file_path=None, parameters=None)
        articles = self.get_articles("hercules-rpa/test/files/accreditations/data.txt")
        committee = process.get_committee("5")
        evaluation:SexenioEvaluation = committee.get_evaluation_sexenio(articles)
        self.assertEqual(evaluation.punctuation, 54)
        self.assertEqual(len(evaluation.main_production),6)

    def test_committee_ciencias_naturaleza(self): 
        """
        Test que evalúa los criterios del comité de ciencias de la naturaleza (5)
        """        
        process = ProcessSexenios.ProcessSexenios(id_schedule=None, id_log=None, id_robot="1", priority="1", log_file_path=None, parameters=None)
        articles = self.get_articles("hercules-rpa/test/files/accreditations/data.txt")
        committee = process.get_committee("5")
        evaluation:SexenioEvaluation = committee.get_evaluation_sexenio(articles)
        self.assertEqual(evaluation.punctuation, 54)
        self.assertEqual(len(evaluation.main_production),6)

    def test_committee_Ingenierias(self): 
        """
        Test que evalúa los criterios del comité de ingenierías (7)
        """        
        process = ProcessSexenios.ProcessSexenios(id_schedule=None, id_log=None, id_robot="1", priority="1", log_file_path=None, parameters=None)
        articles = self.get_articles("hercules-rpa/test/files/accreditations/data.txt")
        committee = process.get_committee("7")
        evaluation:SexenioEvaluation = committee.get_evaluation_sexenio(articles)
        self.assertEqual(evaluation.punctuation, 30)
        self.assertEqual(len(evaluation.main_production),3)

    def test_committee_ArquitecturaIngenieriaCivilYUrbanismo_tecnology(self): 
        """
        Test que evalúa los criterios del comité de arquitectura, ingeniería civil y urbanismo con perfil tecnológico (8)
        """        
        process = ProcessSexenios.ProcessSexenios(id_schedule=None, id_log=None, id_robot="1", priority="1", log_file_path=None, parameters=None)
        articles = self.get_articles("hercules-rpa/test/files/accreditations/data.txt")
        committee = process.get_committee("8")
        committee.is_tecnology=True
        evaluation:SexenioEvaluation = committee.get_evaluation_sexenio(articles)
        self.assertEqual(evaluation.punctuation, 0)

    def test_committee_ArquitecturaIngenieriaCivilYUrbanismo_nottecnology(self): 
        """
        Test que evalúa los criterios del comité de arquitectura, ingeniería civil y urbanismo sin perfil tecnológico (8)
        """        
        process = ProcessSexenios.ProcessSexenios(id_schedule=None, id_log=None, id_robot="1", priority="1", log_file_path=None, parameters=None)
        articles = self.get_articles("hercules-rpa/test/files/accreditations/data.txt")
        committee = process.get_committee("8")
        evaluation:SexenioEvaluation = committee.get_evaluation_sexenio(articles)
        self.assertEqual(evaluation.punctuation, 0)

    def test_committee_CienciasEducacion(self): 
        """
        Test que evalúa los criterios del comité de ciencias de la educación (10)
        """        
        process = ProcessSexenios.ProcessSexenios(id_schedule=None, id_log=None, id_robot="1", priority="1", log_file_path=None, parameters=None)
        articles = self.get_articles("hercules-rpa/test/files/accreditations/data.txt")
        committee = process.get_committee("10")
        evaluation:SexenioEvaluation = committee.get_evaluation_sexenio(articles)
        self.assertEqual(evaluation.punctuation, 14)
        self.assertEqual(len(evaluation.main_production),2)

    def test_committee_CienciasEconomicasYEmpresariales(self): 
        """
        Test que evalúa los criterios del comité de Ciencias Economicas Y Empresariales (11)
        """        
        process = ProcessSexenios.ProcessSexenios(id_schedule=None, id_log=None, id_robot="1", priority="1", log_file_path=None, parameters=None)
        articles = self.get_articles("hercules-rpa/test/files/accreditations/data.txt")
        committee = process.get_committee("11")
        evaluation:SexenioEvaluation = committee.get_evaluation_sexenio(articles)
        self.assertEqual(evaluation.punctuation, 40)
        self.assertEqual(len(evaluation.main_production),5)

    def test_committee_Filologia_Linguistica(self): 
        """
        Test que evalúa los criterios del comité de filología y lingüistica (14)
        """        
        process = ProcessSexenios.ProcessSexenios(id_schedule=None, id_log=None, id_robot="1", priority="1", log_file_path=None, parameters=None)
        articles = self.get_articles("hercules-rpa/test/files/accreditations/data.txt")
        committee = process.get_committee("14")
        evaluation:SexenioEvaluation = committee.get_evaluation_sexenio(articles)
        self.assertEqual(evaluation.punctuation, 40)
        self.assertEqual(len(evaluation.main_production),5)

    def test_committee_cienciasSociales(self): 
        """
        Test que evalúa los criterios del comité de ciencias sociales (9)
        """        
        params = {}
        params['subcomite'] = '1'
        process = ProcessSexenios.ProcessSexenios(id_schedule=None, id_log=None, id_robot="1", priority="1", log_file_path=None, parameters=params)
        articles = self.get_articles("hercules-rpa/test/files/accreditations/data.txt")
        committee = process.get_committee("9")
        evaluation:SexenioEvaluation = committee.get_evaluation_sexenio(articles)
        self.assertEqual(evaluation.punctuation, 50)
        self.assertEqual(len(evaluation.main_production),5)

    def test_committee_cienciasComportamiento_Otros(self): 
        """
        Test que evalúa los criterios del comité de ciencias de comportamiento y del comité Otros (9)
        """        
        params = {}
        params['subcomite'] = '2'
        process = ProcessSexenios.ProcessSexenios(id_schedule=None, id_log=None, id_robot="1", priority="1", log_file_path=None, parameters=params)
        articles = self.get_articles("hercules-rpa/test/files/accreditations/data.txt")
        committee = process.get_committee("9")
        evaluation:SexenioEvaluation = committee.get_evaluation_sexenio(articles)
        self.assertEqual(evaluation.punctuation, 0)

    def test_committee_BiblioteconomiaYDocumentacion(self): 
        """
        Test que evalúa los criterios del comité de Biblioteconomia Y Documentación (9)
        """        
        params = {}
        params['subcomite'] = '3'
        process = ProcessSexenios.ProcessSexenios(id_schedule=None, id_log=None, id_robot="1", priority="1", log_file_path=None, parameters=params)
        articles = self.get_articles("hercules-rpa/test/files/accreditations/data.txt")
        committee = process.get_committee("9")
        evaluation:SexenioEvaluation = committee.get_evaluation_sexenio(articles)
        self.assertEqual(evaluation.punctuation, 0)

    def test_committee_EstudiosGenero(self): 
        """
        Test que evalúa los criterios del comité de estudios de género (9)
        """        
        params = {}
        params['subcomite'] = '4'
        process = ProcessSexenios.ProcessSexenios(id_schedule=None, id_log=None, id_robot="1", priority="1", log_file_path=None, parameters=params)
        articles = self.get_articles("hercules-rpa/test/files/accreditations/data.txt")
        committee = process.get_committee("9")
        evaluation:SexenioEvaluation = committee.get_evaluation_sexenio(articles)
        self.assertEqual(evaluation.punctuation, 0)

    def test_committee_AntropologiaSocial(self): 
        """
        Test que evalúa los criterios del comité de Antropología Social (9)
        """        
        params = {}
        params['subcomite'] = '5'
        process = ProcessSexenios.ProcessSexenios(id_schedule=None, id_log=None, id_robot="1", priority="1", log_file_path=None, parameters=params)
        articles = self.get_articles("hercules-rpa/test/files/accreditations/data.txt")
        committee = process.get_committee("9")
        evaluation:SexenioEvaluation = committee.get_evaluation_sexenio(articles)
        self.assertEqual(evaluation.punctuation, 50)
        self.assertEqual(len(evaluation.main_production), 5)       


if __name__ == '__main__':
    unittest.main()