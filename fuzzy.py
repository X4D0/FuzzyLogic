import pandas as pd

# Read Excel file using Pandas and return in lists
def readExcel():
    baca = pd.read_excel(r'Mahasiswa.xls')
    income = baca['Penghasilan'].tolist()
    spending = baca['Pengeluaran'].tolist()
    return income,spending

# Fuzzification
## Income Classification
def pendapatan(penghasilan):
    if (0<=penghasilan<=4):
        l = 1
        m,mh,h = 0
    elif (4<penghasilan<6):
        l = (6-penghasilan)/2
        m = (penghasilan-4)/2
        mh,h = 0
    elif (5<=penghasilan<=10):
        l = 0
        m = 1
        mh,h = 0
    elif (10<penghasilan<12):
        l = 0
        m = (12-penghasilan)/2
        mh = (penghasilan-10)/2
        h = 0
    elif (12<=penghasilan<=16):
        l,m = 0
        mh = 1
        h = 0
    elif (16<penghasilan<18):
        l,m = 0
        mh = (18-penghasilan)/2
        h = (penghasilan-16)/2
    elif (18<=penghasilan<=20):
        l,m,mh = 0
        h = 1
    return l,m,mh,h

## Spending Classification
def pengeluaran(nilai):
    if (0<=nilai<=1):
        low = 1
        mid,midhigh,high = 0
    elif (1<nilai<4):
        low = (4-nilai)/3
        mid = (nilai-1)/3
        midhigh,high = 0
    elif (4<=nilai<=5):
        low = 0
        mid = 1
        midhigh, high = 0
    elif (5<nilai<8):
        low = 0
        mid = (8-nilai)/3
        midhigh = (nilai-5)/3
        high = 0
    elif (8<=nilai<=9):
        low,mid = 0
        midhigh = 1
        high = 0
    elif (9<nilai<11):
        low,mid = 0
        midhigh = (11-nilai)/3
        high = (nilai-9)/3
    elif (11<=nilai<=12):
        low,mid,midhigh = 0
        high = 1
    return low,mid,midhigh,high

# Inferensi
def FR(l,m,mh,h,low,mid,midhigh,high):
    

readExcel()
