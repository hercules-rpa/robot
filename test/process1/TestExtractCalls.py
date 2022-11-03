import json
import sys
import os
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(os.path.dirname(currentdir))
sys.path.insert(1, parentdir)
print(currentdir, parentdir)
import unittest
import model.process.Process1.Subprocess.ProcessExtractCalls as ProcessExtractCalls

class TestExtractCalls(unittest.TestCase):
    def test_calls(self):
        file = open("hercules-rpa/test/files/calls/calls.txt", "r")
        response_text = file.read()
        file.close()
        process = ProcessExtractCalls.ProcessExtractCalls(
            id_schedule=None, id_log=None, id_robot="1", priority="1", log_file_path=None, parameters=None)
        announcements = json.loads(response_text)
        result = process.process_results(announcements, False)
        self.assertEqual(result[0], 113)

    def test_calls_1(self):
        file = open("hercules-rpa/test/files/calls/calls-1.txt", "r")
        response_text = file.read()
        file.close()
        process = ProcessExtractCalls.ProcessExtractCalls(
            id_schedule=None, id_log=None, id_robot="1", priority="1", log_file_path=None, parameters=None)
        announcements = json.loads(response_text)
        result = process.process_results(announcements, False)
        self.assertEqual(result[0], 3)
        
    def test_calls_2(self):
        file = open("hercules-rpa/test/files/calls/calls-2.txt", "r")
        response_text = file.read()
        file.close()
        process = ProcessExtractCalls.ProcessExtractCalls(
            id_schedule=None, id_log=None, id_robot="1", priority="1", log_file_path=None, parameters=None)
        announcements = json.loads(response_text)
        result = process.process_results(announcements, False)
        self.assertEqual(result[0], 3)

    def test_calls_3(self):
        file = open("hercules-rpa/test/files/calls/calls-3.txt", "r")
        response_text = file.read()
        file.close()
        process = ProcessExtractCalls.ProcessExtractCalls(
            id_schedule=None, id_log=None, id_robot="1", priority="1", log_file_path=None, parameters=None)
        announcements = json.loads(response_text)
        result = process.process_results(announcements, False)
        self.assertEqual(result[0], 3)

    def test_calls_4(self):
        file = open("hercules-rpa/test/files/calls/calls-4.txt", "r")
        response_text = file.read()
        file.close()
        process = ProcessExtractCalls.ProcessExtractCalls(
            id_schedule=None, id_log=None, id_robot="1", priority="1", log_file_path=None, parameters=None)
        announcements = json.loads(response_text)
        result = process.process_results(announcements, False)
        self.assertEqual(result[0], 8)

    def test_calls_5(self):
        file = open("hercules-rpa/test/files/calls/calls-5.txt", "r")
        response_text = file.read()
        file.close()
        process = ProcessExtractCalls.ProcessExtractCalls(
            id_schedule=None, id_log=None, id_robot="1", priority="1", log_file_path=None, parameters=None)
        announcements = json.loads(response_text)
        result = process.process_results(announcements, False)
        self.assertEqual(result[0], 9)

    def test_calls_6(self):
        file = open("hercules-rpa/test/files/calls/calls-6.txt", "r")
        response_text = file.read()
        file.close()
        process = ProcessExtractCalls.ProcessExtractCalls(
            id_schedule=None, id_log=None, id_robot="1", priority="1", log_file_path=None, parameters=None)
        announcements = json.loads(response_text)
        result = process.process_results(announcements, False)
        self.assertEqual(result[0], 1)

    def test_calls_7(self):
        file = open("hercules-rpa/test/files/calls/calls-7.txt", "r")
        response_text = file.read()
        file.close()
        process = ProcessExtractCalls.ProcessExtractCalls(
            id_schedule=None, id_log=None, id_robot="1", priority="1", log_file_path=None, parameters=None)
        announcements = json.loads(response_text)
        result = process.process_results(announcements, False)
        self.assertEqual(result[0], 2)

    def test_calls_8(self):
        file = open("hercules-rpa/test/files/calls/calls-8.txt", "r")
        response_text = file.read()
        file.close()
        process = ProcessExtractCalls.ProcessExtractCalls(
            id_schedule=None, id_log=None, id_robot="1", priority="1", log_file_path=None, parameters=None)
        announcements = json.loads(response_text)
        result = process.process_results(announcements, False)
        self.assertEqual(result[0], 5)

    def test_calls_9(self):
        file = open("hercules-rpa/test/files/calls/calls-9.txt", "r")
        response_text = file.read()
        file.close()
        process = ProcessExtractCalls.ProcessExtractCalls(
            id_schedule=None, id_log=None, id_robot="1", priority="1", log_file_path=None, parameters=None)
        announcements = json.loads(response_text)
        result = process.process_results(announcements, False)
        self.assertEqual(result[0], 5)

    def test_calls1(self):
        file = open("hercules-rpa/test/files/calls/announcements-1.txt", "r")
        response_text = file.read()
        file.close()
        process = ProcessExtractCalls.ProcessExtractCalls(
            id_schedule=None, id_log=None, id_robot="1", priority="1", log_file_path=None, parameters=None)
        announcements = json.loads(response_text)
        result = process.process_results(announcements, False)
        self.assertEqual(result[0], 1)

    def test_calls3(self):
        file = open("hercules-rpa/test/files/calls/announcements-2.txt", "r")
        response_text = file.read()
        file.close()
        process = ProcessExtractCalls.ProcessExtractCalls(
            id_schedule=None, id_log=None, id_robot="1", priority="1", log_file_path=None, parameters=None)
        announcements = json.loads(response_text)
        result = process.process_results(announcements, False)
        self.assertEqual(result[0], 2)      
    

    def test_calls6(self):
        file = open("hercules-rpa/test/files/calls/announcements-6.txt", "r")
        response_text = file.read()
        file.close()
        process = ProcessExtractCalls.ProcessExtractCalls(
            id_schedule=None, id_log=None, id_robot="1", priority="1", log_file_path=None, parameters=None)
        announcements = json.loads(response_text)
        result = process.process_results(announcements, False)
        self.assertEqual(result[0], 5)

    def test_calls9(self):
        file = open("hercules-rpa/test/files/calls/announcements-9.txt", "r")
        response_text = file.read()
        file.close()
        process = ProcessExtractCalls.ProcessExtractCalls(
            id_schedule=None, id_log=None, id_robot="1", priority="1", log_file_path=None, parameters=None)
        announcements = json.loads(response_text)
        result = process.process_results(announcements, False)
        self.assertEqual(result[0], 8)

    def test_calls_without_results(self):
        process = ProcessExtractCalls.ProcessExtractCalls(
            id_schedule=None, id_log=None, id_robot="1", priority="1", log_file_path=None, parameters=None)
        result = process.process_results(None, False)
        self.assertEqual(result[0], 0)


if __name__ == '__main__':
    unittest.main()