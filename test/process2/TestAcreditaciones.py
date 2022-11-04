import json
import sys
import os
import pandas as pd
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(os.path.dirname(currentdir))
sys.path.insert(1, parentdir)
print(currentdir, parentdir)
import unittest
from model.process.ProcessAcreditaciones import ProcessAcreditaciones
from model.process.Process2.Entities.RO import RO
from model.process.Process2.Entities.Evaluations.AccreditationEvaluationBiologCelularMolecular import AccreditationEvaluationBiologCelularMolecular
from model.process.Process2.Entities.Evaluations.AccreditationEvaluationFisica import AccreditationEvaluationFisica
from model.process.Process2.Entities.Evaluations.AccreditationEvaluationQuimica import AccreditationEvaluationQuimica
from model.process.Process2.Entities.Evaluations.AccreditationEvaluationCienciasNaturaleza import AccreditationEvaluationCienciasNaturaleza
from model.process.Process2.Entities.Evaluations.AccreditationEvaluationMedicinaClinicaYEspecialidades import AccreditationEvaluationMedicinaClinicaYEspecialidades
from model.process.Process2.Entities.Evaluations.AccreditationEvaluationOtrasEspecialidadesSanitarias import AccreditationEvaluationOtrasEspecialidadesSanitarias
from model.process.Process2.Entities.Evaluations.AccreditationEvaluationCienciasComportamiento import AccreditationEvaluationCienciasComportamiento
from model.process.Process2.Entities.Evaluations.AccreditationEvaluationCienciasSociales import AccreditationEvaluationCienciasSociales
from model.process.Process2.Entities.Evaluations.AccreditationEvaluationCienciasEconomicasYEmpresariales import AccreditationEvaluationCienciasEconomicasYEmpresariales
from model.process.Process2.Entities.Evaluations.AccreditationEvaluationFilologiaLinguistica import AccreditationEvaluationFilologiaLinguistica
from model.process.Process2.Entities.Accreditation import AccreditationCategory

