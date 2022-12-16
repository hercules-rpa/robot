from locust import HttpUser, task, between

import json
from datetime import datetime, timedelta

class SexeniosProcessUser(HttpUser):
    host = "https://rpa-api-desa.um.es/api/orchestrator"
    token = ""

    @task
    def test_load(self):
        while self.token == "":
            response = self.client.post("/auth/login", json={'username': 'admin', 'password':'admin'})
            if response.ok:
                self.token = response.json()['Auth']
            else:
                self.token = ""
        months = range (1, 11)
        for month in months:
            self.client.post(
                url="/schedules/execute/", 
                headers={'Authorization': 'Bearer ' + self.token}, 
                data=json.dumps({
                    "time_schedule": {
                        "every": [1, "seconds"],
                        "at": None,
                        "forever": False,
                        "tag": "Prueba instantanea",
                        "category": "Extraer Boletines Noticias"
                    },
                    "process":{
                        "priority":1,
                        "id_robot":"robot1",
                        "parameters":{
                            "perfil_tecnologico": False,
                            "receivers":[
                                {"receiver":"jesus.salinas@treelogic.com"}
                                ],
                            "start_date": (datetime.now() - timedelta(days=month*30)).strftime("%Y-%m-%d"),
                            "end_date": datetime.now().strftime("%Y-%m-%d")
                        },
                        "id_process":13,
                        "exclude_robots":[]
                    }
                }))
        self.environment.runner.quit()