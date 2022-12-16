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
        response_token = self.client.get(
                    url="/robots/robotDESAUM/", 
                    headers={'Authorization': 'Bearer ' + self.token})
        token_robot = ""
        if response_token and response_token.status_code == 200:
            token_robot = response_token.json()["token"]
            response_access_token = self.client.post(
                        url="/register/token/", 
                        headers={
                                'Authorization': 'Bearer ' + self.token,
                                'Content-Type':'application/json'
                            }, 
                        data=json.dumps({
                            "iduser": 859,
                            "token": token_robot,
                            "idrobot":"robotDESAUM"
                        }))
            access_token = ""
            if response_access_token and response_access_token.status_code == 200:
                access_token = response_access_token.json()["access_token"]       
        if token_robot != "":
            if access_token != "":
                for i in self.times:
                    self.client.post(
                        url="/register/calificacion/area", 
                        headers={
                                'Authorization': 'Bearer ' + access_token,
                                'Content-Type':'application/json'
                            },
                        data=json.dumps([
                            {
                            "idinvestigador":859,
                            "idarea": 3,
                            "puntuacion":4.5,
                            "nombre": None
                            },
                            {
                            "idinvestigador":859,
                            "idarea": 3,
                            "puntuacion":4.5,
                            "nombre": None
                            }
                        ]))
                    self.client.post(
                        url="/register/calificacion/area", 
                        headers={
                                'Authorization': 'Bearer ' + access_token,
                                'Content-Type':'application/json'
                            },  
                        data=json.dumps([
                            {
                            "idinvestigador":859,
                            "idarea": 3,
                            "puntuacion":4.5,
                            "nombre": None
                            },
                            {
                            "idinvestigador":859,
                            "idarea": 3,
                            "puntuacion":4.5,
                            "nombre": None
                            }
                        ]))
            else:
                print("Error al obtener el token del investigador.")
        else:
            print("Error al obtener el token del robot.")
        self.environment.runner.quit()