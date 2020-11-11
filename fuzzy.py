import pandas as pd

# Read Excel file using Pandas and return in lists
def readExcel():
    baca = pd.read_excel(r'Mahasiswa.xls')
    income = baca['Penghasilan'].tolist()
    spending = baca['Pengeluaran'].tolist()
    return income,spending

def writeExcel(data):
    df = pd.DataFrame(data) 
    writer = pd.ExcelWriter('Bantuan.xls')
    df.to_excel(writer, sheet_name ='Sheet1')
    writer.save()
    print("Bantuan.xls is Done")

# Fuzzification
## Linguistic
def linguistic(a,b,c,d):
    return (a-b)/(c-d)
    
## Income Classification
def pendapatan(penghasilan):
    if (3<=penghasilan<=5):
        l = 1
        m = 0
        h = 0
    elif (5<penghasilan<7):
        l = linguistic(7,penghasilan,7,5)
        m = linguistic(penghasilan,5,7,5)
        h = 0
    elif (7<=penghasilan<=9):
        l = 0
        m = 1
        h = 0
    elif (9<penghasilan<11):
        l = 0
        m = linguistic(11,penghasilan,11,9)
        h = linguistic(penghasilan,9,11,9)
    elif (11<=penghasilan<=25):
        l = 0
        m = 0
        h = 1
    return l,m,h

## Spending Classification
def pengeluaran(keluaran):
    if (2<=keluaran<=5):
        low = 1
        mid = 0
        high = 0
    elif (5<keluaran<6):
        low = linguistic(6,keluaran,6,5)
        mid = linguistic(keluaran,5,6,5)
        high = 0
    elif (6<=keluaran<=8):
        low = 0
        mid = 1
        high = 0
    elif (8<keluaran<10):
        low = 0
        mid = linguistic(10,keluaran,10,8)
        high = linguistic(keluaran,8,10,8)
    elif (10<=keluaran<=20):
        low = 0
        mid = 0
        high = 1
    return low,mid,high

# Inferensi
def FR(l,m,h,low,mid,high):
    if(0<l<=1 and 0<low<=1):
        yes = l
        no = 0
    elif (0<l<=1 and 0<mid<=1):
        yes = l
        no = 0
    elif (0<l<=1 and 0<high<=1):
        yes = l
        no = 0
    elif (0<m<=1 and 0<low<=1):
        yes = 0
        no = m
    elif (0<m<=1 and 0<mid<=1):
        yes = 0
        no = m
    elif (0<m<=1 and 0<high<=1):
        yes = m
        no = 0
    elif (0<h<=1 and 0<low<=1):
        yes = 0
        no = h
    elif (0<h<=1 and 0<mid<=1):
        yes = 0
        no = h
    elif (0<h<=1 and 0<high<=1):
        yes = h
        no = 0
    return yes,no

# Defuzzification
def sugeno(yes,no):
    batasterima = 80
    batastolak = 50
    jumlah = yes+no
    return (yes*batasterima)+(no*batastolak)/jumlah
    
#MAIN-----
hasil = []
n = 1
income,spending = readExcel()
for j in range(100):
    # Fuzzification Process
    l,m,h = pendapatan(float(income[j]))
    low,mid,high = pengeluaran(float(spending[j]))
    #print("lmh : ",l,m,h)
    #print("lowmidhigh : ",low,mid,high)
    #Inference Process
    yes,no = FR(l,m,h,low,mid,high)
    #print("Y : ",yes," N : ",no)
    # Defuzzification Process
    sugen = sugeno(yes,no)
    print("sugeno ke-",j," : ",sugen)
    #print("====================")
    if(sugen>=70 and n<=20):
        #print("ke-",j," : ",yes,no)
        hasil.insert(n,j)
        n += 1
print(hasil)
writeExcel(hasil)
