from locust import HttpUser, task, between

import json
from datetime import datetime, timedelta

class SexeniosProcessUser(HttpUser):
    host = "https://rpa-api-desa.um.es/api/orchestrator"
    token = ""
    times = range (1, 11)

    @task
    def test_load(self):
        while self.token == "":
            response = self.client.post("/auth/login", json={'username': 'admin', 'password':'admin'})
            if response.ok:
                self.token = response.json()['Auth']
            else:
                self.token = ""
        for i in self.times:

            self.client.post(
                url="/schedules/execute/", 
                headers={
                        'Authorization': 'Bearer ' + self.token,
                        'Content-Type':'application/json'
                    },  
                data=json.dumps({
                    "time_schedule":{
                        "every": [1, "seconds"],
                        "at": None,
                        "forever": False,
                        "tag": "Prueba instantanea",
                        "category": "Extraer Convocatorias"
                    },
                    "process": {
                        "id_robot": "robotDESAUM",
                        "priority": 1,
                        "parameters": {
                            "start_date": (datetime.now() - timedelta(days=15)).strftime("%Y-%m-%d"),
                            "end_date": datetime.now().strftime("%Y-%m-%d"),
                            "receivers":[
                                {"receiver":"jesus.salinas@treelogic.com"}
                            ]
                        },
                        "id_process": 9,
                        "exclude_robots":[]
                    }
                }))

            self.client.post(
                url="/schedules/execute/", 
                headers={
                        'Authorization': 'Bearer ' + self.token,
                        'Content-Type':'application/json'
                    },  
                data=json.dumps({
                    "time_schedule":{
                        "every": [1, "seconds"],
                        "at": None,
                        "forever": False,
                        "tag": "Prueba instantanea",
                        "category": "Extraer Convocatoria BDNS"
                    },
                    "process": {
                        "id_robot": "robotDESAUM",
                        "priority": 1,
                        "parameters": {
                            "bdns":"525644"
                        },
                        "id_process": 9,
                        "exclude_robots":[]
                    }
                }))

            self.client.post(
                url="/schedules/execute/", 
                headers={
                        'Authorization': 'Bearer ' + self.token,
                        'Content-Type':'application/json'
                    }, 
                data=json.dumps({
                    "time_schedule":{
                        "every": [1, "seconds"],
                        "at": None,
                        "forever": False,
                        "tag": "Prueba instantanea",
                        "category": "Extraer Concesiones"
                    },
                    "process": {
                        "id_robot": "robotDESAUM",
                        "priority": 1,
                        "parameters": {
                            "nif_universidad": [
                                { "nif": "Q3018001B" }
                                ],
                            "receivers":[
                                {"receiver":"jesus.salinas@treelogic.com"}
                            ]
                        },
                        "id_process": 16,
                        "exclude_robots":[]
                    }
                }))
                
        self.environment.runner.quit()