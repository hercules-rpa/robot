from datetime import datetime
import sys
import os
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(os.path.dirname(currentdir))
sys.path.insert(1, parentdir)
print(currentdir, parentdir)
import unittest
import model.process.Process1.Subprocess.ProcessExtractArticles as ProcessExtractArticles
import model.process.ProcessGenerateTransferReport as ProcessGenerateTransferReport
from model.process.Process1.Subprocess.ProcessExtractOTC import ProcessExtractOTC
from model.process.Process1.Subprocess.ProcessExtractThesis import ProcessExtractThesis
from model.process.Process1.Subprocess.ProcessExtractCalls import ProcessExtractCalls
from model.process.Process1.Subprocess.ProcessExtractInventions import ProcessExtractInventions
from model.process.Process1.Subprocess.ProcessExtractProjectsAndContracts import ProcessExtractProjectsAndContracts



class TestExtractArticles(unittest.TestCase):
    def est_extract_articles_without_results(self):
        params = {}
        params["start_date"] = '2021-01-01'
        params["end_date"] = '2022-05-31'
        processArticles = ProcessExtractArticles.ProcessExtractArticles(id_schedule = None,
         id_log = None, id_robot = '1', priority ="1", log_file_path = None, parameters=params)
        processArticles.execute()

    def est_extract_thesis(self):
        params = {}
        params["start_date"] = datetime.strptime('2020-01-01', "%Y-%m-%d")
        params["end_date"] = datetime.strptime('2022-09-29', "%Y-%m-%d")
        p = ProcessExtractThesis(id_schedule = None,
         id_log = None, id_robot = '1', priority ="1", log_file_path = None, parameters=params)
        p.execute()
        

    def est_extract_otc(self):
        params = {}
        params["start_date"] = '2020-01-01'
        params["end_date"] = '2022-09-12'
        p = ProcessExtractOTC(id_schedule = None,
         id_log = None, id_robot = '1', priority ="1", log_file_path = None, parameters=params)
        p.execute()
    
    def test_extract_projects(self):
        params = {}
        start_date = datetime(2019,1,1,00,00)
        end_date = datetime(2019,12,31,23,59,59)
        start_str = start_date.strftime("%Y-%m-%dT%H:%M:%SZ")
        end_str = end_date.strftime("%Y-%m-%dT%H:%M:%SZ")
        params["start_date"] = start_str
        params["end_date"] = end_str
        p = ProcessExtractProjectsAndContracts(id_schedule = None,
         id_log = None, id_robot = '1', priority ="1", log_file_path = None, parameters=params)
        p.execute()
    
    def est_extract_otc(self):
        params = {}
        start_date = datetime(2019,1,1,00,00)
        end_date = datetime(2022,12,31,23,59,59)
        start_str = start_date.strftime("%Y-%m-%dT%H:%M:%SZ")
        end_str = end_date.strftime("%Y-%m-%dT%H:%M:%SZ")
        params["start_date"] = start_str
        params["end_date"] = end_str
        p = ProcessExtractOTC(id_schedule = None,
         id_log = None, id_robot = '1', priority ="1", log_file_path = None, parameters=params)
        p.execute()

    def est_extract_calls(self):
        params = {}
        params["start_date"] = '2020-01-01'
        params["end_date"] = '2022-09-13'
        p = ProcessExtractCalls(id_schedule = None,
         id_log = None, id_robot = '1', priority ="1", log_file_path = None, parameters=params)
        p.execute()
        

    def st_ExecutionGenerateTransferReport(self):
        params = {}
        params["start_date"] = '2021-01-01'
        params["end_date"] = '2022-05-31'
        processArticles = ProcessExtractArticles.ProcessExtractArticles(id_schedule = None,
         id_log = None, id_robot = '1', priority ="1", log_file_path = None, parameters=params)
        processArticles.execute()
        p = ProcessGenerateTransferReport.ProcessGenerateTransferReport(id_schedule = None,
         id_log = None, id_robot = '1', priority ="1", log_file_path = None, parameters=params)
        print(p.msg_articles(processArticles.result))

    def est_ExecutionGenerateTransferReport2(self):
        params = {}
        params["start_date"] = '2022-01-01'
        params["end_date"] = '2022-07-31'
        params["receivers"] = []
        user = {}
        user["receiver"] = 'mariateresa.moreno@treelogic.com'
        params['receivers'].append(user)
        
        p = ProcessGenerateTransferReport.ProcessGenerateTransferReport(id_schedule = None,
         id_log = None, id_robot = '1', priority ="1", log_file_path = None, parameters=params)
        
        p.execute()



if __name__ == '__main__':
    unittest.main()