import pytest
from panel_app.monitoreo import PanelMonitoreoService

def test_encendido_automatico_al_detectar_presencia():
    """CP-I02: Incrementa contador y activa la zona al detectar presencia"""
    servicio = PanelMonitoreoService()
    nuevo_conteo = servicio.incrementar_contador()
    
    assert nuevo_conteo == 1
    assert servicio.obtener_estado_sensores()["zona_a_activa"] == True

def test_decrementar_contador_no_permite_negativos():
    """CP-U02: Si el contador esta en 0, no permite valores negativos"""
    servicio = PanelMonitoreoService()
    resultado = servicio.decrementar_contador()
    
    assert resultado == 0

def test_rechaza_temporizador_invalido():
    """CP-U03: Un temporizador menor o igual a 0 debe lanzar ValueError"""
    servicio = PanelMonitoreoService()
    
    with pytest.raises(ValueError) as exc_info:
        servicio.configurar_temporizador(-5)
        
    assert "El temporizador debe ser mayor a 0 segundos" in str(exc_info.value)