import sys
import os
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(os.path.dirname(currentdir))
sys.path.insert(1, parentdir)
print(currentdir, parentdir)
import unittest
from model.process.ProcessExtractRegulatoryBases import ProcessExtractRegulatoryBases

class TestExtractRegulatoryBases(unittest.TestCase):
    process = ProcessExtractRegulatoryBases(id_schedule = None, id_log = None, id_robot = "1", priority = "1", log_file_path = None, parameters=None)
    
    def get_params(self, filename):
        params = {}
        params["filename"] = filename
        entries = ["titulo", "urlPdf"]
        params["nodos"] = {"item": entries}
        return params
    
    def set_properties(self, tagName: str, nodo):
        """Función encargada de hidratar las propiedades de una base reguladora"""
        if tagName == 'titulo':
            print('titulo: ' + nodo.firstChild.data)
        if tagName == 'urlPdf':
            print('url: ' + nodo.firstChild.data)

    def test_boe_20220422(self): 
        nodes = self.process.get_nodes(self.get_params("hercules-rpa/test/files/BOE/boe-20220422.xml"), False)
        results = self.process.process_results(nodes)  
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].url,'/boe/dias/2022/04/22/pdfs/BOE-A-2022-6556.pdf')

    def test_boe_20220504(self):
        nodes = self.process.get_nodes(self.get_params("hercules-rpa/test/files/BOE/boe-20220504.xml"), False)
        results = self.process.process_results(nodes) 
        self.assertEqual(len(results), 2)
        self.assertEqual(results[0].url,'/boe/dias/2022/05/04/pdfs/BOE-A-2022-7307.pdf')
        self.assertEqual(results[1].url,'/boe/dias/2022/05/04/pdfs/BOE-B-2022-13808.pdf')

    def test_boe_20220209_otri(self):
        nodes = self.process.get_nodes(self.get_params("hercules-rpa/test/files/BOE/boe-20220209-otri.xml"), False)
        results = self.process.process_results(nodes)  
        self.assertEqual(len(results), 1)

    def test_boe_20211211(self):
        nodes = self.process.get_nodes(self.get_params("hercules-rpa/test/files/BOE/boe-20221211.xml"), False)
        results = self.process.process_results(nodes)  
        self.assertEqual(len(results), 2)
    
    def test_boe_20211208(self):
        nodes = self.process.get_nodes(self.get_params("hercules-rpa/test/files/BOE/boe-20221208.xml"), False)
        results = self.process.process_results(nodes)  
        self.assertEqual(len(results), 2)  

    def test_boe_20210223(self):
        nodes = self.process.get_nodes(self.get_params("hercules-rpa/test/files/BOE/boe-20210223.xml"), False)
        results = self.process.process_results(nodes)
        self.assertEqual(len(results), 0)

    def test_boe_20200930(self):
        nodes = self.process.get_nodes(self.get_params("hercules-rpa/test/files/BOE/boe-2020-09-30.xml"), False)
        results = self.process.process_results(nodes)  
        self.assertEqual(len(results), 1)

    
    def test_boe_20220225_without_results(self):
        nodes = self.process.get_nodes(self.get_params("hercules-rpa/test/files/BOE/boe-20220225.xml"), False)
        results = self.process.process_results(nodes)  
        self.assertEqual(len(results), 0)

    def test_boe_20220430(self):
        nodes = self.process.get_nodes(self.get_params("hercules-rpa/test/files/BOE/20220430.xml"), False)
        results = self.process.process_results(nodes)  
        self.assertEqual(len(results), 1) 

    def test_boe_20220504(self):
        nodes = self.process.get_nodes(self.get_params("hercules-rpa/test/files/BOE/20220504.xml"), False)
        results = self.process.process_results(nodes)  
        self.assertEqual(len(results), 2)
        self.assertEqual(results[0].url, '/boe/dias/2022/05/04/pdfs/BOE-A-2022-7307.pdf')
        self.assertEqual(results[1].url, '/boe/dias/2022/05/04/pdfs/BOE-B-2022-13808.pdf')

    def test_boe_20220526(self):
        nodes = self.process.get_nodes(self.get_params("hercules-rpa/test/files/BOE/20220526.xml"), False)
        results = self.process.process_results(nodes)  
        self.assertEqual(len(results), 2) 
        self.assertEqual(results[0].url, '/boe/dias/2022/05/26/pdfs/BOE-A-2022-8634.pdf')
        self.assertEqual(results[1].url, '/boe/dias/2022/05/26/pdfs/BOE-A-2022-8635.pdf')  
    
    def test_boe_20220610(self):
        nodes = self.process.get_nodes(self.get_params("hercules-rpa/test/files/BOE/20220610.xml"), False)
        results = self.process.process_results(nodes)  
        self.assertEqual(len(results), 1) 
    
    def test_boe_20220618(self):
        nodes = self.process.get_nodes(self.get_params("hercules-rpa/test/files/BOE/20220618.xml"), False)
        results = self.process.process_results(nodes)  
        self.assertEqual(len(results), 1) 
    
    def test_boe_20220621(self):
        nodes = self.process.get_nodes(self.get_params("hercules-rpa/test/files/BOE/20220621.xml"), False)
        results = self.process.process_results(nodes)  
        self.assertEqual(len(results), 1) 

    def test_boe_20220627(self):
        nodes = self.process.get_nodes(self.get_params("hercules-rpa/test/files/BOE/20220627.xml"), False)
        results = self.process.process_results(nodes)  
        self.assertEqual(len(results), 1)
    
    def test_boe_20220802(self):
        nodes = self.process.get_nodes(self.get_params("hercules-rpa/test/files/BOE/20220802.xml"), False)
        results = self.process.process_results(nodes)  
        self.assertEqual(len(results), 1)
    
    def test_boe_20220818(self):
        nodes = self.process.get_nodes(self.get_params("hercules-rpa/test/files/BOE/20220818.xml"), False)
        results = self.process.process_results(nodes)  
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].url, '/boe/dias/2022/08/18/pdfs/BOE-A-2022-13893.pdf')
    

    def test_boe_20220826(self):
        nodes = self.process.get_nodes(self.get_params("hercules-rpa/test/files/BOE/20220826.xml"), False)
        results = self.process.process_results(nodes)  
        self.assertEqual(len(results), 1)

    def test_boe_20220110(self):
        nodes = self.process.get_nodes(self.get_params("hercules-rpa/test/files/BOE/20220110.xml"), False)
        results = self.process.process_results(nodes)  
        self.assertEqual(len(results), 1)

    def test_boe_20220309(self):
        nodes = self.process.get_nodes(self.get_params("hercules-rpa/test/files/BOE/20220309.xml"), False)
        results = self.process.process_results(nodes)  
        self.assertEqual(len(results), 1)
    
    def test_boe_20220223(self):
        nodes = self.process.get_nodes(self.get_params("hercules-rpa/test/files/BOE/20220223.xml"), False)
        results = self.process.process_results(nodes)  
        self.assertEqual(len(results), 1)
    
    def test_boe_20220325(self):
        nodes = self.process.get_nodes(self.get_params("hercules-rpa/test/files/BOE/20220325.xml"), False)
        results = self.process.process_results(nodes)  
        self.assertEqual(len(results), 1)
    
    def test_boe_20220328(self):
        nodes = self.process.get_nodes(self.get_params("hercules-rpa/test/files/BOE/20220328.xml"), False)
        results = self.process.process_results(nodes)  
        self.assertEqual(len(results), 1)
    
    def test_boe_20220329(self):
        nodes = self.process.get_nodes(self.get_params("hercules-rpa/test/files/BOE/20220329.xml"), False)
        results = self.process.process_results(nodes)  
        self.assertEqual(len(results), 1)
    
        
    
if __name__ == '__main__':
    print('testExtractRegulatoryBases')
    unittest.main()                     
