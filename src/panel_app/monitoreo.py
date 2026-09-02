class PanelMonitoreoService:
    def __init__(self):
        self.personas_presentes = 0
        self.zona_a_activa = False
        self.temporizador_segundos = 30

    def incrementar_contador(self):
        self.personas_presentes += 1
        if self.personas_presentes > 0:
            self.zona_a_activa = True
        return self.personas_presentes

    def decrementar_contador(self):
        if self.personas_presentes > 0:
            self.personas_presentes -= 1
        if self.personas_presentes == 0:
            self.zona_a_activa = False
        return self.personas_presentes

    def configurar_temporizador(self, segundos: int):
        if segundos <= 0:
            raise ValueError("El temporizador debe ser mayor a 0 segundos")
        self.temporizador_segundos = segundos
        return self.temporizador_segundos

    def obtener_estado_sensores(self):
        return {
            "personas_presentes": self.personas_presentes,
            "zona_a_activa": self.zona_a_activa,
            "temporizador_segundos": self.temporizador_segundos
        }