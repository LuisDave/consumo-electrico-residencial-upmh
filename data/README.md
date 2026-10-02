# Datos

Este proyecto utiliza el conjunto **Individual Household Electric Power Consumption** de UCI Machine Learning Repository.

- Cobertura: 16 de diciembre de 2006 a 26 de noviembre de 2010.
- Registros: 2,075,259 mediciones por minuto.
- Variables originales: 9.
- Archivo descomprimido: `household_power_consumption.txt` (aprox. 126.8 MB).
- DOI: <https://doi.org/10.24432/C58K54>.
- Licencia: CC BY 4.0.

Para descargar y extraer el archivo oficial, ejecute desde la raíz del proyecto:

```bash
python scripts/download_data.py
```

El archivo se guarda en `data/raw/uci_household_power/` y está excluido del control de versiones. Las tablas de resultados incluidas en `processed/` se generan a partir de ese archivo mediante el notebook.
