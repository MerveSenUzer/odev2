sayi=int(input("Lütfen bir sayı giriniz:"))
j=0

for i in range(2,sayi):
    if (sayi % i ==0):
        j=j+1
if (j==0) and (sayi!=1):
    print("Sayınız Asaldır")
elif (j==0) and (sayi==1):
    print("Geçersiz.Lütfen yeni bir sayı giriniz.")
else:
    print("Sayınız Asal Değildir")
   