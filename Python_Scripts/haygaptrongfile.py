#.lower() chuyen ve chuoi thuong
#.capitalize() chu hoa dau dong

f=open('countries.txt')
country={}  #Dict
suggest=[] #List
for line in f:
     line=line.rstrip().split(',')
     dong1=line[0].lower()
     dong2=line[1]
     country[dong1] = dong2   #{"Abkhazia":"Sukhumi"} like this
     suggest.append(dong1)
city=input('Nhap ten 1 quoc gia: ').lower()
try:
     if(country[city]):
          print ('Thu do cua',city.capitalize(),'la:',country[city])
except:
     print ('\nRat tiec!! ten nuoc khong co trong danh sach!!!\nSau day la 1 so goi y \n')
     for dong1 in suggest:
          if city in dong1:
               print (dong1)