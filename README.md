# ETABS Automation - Definiciones y Normativa Peruana (NTP)

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![ETABS v20-v22](https://img.shields.io/badge/ETABS-v20%20--%20v22-brightgreen.svg)](https://www.csiamerica.com/products/etabs)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Herramienta modular en Python para la automatización y estandarización del modelado estructural en **CSI ETABS** (v20 a v22) según la normativa técnica peruana:

- **NTP E.060**: Concreto Armado
- **NTP E.030**: Diseño Sismorresistente
- **NTP E.020**: Cargas

Todo el flujo es guiado mediante el archivo [`config.yaml`](./config.yaml), donde se permite adaptar dimensiones, resistencias y combinaciones.

---

## Características Principales

1. **Materiales Estandarizados (E.060/ACI-318)**:
   - Concretos $f'_c = 175, 210, 280\text{ kg/cm}^2$ con módulo de elasticidad exacto:
     $$E_c = 15000 \sqrt{f'_c} \times 10 \quad [\text{Tonf/m}^2]$$
     y curva esfuerzo-deformación no lineal de Mander.
   - Acero de refuerzo longitudinal y transversal Grado 60 ($f_y = 42000\text{ Tonf/m}^2$, $E_s = 2 \times 10^7\text{ Tonf/m}^2$).
2. **Secciones Paramétricas**:
   - Columnas rectangulares (centradas, excéntricas y esquineras).
   - Vigas principales y secundarias.
   - Losas aligeradas unidireccionales (Ribbed) de $h=20\text{ cm}$ (loseta de 5 cm, viguetas de 10 cm espaciadas a 40 cm).
3. **Elementos Estructurales**:
   - Asignación de diafragmas rígidos o semi-rígidos para cada piso del modelo.
   - Registro de etiquetas Pier (`Muro-1`, `Muro-2`, etc.) para muros de corte.
4. **Patrones de Carga y Combinaciones de Diseño**:
   - Renombrado limpio: `Dead` $\to$ `CM` y `Live` $\to$ `CV`.
   - Incorporación de sismo estático `SEx` y `SEy`.
   - 9 combinaciones lineales de diseño normativo y generación automática de la Envolvente.
5. **Fuente de Masa Sísmica (E.030)**:
   - Configuración automatizada de $100\%\text{ CM} + 25\%\text{ CV}$ (Edificaciones Categoría C).

---

## Instalación

Instala las dependencias en tu entorno de Python:
   
   ```bash
   pip install -r requirements.txt
   ```
---

## Modo de Uso

1. **Abre ETABS** y crea un modelo nuevo o abre una plantilla en blanco con tus ejes de cuadrícula y pisos definidos.
2. (Opcional) Ajusta los parámetros deseados en [`config.yaml`](./config.yaml) (por ejemplo, agrega o cambia dimensiones de columnas o resistencias de concreto).
3. **Ejecuta el script principal**:
   
   ```bash
   python main.py
   ```
   
   O especificando una ruta de configuración personalizada:
   
   ```bash
   python main.py ruta/personalizada/config.yaml
   ```
---

## Licencia

Distribuido bajo la Licencia [MIT](./LICENSE).
