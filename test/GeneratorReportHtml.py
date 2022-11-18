# coding=utf-8
import HtmlTestRunner
import time
import unittest
import os
import time
# Definir el directorio del caso de prueba como el directorio actual
test_dir = os.path.dirname(os.path.realpath(__file__))  # ./hercules-rpa/test
test_dir1 = test_dir + '/reports'

if __name__ == "__main__":
    # Obtenga la hora actual de acuerdo con un formato determinado
    now = time.strftime("%Y-%m-%d_%H %M")

   # Definir ruta de almacenamiento de informes
    filename = test_dir1 + '/' + now + '-test_result.html'
    fp = open(filename, "w")
    caseList = ['process1']
    suite_module = []
    for case in caseList:  
        file_path = test_dir + '/' + case  # Usar la ruta del archivo de caso
        #  Cargue los casos de uso en lotes, el primer parámetro es la ruta de almacenamiento de los casos de uso, el segundo parámetro es el nombre del archivo de ruta, la ruta del directorio raíz del caso de uso top_level_dir, el valor predeterminado es Ninguno
        discover = unittest.defaultTestLoader.discover(
            file_path,
            pattern='Test*.py'
        )

        # Store discover en el grupo de elementos suite_module
        suite_module.append(discover)
        cont = 1
        for discover in suite_module:
            runner = HtmlTestRunner.HTMLTestRunner(stream=fp,
                        report_title="Informe de pruebas de los procesos de Hércules-RPA", 
                        report_name="process" + str(cont),
                        output=test_dir1)
             # Pruebas de ejecución
            runner.STYLESHEET_TMPL = '<link rel="stylesheet" href="my_stylesheet.css" type="text/css">'
            runner.run(discover)
            cont+=1

    print('Finaliza la creación del informe')
    fp.close()  # Cerrar el archivo del informe

