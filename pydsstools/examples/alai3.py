from datetime import datetime
from pydsstools.heclib.dss import HecDss
from pydsstools.core import TimeSeriesContainer, UNDEFINED

import pandas as pd

dss_file = r"f:\varie\dss\xga_risultati.dss"
excel_file = r"..\data_xga\risultati.xlsx"
dss_file = r"f:\varie\dss\xga_pluvio.dss"
excel_file = r"..\data_xga\pluvio_dettaglio.xlsx"


def read_xls():
    _df = pd.read_excel(excel_file, index_col=0)
    start = _df.index[0]
    _startDateTime = start.strftime("%d%h%Y %H:%M:%S").upper()
    print(_startDateTime)
    return _df, _startDateTime


def genera_path(codice):
    tipo_a = "pluvio"
    anno_b = "2013"
    codice_c = codice
    col_d = "d"
    intervallo_e = "15MINUTES"
    intervallo_e = "1MINUTES"
    pathname = f"/{tipo_a}/{anno_b}/{codice_c}/{col_d}/{intervallo_e}/FIXED/"
    return pathname


def write_to_dss(pathName, inizio, valori):
    with HecDss.Open(dss_file, version=6) as fid:
        pathname = f"/xga/pluvio/anno//15m/FIXED/"
        pathname = pathName
        tsc = TimeSeriesContainer()
        tsc.pathname = pathname
        tsc.startDateTime = "01GEN2013 00:00:00"
        tsc.startDateTime = inizio
        tsc.units = "MM"
        tsc.type = "PER-CUM"
        tsc.interval = 15
        tsc.interval = 1
        tsc.values = valori
        tsc.numberValues = len(tsc.values)
        #fid.deletePathname(tsc.pathname)
        fid.put_ts(tsc)


def fai(quanti):
    _df, _startDateTime = read_xls()

    colonne = _df.columns
    if quanti > 0:
        colonne = _df.columns[0:quanti]

    for colonna in colonne:
        pathName = genera_path(colonna)
        valori = _df[colonna].values
        write_to_dss(pathName, _startDateTime, valori)
        print(pathName,_startDateTime)

fai(0)
