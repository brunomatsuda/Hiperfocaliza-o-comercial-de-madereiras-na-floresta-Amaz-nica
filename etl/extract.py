import pandas as pd
from config import PATH_RAW_DATA, CSV_ENCODING, CSV_SEPARATOR, NA_MARKERS


raw_data = PATH_RAW_DATA
df = pd.read_csv(PATH_RAW_DATA, encoding=CSV_ENCODING, sep=CSV_SEPARATOR, na_values=NA_MARKERS)