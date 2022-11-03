import sys
import os
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(os.path.dirname(currentdir))
sys.path.insert(1, parentdir)
import unittest
import model.process.Proceso4.ProcessFiltroColaborativo as ProcessFiltroColaborativo
import model.process.Proceso4.ProcessSRContenido as ProcessSRContenido
import model.process.Proceso4.ProcessMotorHibrido as ProcessMotorHibrido
import model.process.Proceso4.model.ClassProcess4 as p4
import pandas as pd

class TestSistemaRecomendacion(unittest.TestCase):
    process = ProcessFiltroColaborativo.ProcessFiltroColaborativo(id_schedule = None, id_log = None, id_robot = "1", priority = "1", log_file_path = None, parameters=None)
    
    def test_filtro_colaborativo_0(self): 
        inputAreas = [
            {'areaId':8, 'nombre': 'TOS'},
            {'areaId':11, 'nombre': 'TIC'}
        ]
        inputAreas = pd.DataFrame(inputAreas)
        df_inv = pd.read_csv('hercules-rpa/test/process4/testRecomendacionFC.csv')
        investigadores_ids = df_inv.loc[~df_inv['invId'].duplicated()]
        investigadores_ids = investigadores_ids['invId'].tolist()
        investigadores = []
        for investigador in investigadores_ids:
            investigadores.append(p4.Investigador(id=investigador,nombre="test",email="test@um.es"))
        
        parameters = {}
        parameters['investigadores'] = investigadores

        filtroColaborativo = ProcessFiltroColaborativo.ProcessFiltroColaborativo(id_schedule = None, id_log = None, id_robot = "1", priority = "1", log_file_path = None, parameters=parameters)
        result = filtroColaborativo.recomedacion_filtro_colaborativo(inputAreas, df_inv, investigadores, threshold_count=150)
        self.assertEqual(result[90],1)
        self.assertEqual(result[91],0.30000000000000004)
        self.assertEqual(result[92],1)
        self.assertEqual(result[93],0.7)
        self.assertEqual(result[94],0.8)
        return result
    
    def test_filtro_colaborativo_1(self): 
        inputAreas = [
        {'areaId':4, 'nombre': 'TOS'},
        {'areaId':6, 'nombre': 'TIC'}
        ]
        inputAreas = pd.DataFrame(inputAreas)
        df_inv = pd.read_csv('hercules-rpa/test/process4/testRecomendacionFC.csv')
        investigadores_ids = df_inv.loc[~df_inv['invId'].duplicated()]
        investigadores_ids = investigadores_ids['invId'].tolist()
        investigadores = []
        for investigador in investigadores_ids:
            investigadores.append(p4.Investigador(id=investigador,nombre="test",email="test@um.es"))
        
        parameters = {}
        parameters['investigadores'] = investigadores

        filtroColaborativo = ProcessFiltroColaborativo.ProcessFiltroColaborativo(id_schedule = None, id_log = None, id_robot = "1", priority = "1", log_file_path = None, parameters=parameters)
        result = filtroColaborativo.recomedacion_filtro_colaborativo(inputAreas, df_inv, investigadores, threshold_count=150)
        self.assertEqual(result[90],0.6)
        self.assertEqual(result[91],1)
        self.assertEqual(result[92],1)
        self.assertEqual(result[93],0.5)
        self.assertEqual(result[94],1)
        return result
    
    def test_filtro_colaborativo_2(self): 
        inputAreas = [
        {'areaId':8, 'nombre': 'TOS'},
        {'areaId':11, 'nombre': 'TIC'}
        ]
        inputAreas = pd.DataFrame(inputAreas)
        df_inv = pd.read_csv('hercules-rpa/test/process4/testRecomendacionFC.csv')
        investigadores_ids = df_inv.loc[~df_inv['invId'].duplicated()]
        investigadores_ids = investigadores_ids['invId'].tolist()
        investigadores = []
        for investigador in investigadores_ids:
            investigadores.append(p4.Investigador(id=investigador,nombre="test",email="test@um.es"))
        
        parameters = {}
        parameters['investigadores'] = investigadores

        filtroColaborativo = ProcessFiltroColaborativo.ProcessFiltroColaborativo(id_schedule = None, id_log = None, id_robot = "1", priority = "1", log_file_path = None, parameters=parameters)
        result = filtroColaborativo.recomedacion_filtro_colaborativo(inputAreas, df_inv, investigadores, threshold_count=5)
        self.assertEqual(result[90],0.5199381588731546)
        self.assertEqual(result[91],0.5290732865723501)
        self.assertEqual(result[92],0.46286619686176517)
        self.assertEqual(result[93],0.5006377751113926)
        self.assertEqual(result[94],0.9695216111388298)
        return result
    
    def test_filtro_colaborativo_3(self): 
        inputAreas = [
            {'areaId':8, 'nombre': 'TOS'},
            {'areaId':11, 'nombre': 'TIC'},
            {'areaId':7, 'nombre': 'TIC'}
        ]
        inputAreas = pd.DataFrame(inputAreas)
        df_inv = pd.read_csv('hercules-rpa/test/process4/testRecomendacionFC.csv')
        investigadores_ids = df_inv.loc[~df_inv['invId'].duplicated()]
        investigadores_ids = investigadores_ids['invId'].tolist()
        investigadores = []
        for investigador in investigadores_ids:
            investigadores.append(p4.Investigador(id=investigador,nombre="test",email="test@um.es"))
        
        parameters = {}
        parameters['investigadores'] = investigadores

        filtroColaborativo = ProcessFiltroColaborativo.ProcessFiltroColaborativo(id_schedule = None, id_log = None, id_robot = "1", priority = "1", log_file_path = None, parameters=parameters)
        result = filtroColaborativo.recomedacion_filtro_colaborativo(inputAreas, df_inv, investigadores, threshold_count=5)
        self.assertEqual(result[90],0.6108669001681826)
        self.assertEqual(result[91],0.4920725573836336)
        self.assertEqual(result[92],0.30857746457451013)
        self.assertEqual(result[93],0.6670918500742617)
        self.assertEqual(result[94],0.9096419177062924)
        return result
    
    def test_filtro_colaborativo_4(self): 
        inputAreas = [
            {'areaId':4, 'nombre': 'TOS'},
            {'areaId':6, 'nombre': 'TIC'}
        ]
        inputAreas = pd.DataFrame(inputAreas)
        df_inv = pd.read_csv('hercules-rpa/test/process4/testRecomendacionFC.csv')
        investigadores_ids = df_inv.loc[~df_inv['invId'].duplicated()]
        investigadores_ids = investigadores_ids['invId'].tolist()
        investigadores = []
        for investigador in investigadores_ids:
            investigadores.append(p4.Investigador(id=investigador,nombre="test",email="test@um.es"))
        
        parameters = {}
        parameters['investigadores'] = investigadores

        filtroColaborativo = ProcessFiltroColaborativo.ProcessFiltroColaborativo(id_schedule = None, id_log = None, id_robot = "1", priority = "1", log_file_path = None, parameters=parameters)
        result = filtroColaborativo.recomedacion_filtro_colaborativo(inputAreas, df_inv, investigadores, threshold_count=5)
        self.assertEqual(result[90],0.7699276745316028)
        self.assertEqual(result[91],0.5025586290195514)
        self.assertEqual(result[92],0.57656853222703)
        self.assertEqual(result[93],0.5655926875964769)
        self.assertEqual(result[94],0.6892017636113607)
        return result
        
        
    def test_basado_contenido_0(self): 
        areaTematica1 = p4.AreaTematica(id=4,areaPadre=None,nombre="TOS")
        areaTematica2 = p4.AreaTematica(id=6,areaPadre=areaTematica1,nombre="TIC")
        areaTematica1.areaHijo=areaTematica2
        convocatoria = p4.Convocatoria(2,"test",[areaTematica1], None)
        parameters = {}
        parameters['convocatoria'] = convocatoria
        sr_contenido = ProcessSRContenido.ProcessSRContenido(id_schedule = None, id_log = None, id_robot = "1", priority = "1", log_file_path = None, parameters=parameters)
        convo_input_format = ['BIO AEI Proyectos Unión  Europea COMPETITIVOS EUROPEAN COMMISION Energy efficiency EUROPEAN COMMISION Subvención']
        investigadores = {}
        df_inv = pd.read_csv('hercules-rpa/test/process4/testRecomendacionContenido.csv')
        for idx, id_inv in enumerate(df_inv['invId'].tolist()):
            if not id_inv in investigadores:
                investigadores[id_inv] = []
            word = df_inv['words'][idx]
            investigadores[id_inv].append(word)
        result = sr_contenido.SR_contenido(convo_input_format, investigadores, threshold_count=3, test=True)
        self.assertEqual(result[90],0.05170876899950191)
        self.assertEqual(result[91],0.72281172408504)
        self.assertEqual(result[92],1)
        return result
    
    def test_basado_contenido_1(self): 
        areaTematica1 = p4.AreaTematica(id=4,areaPadre=None,nombre="TOS")
        areaTematica2 = p4.AreaTematica(id=6,areaPadre=areaTematica1,nombre="TIC")
        areaTematica1.areaHijo=areaTematica2
        convocatoria = p4.Convocatoria(2,"test",[areaTematica1], None)
        parameters = {}
        parameters['convocatoria'] = convocatoria
        sr_contenido = ProcessSRContenido.ProcessSRContenido(id_schedule = None, id_log = None, id_robot = "1", priority = "1", log_file_path = None, parameters=parameters)
        convo_input_format = ['Convocatoria PCI Energy efficiency EUROPEAN COMMISION Subvención']
        investigadores = {}
        df_inv = pd.read_csv('hercules-rpa/test/process4/testRecomendacionContenido.csv')
        for idx, id_inv in enumerate(df_inv['invId'].tolist()):
            if not id_inv in investigadores:
                investigadores[id_inv] = []
            word = df_inv['words'][idx]
            investigadores[id_inv].append(word)
        result = sr_contenido.SR_contenido(convo_input_format, investigadores, threshold_count=3, test=True)
        self.assertEqual(result[90], 0.16116459280507603)
        self.assertEqual(result[91],0.6149890615709249)
        self.assertEqual(result[92],1)
        return result
    
    def test_basado_contenido_2(self): 
        areaTematica1 = p4.AreaTematica(id=4,areaPadre=None,nombre="TOS")
        areaTematica2 = p4.AreaTematica(id=6,areaPadre=areaTematica1,nombre="TIC")
        areaTematica1.areaHijo=areaTematica2
        convocatoria = p4.Convocatoria(2,"test",[areaTematica1], None)
        parameters = {}
        parameters['convocatoria'] = convocatoria
        sr_contenido = ProcessSRContenido.ProcessSRContenido(id_schedule = None, id_log = None, id_robot = "1", priority = "1", log_file_path = None, parameters=parameters)
        convo_input_format = ['Convocatoria PCI UGI Proyectos IDI Subvención']
        investigadores = {}
        df_inv = pd.read_csv('hercules-rpa/test/process4/testRecomendacionContenido.csv')
        for idx, id_inv in enumerate(df_inv['invId'].tolist()):
            if not id_inv in investigadores:
                investigadores[id_inv] = []
            word = df_inv['words'][idx]
            investigadores[id_inv].append(word)
        result = sr_contenido.SR_contenido(convo_input_format, investigadores, threshold_count=3, test=True)
        self.assertEqual(result[90], 0.43519413988924455)
        self.assertEqual(result[91],0.11185478398230513)
        self.assertEqual(result[92],1)
        return result
    
    def test_basado_contenido_3(self): 
        areaTematica1 = p4.AreaTematica(id=4,areaPadre=None,nombre="TOS")
        areaTematica2 = p4.AreaTematica(id=6,areaPadre=areaTematica1,nombre="TIC")
        areaTematica1.areaHijo=areaTematica2
        convocatoria = p4.Convocatoria(2,"test",[areaTematica1], None)
        parameters = {}
        parameters['convocatoria'] = convocatoria
        sr_contenido = ProcessSRContenido.ProcessSRContenido(id_schedule = None, id_log = None, id_robot = "1", priority = "1", log_file_path = None, parameters=parameters)
        convo_input_format = ['AEI UGI EUROPEAN COMMISION Retos sociales']
        investigadores = {}
        df_inv = pd.read_csv('hercules-rpa/test/process4/testRecomendacionContenido.csv')
        for idx, id_inv in enumerate(df_inv['invId'].tolist()):
            if not id_inv in investigadores:
                investigadores[id_inv] = []
            word = df_inv['words'][idx]
            investigadores[id_inv].append(word)
        result = sr_contenido.SR_contenido(convo_input_format, investigadores, threshold_count=1, test=True)
        self.assertEqual(result[90],0.14664711502135333)
        self.assertEqual(result[91],0.6793662204867574)
        self.assertEqual(result[92],0.545544725589981)
        return result
    
    def test_basado_contenido_4(self): 
        areaTematica1 = p4.AreaTematica(id=4,areaPadre=None,nombre="TOS")
        areaTematica2 = p4.AreaTematica(id=6,areaPadre=areaTematica1,nombre="TIC")
        areaTematica1.areaHijo=areaTematica2
        convocatoria = p4.Convocatoria(2,"test",[areaTematica1], None)
        parameters = {}
        parameters['convocatoria'] = convocatoria
        sr_contenido = ProcessSRContenido.ProcessSRContenido(id_schedule = None, id_log = None, id_robot = "1", priority = "1", log_file_path = None, parameters=parameters)
        convo_input_format = ['Convocatoria PCI UGI Proyectos IDI Subvención']
        investigadores = {}
        df_inv = pd.read_csv('hercules-rpa/test/process4/testRecomendacionContenido.csv')
        for idx, id_inv in enumerate(df_inv['invId'].tolist()):
            if not id_inv in investigadores:
                investigadores[id_inv] = []
            word = df_inv['words'][idx]
            investigadores[id_inv].append(word)
        result = sr_contenido.SR_contenido(convo_input_format, investigadores, threshold_count=1, test=True)
        self.assertEqual(result[90],0.4351941398892446)
        self.assertEqual(result[91],0.22645540682891918)
        self.assertEqual(result[92],0.4351941398892446)
        return result
        
    def test_motor_hibrido_0(self):
        test_fc = self.test_filtro_colaborativo_0()
        test_c  = self.test_basado_contenido_0()
        input_list = []
        format_input = {}
        format_input['SistemaRecomendacion'] = 'FiltroColaborativo'
        format_input['peso'] = 0.70
        format_input['data'] = test_fc
        input_list.append(format_input)
        format_input = {}
        format_input['SistemaRecomendacion'] = 'SRContenido'
        format_input['peso'] = 0.2
        format_input['data'] = test_c
        input_list.append(format_input)
        motorHibrido = ProcessMotorHibrido.ProcessMotorHibrido(id_schedule = None, id_log = None, id_robot = "1", priority = "1", log_file_path = None, parameters=input_list)
        motorHibrido.execute()
        result = motorHibrido.result
        self.assertEqual(result[90],0.7103417537999004)
        self.assertEqual(result[91],0.354562344817008)
        self.assertEqual(result[92],0.8999999999999999)
        self.assertEqual(result[93],0.48999999999999994)
        self.assertEqual(result[94],0.5599999999999999)
        
    def test_motor_hibrido_1(self):
        test_fc = self.test_filtro_colaborativo_1()
        test_c  = self.test_basado_contenido_1()
        input_list = []
        format_input = {}
        format_input['SistemaRecomendacion'] = 'FiltroColaborativo'
        format_input['peso'] = 0.70
        format_input['data'] = test_fc
        input_list.append(format_input)
        format_input = {}
        format_input['SistemaRecomendacion'] = 'SRContenido'
        format_input['peso'] = 0.2
        format_input['data'] = test_c
        input_list.append(format_input)
        motorHibrido = ProcessMotorHibrido.ProcessMotorHibrido(id_schedule = None, id_log = None, id_robot = "1", priority = "1", log_file_path = None, parameters=input_list)
        motorHibrido.execute()
        result = motorHibrido.result
        self.assertEqual(result[90],0.4522329185610152)
        self.assertEqual(result[91],0.822997812314185)
        self.assertEqual(result[92],0.8999999999999999)
        self.assertEqual(result[93],0.35)
        self.assertEqual(result[94],0.7)
        
    def test_motor_hibrido_2(self):
        test_fc = self.test_filtro_colaborativo_2()
        test_c  = self.test_basado_contenido_2()
        input_list = []
        format_input = {}
        format_input['SistemaRecomendacion'] = 'FiltroColaborativo'
        format_input['peso'] = 0.70
        format_input['data'] = test_fc
        input_list.append(format_input)
        format_input = {}
        format_input['SistemaRecomendacion'] = 'SRContenido'
        format_input['peso'] = 0.2
        format_input['data'] = test_c
        input_list.append(format_input)
        motorHibrido = ProcessMotorHibrido.ProcessMotorHibrido(id_schedule = None, id_log = None, id_robot = "1", priority = "1", log_file_path = None, parameters=input_list)
        motorHibrido.execute()
        result = motorHibrido.result
        self.assertEqual(result[90],0.4509955391890571)
        self.assertEqual(result[91],0.39272225739710603)
        self.assertEqual(result[92],0.5240063378032356)
        self.assertEqual(result[93],0.3504464425779748)
        self.assertEqual(result[94],0.6786651277971808)
        
    def test_motor_hibrido_3(self):
        test_fc = self.test_filtro_colaborativo_3()
        test_c  = self.test_basado_contenido_3()
        input_list = []
        format_input = {}
        format_input['SistemaRecomendacion'] = 'FiltroColaborativo'
        format_input['peso'] = 0.70
        format_input['data'] = test_fc
        input_list.append(format_input)
        format_input = {}
        format_input['SistemaRecomendacion'] = 'SRContenido'
        format_input['peso'] = 0.2
        format_input['data'] = test_c
        input_list.append(format_input)
        motorHibrido = ProcessMotorHibrido.ProcessMotorHibrido(id_schedule = None, id_log = None, id_robot = "1", priority = "1", log_file_path = None, parameters=input_list)
        motorHibrido.execute()
        result = motorHibrido.result
        self.assertEqual(result[90],0.4569362531219984)
        self.assertEqual(result[91],0.480324034265895)
        self.assertEqual(result[92],0.3251131703201533)
        self.assertEqual(result[93],0.46696429505198317)
        self.assertEqual(result[94],0.6367493423944046)
        
    def test_motor_hibrido_4(self):
        test_fc = self.test_filtro_colaborativo_4()
        test_c  = self.test_basado_contenido_4()
        input_list = []
        format_input = {}
        format_input['SistemaRecomendacion'] = 'FiltroColaborativo'
        format_input['peso'] = 0.70
        format_input['data'] = test_fc
        input_list.append(format_input)
        format_input = {}
        format_input['SistemaRecomendacion'] = 'SRContenido'
        format_input['peso'] = 0.2
        format_input['data'] = test_c
        input_list.append(format_input)
        motorHibrido = ProcessMotorHibrido.ProcessMotorHibrido(id_schedule = None, id_log = None, id_robot = "1", priority = "1", log_file_path = None, parameters=input_list)
        motorHibrido.execute()
        result = motorHibrido.result
        print(result)
        self.assertEqual(result[90],0.6259882001499708)
        self.assertEqual(result[91],0.3970821216794698)
        self.assertEqual(result[92],0.49063680053676983)
        self.assertEqual(result[93],0.3959148813175338)
        self.assertEqual(result[94],0.4824412345279524)
        
if __name__ == '__main__':
    unittest.main()                     
