from model.process.Proceso2.Entities.Evaluaciones.EvaluacionSexenios.EvaluacionSexenio import EvaluacionSexenio
from model.process.Proceso2.Entities.Comites.ComiteCienciasComportamiento import ComiteCienciasComportamiento

class ComiteBiblioteconomiaYDocumentacion(ComiteCienciasComportamiento):
    """
    Comité que evalúa el área de Biblioteconomía y Documentación dentro del comité 7.1.
    """
    def __init__(self, id, evaluador, es_comision: bool = False):
        super().__init__(id, evaluador, es_comision)

    def get_evaluacion_sexenio(self, produccion_cientifica) -> EvaluacionSexenio:
        """
        Método encargado de realizar la baremación del sexenio.
        :param [] produccion_científica: listado de artículos de un investigador.
        :return EvaluacionSexenio evaluación del sexenio.        
        """
        return super().get_evaluacion_sexenio(produccion_cientifica)