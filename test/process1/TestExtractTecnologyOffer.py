import json
import sys
import os
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(os.path.dirname(currentdir))
sys.path.insert(1, parentdir)
print(currentdir, parentdir)
import unittest
import pandas as pd
from model.process.Process1.Subprocess.ProcessExtractOTC import ProcessExtractOTC

class TestExtractTecnologyOffer(unittest.TestCase):
    def test_extract_articles_without_results(self):
        params = {}
        params["start_date"] = '2021-01-01'
        params["end_date"] = '2022-05-31'
        p = ProcessExtractOTC(id_schedule = None,
         id_log = None, id_robot = '1', priority ="1", log_file_path = None, parameters=params)
        result= p.execute()
        self.assertIsNone(result) 

    def test_without_results(self):
        file = open("hercules-rpa/test/files/otc/otc-without-results.txt", "r")
        response_text = file.read()
        json_dict = json.loads(response_text)
        file.close()
        process = ProcessExtractOTC(id_schedule = None, id_log = None, id_robot = None, priority ="1", log_file_path = None, parameters=None)
        results = process.process_results(pd.json_normalize(json_dict["results"]["bindings"]))
        self.assertEqual(len(results),0)  


if __name__ == '__main__':
    unittest.main()