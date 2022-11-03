import sys
import os
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(os.path.dirname(currentdir))
sys.path.insert(1, parentdir)
print(currentdir, parentdir)
import unittest
import model.process.ProcessExtractRegulatoryBases as ProcessRegulatoryBases

class TestExecution(unittest.TestCase):
    def test_extract(self):
        params = {}
        params["start_date"] = '2022-01-01'
        params["end_date"] = '2022-09-30'
        process = ProcessRegulatoryBases.ProcessExtractRegulatoryBases(id_schedule = None,
         id_log = None, id_robot = '1', priority ="1", log_file_path = None, parameters=params)
        process.execute()


if __name__ == '__main__':
    unittest.main()