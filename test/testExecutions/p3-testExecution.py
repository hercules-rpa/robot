import sys
import os

import requests
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(os.path.dirname(currentdir))
sys.path.insert(1, parentdir)
print(currentdir, parentdir)
import unittest
#import model.process.ProcessExtractRegulatoryBases as ProcessRegulatoryBases

class TestExecution(unittest.TestCase):
    def est_extract(self):
        params = {}
        params["start_date"] = '2022-01-01'
        params["end_date"] = '2022-09-30'
        #process = ProcessRegulatoryBases.ProcessExtractRegulatoryBases(id_schedule = None,
        # id_log = None, id_robot = '1', priority ="1", log_file_path = None, parameters=params)
        #process.execute()

    def test(self):
        requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += ':RC4-SHA'
        response = requests.get('https://boe.es/diario_boe/xml.php?id=BOE-S-20221101')
        print(response)
        print(response.text)


if __name__ == '__main__':
    unittest.main()