import pandas as pd

def readExcel():
    baca = pd.read_excel(r'Mahasiswa.xls')
    return print(baca)

readExcel()
