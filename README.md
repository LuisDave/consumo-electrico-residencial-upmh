# Consumo eléctrico residencial

Análisis estadístico del consumo eléctrico de una vivienda, realizado para la asignatura de **Estadística Aplicada** de la Maestría en Inteligencia Artificial de la Universidad Politécnica Metropolitana de Hidalgo (UPMH).

**Autores:** Luis David Gonzalez Romero y Diego Alberto Ortega Carreto  
**Docente:** Dr. Jaime Aguilar Ortiz  
**Fecha:** octubre de 2026

## Propósito

Caracterizar el consumo eléctrico residencial para identificar su distribución, variabilidad, patrones horarios y episodios de alta demanda. Los resultados se interpretan como evidencia descriptiva de una sola vivienda y se traducen en recomendaciones prudentes de eficiencia energética.

## Datos

El proyecto utiliza el conjunto **Individual Household Electric Power Consumption** de UCI Machine Learning Repository. Contiene 2,075,259 mediciones por minuto, nueve variables originales y observaciones de diciembre de 2006 a noviembre de 2010.

- Página del conjunto de datos: <https://archive.ics.uci.edu/dataset/235/individual+household+electric+power+consumption>
- DOI: <https://doi.org/10.24432/C58K54>
- Licencia de los datos: CC BY 4.0

El archivo de datos bruto no se incluye en el repositorio. Descárguelo con el script incluido antes de ejecutar el análisis.

## Uso rápido

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
# source .venv/bin/activate

pip install -r requirements.txt
python scripts/download_data.py
jupyter lab
```

Abra `notebooks/analisis_consumo_electrico_residencial.ipynb` y ejecute las celdas en orden. El notebook también puede descargar los datos si aún no están disponibles.

## Contenido del análisis

- revisión de la calidad de los datos y tratamiento explícito de valores faltantes;
- variables temporales, perfil horario y comparación por tipo de día;
- medidas de tendencia central, dispersión, posición, sesgo y curtosis;
- distribución de la potencia activa y observaciones inusuales mediante la regla de Tukey;
- serie diaria, medias móviles, perfil mensual y correlaciones de Pearson;
- composición de las submediciones e indicadores para contextualizar hábitos de consumo.

## Resultados destacados

- `Global_active_power`: media de **1.092 kW**, mediana de **0.602 kW**, desviación estándar de **1.057 kW** y sesgo de **1.786**.
- El mayor promedio horario se observa a las **20:00 (1.899 kW)** y el menor a las **04:00 (0.444 kW)**.
- Por la noche, los fines de semana promedian **1.745 kW** frente a **1.439 kW** en días laborables.
- `Global_active_power` se asocia fuertemente con `Global_intensity` (**r ≈ 0.999**) y de forma moderada con `other_active_energy_wh` (**r ≈ 0.701**) y `Sub_metering_3` (**r ≈ 0.639**).

La correlación no implica causalidad; los hallazgos describen el comportamiento de la vivienda estudiada y no se generalizan automáticamente a otros hogares.

## Estructura del proyecto

```text
.
├── data/
│   ├── raw/                 # datos descargados localmente (ignorados por Git)
│   └── processed/           # tablas resumen generadas por el análisis
├── notebooks/
│   └── analisis_consumo_electrico_residencial.ipynb
├── poster/
│   └── cartel.png
├── reports/
│   └── informe_analisis.html
├── scripts/
│   └── download_data.py
├── .gitignore
├── requirements.txt
└── README.md
```

## Referencia de los datos

Hebrail, G., & Berard, A. (2006). *Individual Household Electric Power Consumption* [Dataset]. UCI Machine Learning Repository. <https://doi.org/10.24432/C58K54>
