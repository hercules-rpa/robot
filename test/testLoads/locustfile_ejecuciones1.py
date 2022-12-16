from locust import HttpUser, task, between

import json
from datetime import datetime, timedelta

class SexeniosProcessUser(HttpUser):
    host = "https://rpa-api-desa.um.es/api/orchestrator"
    token = ""
    times = range(1,11)

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
                        "category": "Extraer Sexenios"
                    },
                    "process": {
                        "id_robot": "robotDESAUM",
                        "priority": 1,
                        "parameters" : {
                            "comite": "9",     
                            "subcomite": "1",   
                            "periodo": "2015-2020",
                            "tipoId": 3,
                            "investigador": "0000-0001-5844-4163"
                        },        
                        "id_process": 18,
                        "exclude_robots":[]
                    }
                }))

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
                        "category": "Extraer Acreditaciones"
                    },
                    "process": {
                        "id_robot": "robotDESAUM",
                        "priority": 1,
                        "parameters" : {
                            "comision" : "15",
                            "tipo_acreditacion" : "2",
                            "tipoId" : 3,
                            "investigador" : "0000-0002-5525-1259"
                        },        
                        "id_process": 22,
                        "exclude_robots":[]
                    }
                }))
        
        if self.token == "":
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

        if self.token == "":
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
        
        if self.token == "":
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
                        "category": "Extraer Bases reguladoras"
                    },
                    "process": {
                        "id_robot": "robotDESAUM",
                        "priority": 1,
                        "parameters": {
                            "perfil_tecnologico": False, 
                            "receivers_otri": [
                                {"receiver": "jesus.salinas@treelogic.com"}
                                ], 
                            "receivers_ugi": [
                                {"receiver": "jesus.salinas@treelogic.com"}
                                ], 
                            "start_date": (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d"),
                            "end_date": datetime.now().strftime("%Y-%m-%d")
                        },
                        "id_process": 10,
                        "exclude_robots":[]
                    }
                }))

        if self.token == "":
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
                    "time_schedule": {
                        "every": [1, "seconds"],
                        "at": None,
                        "forever": False,
                        "tag": "Prueba instantanea",
                        "category": "Extraer Boletines Noticias"
                    },
                    "process":{
                        "priority":1,
                        "id_robot":"robotDESAUM",
                        "parameters":{
                            "perfil_tecnologico": False,
                            "receivers":[
                                {"receiver":"jesus.salinas@treelogic.com"}
                                ],
                            "start_date": (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d"),
                            "end_date": datetime.now().strftime("%Y-%m-%d")
                        },
                        "id_process":13,
                        "exclude_robots":[]
                    }
                }))

        if self.token == "":
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