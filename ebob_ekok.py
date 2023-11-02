sayi1=int(input("Lütfen birinci sayıyı giriniz:"))
sayi2=int(input("Lütfen ikinci sayıyı giriniz:"))
if sayi1>sayi2:
    kucuksayi = sayi2
else:
    kucuksayi = sayi1
ebob=0
for i in range(1,kucuksayi+1):
    if (sayi1 % i==0) and (sayi2 %i==0):
        ebob=i

print("EBOB:",ebob)
print("EKOK:",sayi1*sayi2/ebob)