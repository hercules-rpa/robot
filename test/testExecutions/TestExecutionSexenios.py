import os
import sys
import unittest
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(os.path.dirname(currentdir))
sys.path.insert(1, parentdir)
print(currentdir, parentdir)
from model.process.ValidEvaluators import ValidEvaluators
from model.process.ProcessSexenios import ProcessSexenios
import model.process.ProcessAcreditaciones as ProcessAcreditaciones
from rpa_robot.ControllerSettings  import ControllerSettings

class TestExecutionSexenios(unittest.TestCase):
    #edma = EDMA.EDMA()

    def test_valid_evaluators(self) -> dict:
        """
        Método que obtiene del configurador de los comités los que están implementados.
        :param filename nombre del fichero de configuración
        :return diccionario con los comités implementados
        """
        result:dict = {}
        process = ProcessSexenios(id_schedule = None, id_log = None, id_robot = "1", priority = "1", log_file_path = None, parameters=None, ip_api="10.208.99.12", port_api="5000")
        cs = ControllerSettings()
        conf = ControllerSettings().get_globals_settings(process.ip_api, process.port_api)
        print(conf)

        SGI = cs.get_sgi(process.ip_api, process.port_api)
        if SGI and SGI.host:
            print(SGI.host)
            print(SGI.oauth_username)
            print(SGI.oauth_password)
            print(SGI.oauth_url)
            res = SGI.auth()

            print(res)

        conf = cs.get_database_configuration(process.ip_api, process.port_api)
        print(str(conf))
        
        #comite = process.get_committee("2")
        #print(comite)

    def _test(self):
        valid = ValidEvaluators()
        result = valid.get_valid_commissions()
        print(result)                    

    def _test_get_investigador(self):       
        params = {}
        params["comite"] = "7"
        params["periodo"] = "2016-2021"
        params["tipoId"] = 1
        params["investigador"] = "28710458"
        
        process = ProcessSexenios(id_schedule = None, id_log = None, id_robot = "1", priority = "1", log_file_path = None, parameters=params)
        infoInvestigador = process.get_researcher_info(process.parameters)
        self.assertEqual("28710458", infoInvestigador[1])

        params["tipoId"] = 2
        params["investigador"] = "jtpalma@um.es"
        infoInvestigador = process.get_researcher_info(process.parameters)
        self.assertEqual("jtpalma@um.es", infoInvestigador[1])
        datosInvestigador = self.edma.get_researcher_data(infoInvestigador)
        self.assertEqual(datosInvestigador.email, 'jtpalma@um.es')
        self.assertEqual(datosInvestigador.name, 'Jose Tomas Palma Mendez')

        params["tipoId"] = 2
        params["investigador"] = "fernan@um.es"
        infoInvestigador = process.get_researcher_info(process.parameters)
        self.assertEqual("fernan@um.es", infoInvestigador[1])
        datosInvestigador = self.edma.get_researcher_data(infoInvestigador)
        self.assertEqual(datosInvestigador.email, 'fernan@um.es')

        params["tipoId"] = 2
        params["investigador"] = "manuelcampos@um.es"
        infoInvestigador = process.get_researcher_info(process.parameters)
        self.assertEqual("manuelcampos@um.es", infoInvestigador[1])
        datosInvestigador = self.edma.get_researcher_data(infoInvestigador)
        self.assertEqual(datosInvestigador.email, 'manuelcampos@um.es')

        params["tipoId"] = 2
        params["investigador"] = "jmjuarez@um.es"
        infoInvestigador = process.get_researcher_info(process.parameters)
        self.assertEqual("jmjuarez@um.es", infoInvestigador[1])
        datosInvestigador = self.edma.get_researcher_data(infoInvestigador)
        self.assertEqual(datosInvestigador.email, "jmjuarez@um.es")

    def _test_execute_sexenios(self):
        params = {}
        params["comite"] = "9"     
        params["subcomite"] = "1"   
        params["periodo"] = "2015-2020"
        params["tipoId"] = 3
        params["investigador"] = "0000-0001-5844-4163" #barrionuevo
        process = ProcessSexenios(id_schedule = None, id_log = None, id_robot = "1", priority = "1", log_file_path = None, parameters=params)
        process.execute()

        params["comite"] = "9"     
        params["subcomite"] = "2"         
        process.execute()

        params["comite"] = "9"     
        params["subcomite"] = "3"  
        process.execute()

        params["comite"] = "9"     
        params["subcomite"] = "4"  
        process.execute()

        params["comite"] = "9"     
        params["subcomite"] = "5"  
        process.execute()

        params["comite"] = "9"     
        params["subcomite"] = "6"  
        #process.execute()

        params["comite"] = "10"
        params["tipoId"] = 2
        params["investigador"] = "manuelcampos@um.es"  
        params["periodo"] = "2015-2020"    
        #process.execute()

        params["comite"] = "11"
        #process.execute()

        params["comite"] = "14"
        params["tipoId"] = 2
        params["investigador"] = "jtpalma@um.es"
        params["periodo"] = "2013-2018"
        #process.execute()
        #process.execute()

    def _test_execute_acreditaciones(self):
        #2,3,4,5,7,8,11,12,15,16,18,19,
        comisiones = [21]
        for com in comisiones:
            params = {}
            params["comision"] = str(com)
            if com == 21:
                params['categoria_acreditacion'] = '1'
            params["tipo_acreditacion"] = "2"
            params["tipoId"] = 3
            params["investigador"] = "0000-0002-5525-1259"      #skarmeta  
            process = ProcessAcreditaciones.ProcessAcreditaciones(id_schedule = None, id_log = None, id_robot = "1", priority = "1", log_file_path = None, parameters=params)
            process.execute()

        params["tipoId"] = 2
        params["investigador"] = "manuelcampos@um.es"  
       

        params["tipoId"]=3
        params["investigador"]="0000-0003-1776-1992"
       

        params["tipoId"] = 2
        params["investigador"] = "jtpalma@um.es"
        



if __name__ == '__main__':
    unittest.main()