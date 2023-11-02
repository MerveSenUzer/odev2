sayi=int(input("Lütfen bir sayı giriniz:"))
bolenlerToplami=0
for i in range(1,sayi+1):
    if sayi % i ==0:
        bolenlerToplami += i
if bolenlerToplami == sayi*2:
    print("Mükemmel sayıdır.")
else:
    print("Mükemmel sayı değildir.")