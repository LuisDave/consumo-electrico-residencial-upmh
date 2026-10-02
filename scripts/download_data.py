from pathlib import Path
from urllib.request import urlretrieve
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
ZIP_PATH = RAW / "household_power_consumption.zip"
EXTRACT_DIR = RAW / "uci_household_power"
TXT_PATH = EXTRACT_DIR / "household_power_consumption.txt"

URLS = [
    "https://archive.ics.uci.edu/static/public/235/individual+household+electric+power+consumption.zip",
    "https://archive.ics.uci.edu/ml/machine-learning-databases/00235/household_power_consumption.zip",
]

RAW.mkdir(parents=True, exist_ok=True)
EXTRACT_DIR.mkdir(parents=True, exist_ok=True)

if TXT_PATH.exists():
    print(f"Dataset ya disponible: {TXT_PATH}")
    raise SystemExit(0)

last_error = None
for url in URLS:
    try:
        print(f"Descargando desde: {url}")
        urlretrieve(url, ZIP_PATH)
        with ZipFile(ZIP_PATH) as zf:
            zf.extractall(EXTRACT_DIR)
        if TXT_PATH.exists():
            print(f"OK: {TXT_PATH}")
            print(f"Tamaño: {TXT_PATH.stat().st_size/1024**2:.1f} MB")
            break
    except Exception as exc:
        last_error = exc
        if ZIP_PATH.exists():
            ZIP_PATH.unlink(missing_ok=True)
else:
    raise RuntimeError(f"No se pudo descargar el dataset. Último error: {last_error}")
