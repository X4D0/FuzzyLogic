import pandas as pd

def readExcel():
    baca = pd.read_excel(r'Mahasiswa.xls')
    income = baca['Penghasilan'].tolist()
    spending = baca['Pengeluaran'].tolist()
    return income,spending

readExcel()
