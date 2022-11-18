import sys
import os

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(os.path.dirname(currentdir))
sys.path.insert(1, parentdir)
print(currentdir, parentdir)
import unittest
from model.process.Process3.GrantsEuropeExtractor import GrantsEuropeExtractor
from model.process.Process3.BDNS import BDNS


class TestExtractCalls(unittest.TestCase):

    # Pruebas realizadas a través de la convocatoria resuelta: https://www.infosubvenciones.es/bdnstrans/GE/es/convocatoria/525644

    def test_extract_call_info(self):
        bdns = BDNS("","")
        result = bdns.obtain_data_bdns_file("hercules-rpa/test/files/525644.html")
        self.assertEqual(result["Órgano convocante"], "ESTADO") 
        self.assertEqual(result["Sede electrónica para la presentación de solicitudes"], "https://ciencia.sede.gob.es") 
        self.assertEqual(result["Código BDNS"], "525644") 
        self.assertEqual(result["Mecanismo de Recuperación y Resiliencia"], "NO") 
        self.assertEqual(result["Fecha de registro"], "28/09/2020") 
        self.assertEqual(result["Instrumento de ayuda"], "SUBVENCIÓN Y ENTREGA DINERARIA SIN CONTRAPRESTACIÓN ") 
        self.assertEqual(result["Tipo de convocatoria"], "Concurrencia competitiva - canónica") 
        #self.assertEqual(result["Presupuesto total de la convocatoria"], "108,954,960.00 €") 
        #self.assertEqual(result["Título de la convocatoria en español"], "Resolución de 30 de septiembre de 2020, de la Presidencia de la Agencia Estatal de Investigación, por la que se aprueba la convocatoria 2020 de ayudas para contratos predoctorales en el marco del Plan Estatal de I+D+i 2017-2020..") 
        self.assertEqual(result["Título de la convocatoria en otra lengua cooficial"], ".") 
        self.assertEqual(result["Tipo de beneficiario elegible"], "PERSONAS JURÍDICAS QUE NO DESARROLLAN ACTIVIDAD ECONÓMICA") 
        self.assertEqual(result["Sector económico del beneficiario"], "ACTIVIDADES PROFESIONALES, CIENTÍFICAS Y TÉCNICAS") 
        self.assertEqual(result["Región de impacto"], "ES - ESPAÑA ") 
        self.assertEqual(result["Finalidad (política de gasto)"], "INVESTIGACIÓN, DESARROLLO E INNOVACIÓN") 
        #self.assertEqual(result["Título de las Bases reguladoras"], "Orden CNU/692/2019, de 20 de junio, por la que se aprueban las bases reguladoras para la concesión de ayudas en el marco del Programa de Promoción del Talento y su Empleabilidad en I+D+i del Plan Estatal de I+D+i 2017-2020")
        self.assertEqual(result["Dirección electrónica de las bases reguladoras"], "https://www.boe.es/diario_boe/txt.php?id=BOE-A-2019-9533")
        self.assertEqual(result["¿El extracto de la convocatoria se publica en diario oficial?"], "Sí") 
        self.assertEqual(result["¿Se puede solicitar indefinidamente?"], "No") 
        self.assertEqual(result["Fecha de inicio del periodo de solicitud"], "13/10/2020") 
        self.assertEqual(result["Fecha de finalización del periodo de solicitud"], "27/10/2020") 
        self.assertEqual(result["SA Number (Referencia de ayuda de estado)"], "") 
        self.assertEqual(result["Cofinanciado con Fondos UE"], "FSE - FONDO SOCIAL EUROPEO ") 
        self.assertEqual(result["Reglamento (UE)"], "") 
        self.assertEqual(result["Sector de productos"], "")
    
    def test_extract_call_word_investigacion(self):
        bdns = BDNS("","")
        response = bdns.search_name_csv_file("hercules-rpa/test/files/convocatorias.csv", ["investigación"])
        self.assertEqual(response, True)

    def test_extract_call_word_ayuda(self):
        bdns = BDNS("","")
        response = bdns.search_name_csv_file("hercules-rpa/test/files/convocatorias.csv", ["ayuda"])
        self.assertEqual(response, True)

    def test_extract_call_word_desarrollo(self):
        bdns = BDNS("","")
        response = bdns.search_name_csv_file("hercules-rpa/test/files/convocatorias.csv", ["desarrollo"])
        self.assertEqual(response, True)

    def test_extract_call_without_word(self):
        bdns = BDNS("","")
        response = bdns.search_name_csv_file("hercules-rpa/test/files/convocatorias.csv", ["hola", "caracola"])
        self.assertEqual(response, False)

    def test_extract_call_without_number(self):
        bdns = BDNS("","")
        response = bdns.search_numbdns_csv("hercules-rpa/test/files/convocatorias.csv","525644")
        self.assertEqual(response,"")

    def test_extract_call_with_number(self):
        bdns = BDNS("","")
        response = bdns.search_numbdns_csv("hercules-rpa/test/files/convocatorias.csv","606845")
        self.assertEqual(response[0],"606845")

    def test_extract_call_number(self):
        bdns = BDNS("","")
        response = bdns.search_numbdns_csv("hercules-rpa/test/files/convocatorias.csv","607221")
        self.assertEqual(response[0],"607221")
    
    def test_extract_call_no_number(self):
        bdns = BDNS("","")
        response = bdns.search_numbdns_csv("hercules-rpa/test/files/convocatorias.csv","525655")
        self.assertEqual(response,"")

    def test_extract_call_europa_dates_day(self):
        europa = GrantsEuropeExtractor("","")
        response = europa.search_europe_date_file("hercules-rpa/test/files/grantsTenders.json", "2022-03-01", "2022-03-02")
        self.assertEqual(len(response),44)
        self.assertEqual(response[0]['titulo'],"CREA-CROSS-2022-INNOVLAB")
        self.assertEqual(response[1]['titulo'],"CREA-CULT-2022-LIT")

    def test_extract_call_europa_dates_week(self):
        europa = GrantsEuropeExtractor("","")
        response = europa.search_europe_date_file("hercules-rpa/test/files/grantsTenders.json", "2022-04-01", "2022-04-07")
        self.assertEqual(len(response),11)
        self.assertEqual(response[0]['titulo'],"CREA-MEDIA-2022-CINNET")
        self.assertEqual(response[1]['titulo'],"DIGITAL-EUROHPC-JU-2022-NCC-01-01")

    def test_extract_call_europa_dates_half_month(self):
        europa = GrantsEuropeExtractor("","")
        response = europa.search_europe_date_file("hercules-rpa/test/files/grantsTenders.json", "2022-05-15", "2022-05-31")
        self.assertEqual(len(response),38)
        self.assertEqual(response[0]['titulo'],"BMVI-2021-TF1-AG-NQAM")
        self.assertEqual(response[1]['titulo'],"CEF-E-2022-PCI-STUDIES")

    def test_extract_call_europa_dates_month(self):
        europa = GrantsEuropeExtractor("","")
        response = europa.search_europe_date_file("hercules-rpa/test/files/grantsTenders.json", "2022-01-01", "2022-01-31")
        self.assertEqual(len(response),2)
        self.assertEqual(response[0]['titulo'],"ISF-2022-TF1-AG-COP")
        self.assertEqual(response[1]['titulo'],"ISF-2022-TF1-AG-COP-TR")

    def test_extract_call_europa_dates_six_month(self):
        europa = GrantsEuropeExtractor("","")
        response = europa.search_europe_date_file("hercules-rpa/test/files/grantsTenders.json", "2022-01-01", "2022-06-30")
        self.assertEqual(len(response),312)
        self.assertEqual(response[0]['titulo'],"AMIF-2022-TF1-AG-INFO")
        self.assertEqual(response[7]['titulo'],"CREA-CROSS-2022-JOURPART")

    def test_extract_call_europa_incorrect_dates(self):
        europa = GrantsEuropeExtractor("","")
        response = europa.search_europe_date_file("hercules-rpa/test/files/grantsTenders.json", "2022-01-01", "2021-12-31")
        self.assertEqual(len(response),0)

    def test_extract_call_europa_none_dates(self):
        europa = GrantsEuropeExtractor("","")
        response = europa.search_europe_date_file("hercules-rpa/test/files/grantsTenders.json", None, None)
        self.assertEqual(len(response),0)

    def test_extract_call_pdf_525644(self):
        bdns = BDNS("","")
        JSON = {"rows":[[458217,"2020-09-30","2020-10-05","Convocatoria ayudas contratos predoctorales 2020.pdf"],[549902,"2021-04-13","2021-04-13","resolucion ampliacion plazo concesion PRE2020.pdf"],[590421,"2021-06-29","2021-06-29","Resolucion_Concesion_PREDOC2020_firmada.pdf"],[592212,"2021-07-02","2021-07-02","PRE2020_RC_ModificacionRC_CambiosCentros_Firmada.pdf"],[634857,"2021-10-13","2021-10-13","PRE2020_SegundaRC_Art20_3_abc_Firmada.pdf"],[634859,"2021-10-13","2021-10-13","PRE2020_TerceraRC_Art20_4_Firmada.pdf"]],"page":1,"total":1,"records":6,"infs":True}
        result = bdns.obtain_resources_bdns_file(JSON)
        self.assertEqual(len(result), 6)
        self.assertEqual(result[0][3], "Convocatoria ayudas contratos predoctorales 2020.pdf")
        self.assertEqual(result[2][3], "Resolucion_Concesion_PREDOC2020_firmada.pdf")

    def test_extract_call_pdf_607221(self):
        bdns = BDNS("","")
        JSON = {"rows":[[679583,"2022-01-24","2022-01-24","RD 1101-2021 y modificación BOE.pdf"]],"page":1,"total":1,"records":1,"infs":True}
        result = bdns.obtain_resources_bdns_file(JSON)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][3], "RD 1101-2021 y modificación BOE.pdf")


    def test_extract_call_empty_pdf(self):
        bdns = BDNS("","")
        JSON = {"rows":[],"page":1,"total":1,"records":0,"infs":True}
        result = bdns.obtain_resources_bdns_file(JSON)
        self.assertEqual(len(result), 0)

    def test_extract_call_none_pdf(self):
        bdns = BDNS("","")
        JSON = {"rows":[],"page":1,"total":1,"records":0,"infs":True}
        result = bdns.obtain_resources_bdns_file(None)
        self.assertEqual(len(result), 0)

if __name__ == '__main__':
    print('testExtractCalls')

    unittest.main()