class PanelMonitoreoService:
    """
    Módulo para atender los requerimientos:
    - RF07: Visualización del estado de sensores IoT
    - RF08: Configuración de parámetros de alerta
    - RF09: Registro y consulta de historial de eventos
    """

    def __init__(self):
        self.configuraciones = {
            "umbral_temperatura": 35.0,
            "estado_alertas": True
        }

    def obtener_estado_sensores(self):
        return {
            "estado_sistema": "OPERATIVO",
            "sensores_activos": 5,
            "ultima_lectura": "OK"
        }

    def actualizar_configuracion(self, nuevo_umbral):
        self.configuraciones["umbral_temperatura"] = nuevo_umbral
        return f"Umbral actualizado exitosamente a {nuevo_umbral}°C"