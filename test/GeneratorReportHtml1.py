# coding=utf-8
import HtmlTestRunner
import time
import unittest
import os
import time
# Definir el directorio del caso de prueba como el directorio actual
test_dir = os.path.dirname(os.path.realpath(__file__))  # ../hercules-rpa/test
test_dir1 = test_dir + '/reports'

if __name__ == "__main__":
    # Obtenga la hora actual de acuerdo con un formato determinado
    now = time.strftime("%Y-%m-%d_%H %M")

   # Definir ruta de almacenamiento de informes
    filename = test_dir1 + '/' + now + '-test_result.html'
    fp = open(filename, "w")
    print(test_dir + '/test-execution')
    discover = unittest.defaultTestLoader.discover(
            start_dir =test_dir + '/process1',            
            pattern='*.py')

    runner = HtmlTestRunner.HTMLTestRunner(stream=fp,
                        combine_reports=True,
                        report_title="Informe de pruebas de los procesos de Hércules-RPA", 
                        output=test_dir1)
    # Pruebas de ejecución
    runner.STYLESHEET_TMPL = '<link rel="stylesheet" href="my_stylesheet.css" type="text/css">'
    runner.run(discover)

    print('Finaliza la creación del informe')
    fp.close()  # Cerrar el archivo del informe

