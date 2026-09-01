# Panel de Monitoreo IoT - Iluminación Inteligente

Este proyecto implementa la lógica de control y monitoreo para un sistema inteligente de iluminación de doble zona con detección de presencia.

## 🚀 Estructura del Proyecto

```text
panel-monitoreo-iot/
├── .github/
│   └── workflows/
│       └── ci.yml          # Pipeline de Integración Continua (GitHub Actions)
├── src/
│   └── panel_app/
│       ├── __init__.py
│       └── monitoreo.py    # Lógica principal de sensores y temporizadores
├── tests/
│   ├── __init__.py
│   └── test_monitoreo.py  # Pruebas unitarias e integración con Pytest
├── .gitignore               # Exclusión de archivos innecesarios para Git
├── pytest.ini               # Configuración de rutas de importación para Pytest
└── README.md