class TestAcreditaciones(unittest.TestCase):

    def get_articles(self, filename) -> list:
        file = open(filename, "r")
        text = file.read()
        file.close()
        arts_json = json.loads(text)
        articles = []
        for element in arts_json['bindings']:
            df = pd.json_normalize(element)
            aux = df.iloc[0]
            article = RO(title=aux["titulo.value"], publication_type=aux["tipoProduccion.value"],
            publication_date= aux["fechaPublicacion.value"], wos_cites=aux["citasWos.value"],
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
    
    def test_accreditation_commission2_titularidad(self):
        """
        Test que evalúa los criterios de la comisión de Física (2)
        """
        process = ProcessAcreditaciones(id_schedule=None, id_log=None, id_robot="1", priority="1", log_file_path=None, parameters=None)
        articles = self.get_articles("hercules-rpa/test/files/accreditations/data.txt")
        accreditation = process.get_accreditation("1")
        commission = process.get_commission("2")

        evaluation:AccreditationEvaluationFisica = commission.get_accreditation_evaluation(articles, accreditation)
        self.assertTrue(evaluation.positive)
        self.assertIs(len(evaluation.scientific_production),135)
        self.assertIs(len(evaluation.arts_t1),97)
        self.assertIs(len(evaluation.arts_t2), 0)
        self.assertIs(len(evaluation.get_publications_t1()),14)
        self.assertIs(len(evaluation.get_publications_t1_t2()),22)
        self.assertIs(len(evaluation.get_substitute_production()),113)

    def test_accreditation_commission2_catedra(self):
        """
        Test que evalúa los criterios de la comisión de Física (2)
        """
        process = ProcessAcreditaciones(id_schedule=None, id_log=None, id_robot="1", priority="1", log_file_path=None, parameters=None)
        articles = self.get_articles("hercules-rpa/test/files/accreditations/data.txt")
        accreditation = process.get_accreditation("2")
        commission = process.get_commission("2")

        evaluation:AccreditationEvaluationFisica = commission.get_accreditation_evaluation(articles, accreditation)
        self.assertTrue(evaluation.positive)
        self.assertIs(len(evaluation.scientific_production),135)
        self.assertIs(len(evaluation.arts_t1),97)
        self.assertIs(len(evaluation.arts_t2), 0)
        self.assertIs(len(evaluation.get_publications_t1()),30)
        self.assertIs(len(evaluation.get_publications_t1_t2()),30)
        self.assertIs(len(evaluation.get_substitute_production()),105)

    def test_accreditation_commission3_titularidad(self):
        """
        Test que evalúa los criterios de la comisión de Química (3)
        """
        process = ProcessAcreditaciones(id_schedule=None, id_log=None, id_robot="1", priority="1", log_file_path=None, parameters=None)
        articles = self.get_articles("hercules-rpa/test/files/accreditations/data.txt")
        accreditation = process.get_accreditation("1")
        commission = process.get_commission("3")

        evaluation:AccreditationEvaluationQuimica = commission.get_accreditation_evaluation(articles, accreditation)
        self.assertTrue(evaluation.positive)
        self.assertIs(len(evaluation.scientific_production),135)
        self.assertIs(len(evaluation.art_t1),91)
        self.assertIs(len(evaluation.get_publications_t1()),15)
        self.assertIs(len(evaluation.art_first_author), 91)
        self.assertIs(len(evaluation.get_publications_first_author()), 4)
        self.assertIs(len(evaluation.get_substitute_production()),44)  
            
    def test_accreditation_commission3_catedra(self):
        """
        Test que evalúa los criterios de la comisión de Química (3)
        """
        process = ProcessAcreditaciones(id_schedule=None, id_log=None, id_robot="1", priority="1", log_file_path=None, parameters=None)
        articles = self.get_articles("hercules-rpa/test/files/accreditations/data.txt")
        accreditation = process.get_accreditation("2")
        commission = process.get_commission("3")

        evaluation:AccreditationEvaluationQuimica = commission.get_accreditation_evaluation(articles, accreditation)
        self.assertTrue(evaluation.positive)
        self.assertIs(len(evaluation.scientific_production),135)
        self.assertIs(len(evaluation.art_t1),97)
        self.assertIs(len(evaluation.get_publications_t1()),25)
        self.assertIs(len(evaluation.art_first_author), 97)
        self.assertIs(len(evaluation.get_publications_first_author()), 4)
        self.assertIs(len(evaluation.get_substitute_production()),38)  

    def test_accreditation_commission4_titularidad(self):
        """
        Test que evalúa los criterios de la comisión de Ciencias de la Naturaleza (4)
        """
        process = ProcessAcreditaciones(id_schedule=None, id_log=None, id_robot="1", priority="1", log_file_path=None, parameters=None)
        articles = self.get_articles("hercules-rpa/test/files/accreditations/data.txt")
        accreditation = process.get_accreditation("1")
        commission = process.get_commission("4")

        evaluation:AccreditationEvaluationCienciasNaturaleza = commission.get_accreditation_evaluation(articles, accreditation)
        self.assertTrue(evaluation.positive)
        self.assertIs(len(evaluation.scientific_production),135)
        self.assertIs(len(evaluation.publications_t1),16)
        self.assertIs(len(evaluation.get_publications_t1()),5)
        self.assertIs(len(evaluation.publications_t2),8)
        self.assertIs(len(evaluation.get_publications_t2()),5)
        self.assertIs(len(evaluation.publications_author),24)
        self.assertIs(len(evaluation.get_publications_author()),4)
        self.assertIs(len(evaluation.get_substitute_production()),125)  

    def test_accreditation_commission4_catedra(self):
        """
        Test que evalúa los criterios de la comisión de Ciencias de la Naturaleza (4)
        """
        process = ProcessAcreditaciones(id_schedule=None, id_log=None, id_robot="1", priority="1", log_file_path=None, parameters=None)
        articles = self.get_articles("hercules-rpa/test/files/accreditations/data.txt")
        accreditation = process.get_accreditation("2")
        commission = process.get_commission("4")

        evaluation:AccreditationEvaluationCienciasNaturaleza = commission.get_accreditation_evaluation(articles, accreditation)
        self.assertTrue(evaluation.positive)
        self.assertIs(len(evaluation.scientific_production),135)
        self.assertIs(len(evaluation.publications_t1),16)
        self.assertIs(len(evaluation.get_publications_t1()),10)
        self.assertIs(len(evaluation.publications_t2),8)
        self.assertIs(len(evaluation.get_publications_t2()),8)
        self.assertIs(len(evaluation.publications_author),24)
        self.assertIs(len(evaluation.get_publications_author()),10)
        self.assertIs(len(evaluation.get_substitute_production()),117)  

    def test_accreditation_commission5_titularidad(self): 
        """
        Test que evalúa los criterios de la comisión de biología celular y molecular (5)
        """
        
        process = ProcessAcreditaciones(id_schedule=None, id_log=None, id_robot="1", priority="1", log_file_path=None, parameters=None)
        articles = self.get_articles("hercules-rpa/test/files/accreditations/data.txt")
        accreditation = process.get_accreditation("1")
        commission = process.get_commission("5")

        evaluation:AccreditationEvaluationBiologCelularMolecular = commission.get_accreditation_evaluation(articles, accreditation)
        self.assertTrue(evaluation.positive)
        self.assertIs(evaluation.assessment, 'B')
        self.assertIs(len(evaluation.scientific_production),135)
        self.assertIs(len(evaluation.publications_authorship),5)
        self.assertIs(len(evaluation.get_publications_authorship()), 5)
        self.assertIs(len(evaluation.publications_t1),97)
        self.assertIs(len(evaluation.get_publications_t1()),10)
        self.assertIs(len(evaluation.get_substitute_production()),125)
    
    def test_accreditation_commission5_catedra(self): 
        """
        Test que evalúa los criterios de la comisión de biología celular y molecular (5)
        """
        
        process = ProcessAcreditaciones(id_schedule=None, id_log=None, id_robot="1", priority="1", log_file_path=None, parameters=None)
        articles = self.get_articles("hercules-rpa/test/files/accreditations/data.txt")
        accreditation = process.get_accreditation("2")
        commission = process.get_commission("5")

        evaluation:AccreditationEvaluationBiologCelularMolecular = commission.get_accreditation_evaluation(articles, accreditation)
        self.assertTrue(evaluation.positive)
        self.assertIs(len(evaluation.scientific_production),135)
        self.assertIs(len(evaluation.publications_authorship),10)
        self.assertIs(len(evaluation.get_publications_authorship()), 10)
        self.assertIs(len(evaluation.publications_t1),97)
        self.assertIs(len(evaluation.get_publications_t1()),20)
        self.assertIs(len(evaluation.get_substitute_production()),114)       
    
    def test_accreditation_commission7_titularidad(self): 
        """
        Test que evalúa los criterios de la commission de medicina clinica y especialidades clinicas (7)
        """

        process = ProcessAcreditaciones(id_schedule=None, id_log=None, id_robot="1", priority="1", log_file_path=None, parameters=None)
        articles = self.get_articles("hercules-rpa/test/files/accreditations/data.txt")
        accreditation = process.get_accreditation("1")
        commission = process.get_commission("7")

        evaluation:AccreditationEvaluationMedicinaClinicaYEspecialidades = commission.get_accreditation_evaluation(articles, accreditation)
        self.assertTrue(evaluation.positive)
        self.assertIs(len(evaluation.scientific_production),135)
        self.assertIs(len(evaluation.arts_authorship), 8)
        self.assertIs(len(evaluation.arts_t1), 97)

    def test_accreditation_commission7_catedra(self): 
        """
        Test que evalúa los criterios de la commission de medicina clinica y especialidades clinicas (7)
        """

        process = ProcessAcreditaciones(id_schedule=None, id_log=None, id_robot="1", priority="1", log_file_path=None, parameters=None)
        articles = self.get_articles("hercules-rpa/test/files/accreditations/data.txt")
        accreditation = process.get_accreditation("2")
        commission = process.get_commission("7")

        evaluation:AccreditationEvaluationMedicinaClinicaYEspecialidades = commission.get_accreditation_evaluation(articles, accreditation)
        self.assertTrue(evaluation.positive)
        self.assertIs(len(evaluation.scientific_production),135)
        self.assertIs(len(evaluation.arts_authorship), 15)
        self.assertIs(len(evaluation.arts_t1), 97)
    
    def test_accreditation_commission8_titularidad(self): 
        """
        Test que evalúa los criterios de la comisión de otras especialidades sanitarias (8)
        """
        process = ProcessAcreditaciones(id_schedule=None, id_log=None, id_robot="1", priority="1", log_file_path=None, parameters=None)
        articles = self.get_articles("hercules-rpa/test/files/accreditations/data.txt")
        accreditation = process.get_accreditation("1")
        commission = process.get_commission("8")

        evaluation:AccreditationEvaluationOtrasEspecialidadesSanitarias = commission.get_accreditation_evaluation(articles, accreditation)
        self.assertTrue(evaluation.positive)
        self.assertIs(len(evaluation.scientific_production),135)
        self.assertIs(len(evaluation.articles_authorship), 7)
      
    def test_accreditation_commission8_catedra(self):  
        """
        Test que evalúa los criterios de la comisión de otras especialidades sanitarias (8)
        """

        process = ProcessAcreditaciones(id_schedule=None, id_log=None, id_robot="1", priority="1", log_file_path=None, parameters=None)
        articles = self.get_articles("hercules-rpa/test/files/accreditations/data.txt")
        accreditation = process.get_accreditation("2")
        commission = process.get_commission("8")

        evaluation:AccreditationEvaluationOtrasEspecialidadesSanitarias = commission.get_accreditation_evaluation(articles, accreditation)
        self.assertTrue(evaluation.positive)
        self.assertIs(len(evaluation.scientific_production),135)
        self.assertIs(len(evaluation.articles_authorship), 16)

    def test_accreditation_commission15_16_titularidad(self): 
        """
        Test que evalúa los criterios de la comisión de Ciencias Económicas y Empresariales (15-16)
        """
        process = ProcessAcreditaciones(id_schedule=None, id_log=None, id_robot="1", priority="1", log_file_path=None, parameters=None)
        articles = self.get_articles("hercules-rpa/test/files/accreditations/data.txt")
        accreditation = process.get_accreditation("1")
        commission = process.get_commission("15")

        evaluation:AccreditationEvaluationCienciasEconomicasYEmpresariales = commission.get_accreditation_evaluation(articles, accreditation)
        self.assertTrue(evaluation.positive)
        self.assertIs(len(evaluation.scientific_production),135)
        self.assertIs(len(evaluation.art_Q1_Q2), 120)
        self.assertIs(len(evaluation.get_publications_Q1_Q2()), 4)
        self.assertIs(len(evaluation.art_Q3_Q4), 15)
        self.assertIs(len(evaluation.get_publications_Q3_Q4()), 2)
        self.assertIs(len(evaluation.art_Q1_Q2), 120)
        self.assertIs(len(evaluation.get_publications_Q1_Q2()), 4)


    def test_accreditation_commission15_16_catedra(self): 
        """
        Test que evalúa los criterios de la comisión de Ciencias Económicas y Empresariales (15-16)
        """
        process = ProcessAcreditaciones(id_schedule=None, id_log=None, id_robot="1", priority="1", log_file_path=None, parameters=None)
        articles = self.get_articles("hercules-rpa/test/files/accreditations/data.txt")
        accreditation = process.get_accreditation("2")
        commission = process.get_commission("15")

        evaluation:AccreditationEvaluationCienciasEconomicasYEmpresariales = commission.get_accreditation_evaluation(articles, accreditation)
        self.assertTrue(evaluation.positive)
        self.assertIs(len(evaluation.scientific_production),135)
        self.assertIs(len(evaluation.art_Q1_Q2), 120)
        self.assertIs(len(evaluation.get_publications_Q1_Q2()), 8)
        self.assertIs(len(evaluation.art_Q3_Q4), 15)
        self.assertIs(len(evaluation.get_publications_Q3_Q4()), 4)
        self.assertIs(len(evaluation.art_Q1_Q2), 120)
        self.assertIs(len(evaluation.get_publications_Q1_Q2()), 8)

    def test_accreditation_commission18_titularidad(self):
        """
        Test que evalúa los criterios de la comisión de Ciencias del Comportamiento (18)
        """
        process = ProcessAcreditaciones(id_schedule=None, id_log=None, id_robot="1", priority="1", log_file_path=None, parameters=None)
        articles = self.get_articles("hercules-rpa/test/files/accreditations/data.txt")
        accreditation = process.get_accreditation("1")
        commission = process.get_commission("18")

        evaluation:AccreditationEvaluationCienciasComportamiento = commission.get_accreditation_evaluation(articles, accreditation)
        self.assertTrue(evaluation.positive)
        self.assertIs(len(evaluation.scientific_production),135)
        self.assertIs(len(evaluation.publications_t1_t2),127)
        self.assertIs(len(evaluation.get_publications_t1_t2()),5)
        self.assertIs(len(evaluation.publications_authorship),8)
        self.assertIs(len(evaluation.get_publications_authorship()),8)
        self.assertIs(len(evaluation.get_substitute_production()),122)  

    def test_accreditation_commission18_catedra(self):
        """
        Test que evalúa los criterios de la comisión de Ciencias del Comportamiento (18)
        """
        process = ProcessAcreditaciones(id_schedule=None, id_log=None, id_robot="1", priority="1", log_file_path=None, parameters=None)
        articles = self.get_articles("hercules-rpa/test/files/accreditations/data.txt")
        accreditation = process.get_accreditation("2")
        commission = process.get_commission("18")

        evaluation:AccreditationEvaluationCienciasComportamiento = commission.get_accreditation_evaluation(articles, accreditation)
        self.assertTrue(evaluation.positive)
        self.assertIs(len(evaluation.scientific_production),135)
        self.assertIs(len(evaluation.publications_t1_t2),127)
        self.assertIs(len(evaluation.get_publications_t1_t2()),8)
        self.assertIs(len(evaluation.publications_authorship),8)
        self.assertIs(len(evaluation.get_publications_authorship()),8)
        self.assertIs(len(evaluation.get_substitute_production()),119) 

    def test_accreditation_commission19_titularidad(self):
        """
        Test que evalúa los criterios de la comisión de Ciencias Sociales (19)
        """
        process = ProcessAcreditaciones(id_schedule=None, id_log=None, id_robot="1", priority="1", log_file_path=None, parameters=None)
        articles = self.get_articles("hercules-rpa/test/files/accreditations/data.txt")
        accreditation = process.get_accreditation("1")
        commission = process.get_commission("19")

        evaluation:AccreditationEvaluationCienciasSociales = commission.get_accreditation_evaluation(articles, accreditation)
        self.assertTrue(evaluation.positive)
        self.assertIs(len(evaluation.scientific_production),135)
        self.assertIs(len(evaluation.publications_n1),97)
        self.assertIs(len(evaluation.publications_n2),30)
        self.assertIs(len(evaluation.get_publications_n1_n2()),8)
        self.assertIs(len(evaluation.get_substitute_production()),127)  

    def test_accreditation_commission19_catedra(self):
        """
        Test que evalúa los criterios de la comisión de Ciencias de Sociales (19)
        """
        process = ProcessAcreditaciones(id_schedule=None, id_log=None, id_robot="1", priority="1", log_file_path=None, parameters=None)
        articles = self.get_articles("hercules-rpa/test/files/accreditations/data.txt")
        accreditation = process.get_accreditation("2")
        commission = process.get_commission("19")

        evaluation:AccreditationEvaluationCienciasSociales = commission.get_accreditation_evaluation(articles, accreditation)
        self.assertTrue(evaluation.positive)
        self.assertIs(len(evaluation.scientific_production),135)
        self.assertIs(len(evaluation.publications_n1),97)
        self.assertIs(len(evaluation.publications_n2),30)
        self.assertIs(len(evaluation.get_publications_n1_n2()),16)
        self.assertIs(len(evaluation.get_substitute_production()),119) 

    def test_accreditation_commission21_titularidad(self):
        """
        Test que evalúa los criterios de la comisión de Filología y Lingüistica (21)
        """
        process = ProcessAcreditaciones(id_schedule=None, id_log=None, id_robot="1", priority="1", log_file_path=None, parameters=None)
        articles = self.get_articles("hercules-rpa/test/files/accreditations/data.txt")
        accreditation = process.get_accreditation("1", AccreditationCategory.INVESTIGACION)
        commission = process.get_commission("21")

        evaluation:AccreditationEvaluationFilologiaLinguistica = commission.get_accreditation_evaluation(articles, accreditation)
        self.assertTrue(evaluation.positive)
        self.assertIs(len(evaluation.scientific_production),135)
        self.assertIs(len(evaluation.publications_n1),97)
        self.assertIs(len(evaluation.get_publications_n1()),6)
        self.assertIs(len(evaluation.get_substitute_production()),129)  

    def test_accreditation_commission21_catedra(self):
        """
        Test que evalúa los criterios de la comisión de Filología y Lingüistica (21)
        """
        process = ProcessAcreditaciones(id_schedule=None, id_log=None, id_robot="1", priority="1", log_file_path=None, parameters=None)
        articles = self.get_articles("hercules-rpa/test/files/accreditations/data.txt")
        accreditation = process.get_accreditation("2",AccreditationCategory.INVESTIGACION)
        commission = process.get_commission("21")

        evaluation:AccreditationEvaluationFilologiaLinguistica = commission.get_accreditation_evaluation(articles, accreditation)
        self.assertTrue(evaluation.positive)
        self.assertIs(len(evaluation.scientific_production),135)
        self.assertIs(len(evaluation.publications_n1),97)
        self.assertIs(len(evaluation.get_publications_n1()),12)
        self.assertIs(len(evaluation.get_substitute_production()),123) 

if __name__ == '__main__':
    unittest.main()