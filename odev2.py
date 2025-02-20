# Görev 1: Kullanıcıdan iki sayı alıp işlemleri gerçekleştirme

sayi1 = float(input("Birinci sayıyı girin: "))
sayi2 = float(input("İkinci sayıyı girin: "))

print(f"Toplama: {sayi1} + {sayi2} = {sayi1+ sayi2}")
print(f"Çıkarma: {sayi1} - {sayi2} = {sayi1- sayi2}")
print(f"Çarpma: {sayi1} * {sayi2} = {sayi1* sayi2}")
print(f"Bölme: {sayi1} / {sayi2} = {sayi1/ sayi2 if sayi2 != 0 else 'Tanımsız'}")
print(f"Mod alma: {sayi1} % {sayi2} = {sayi1% sayi2}")
print(f"Üs alma: {sayi1} ** {sayi2} = {sayi1** sayi2}")
print()

# Görev 2: 1’den kullanıcının girdiği sayıya kadar olan sayıların toplamı

n = int(input("Bir sayı girin: "))
total = sum(range(1, n+1))
print(f"1'den {n}'e kadar olan sayıların toplamı: {total}")
print()

# Görev 3: 1 ile 100 arasındaki çift sayıları ekrana yazdırma

print("1 ile 100 arasındaki çift sayılar:")
for i in range(2, 101, 2):
    print(i, end=" ")
print()
print()

# Görev 4: Kullanıcıdan alınan metni ters çevirme

text = input("Bir metin girin: ")
reversed_text = "".join(reversed(text))  # Döngü ile ters çevirme
print(f"Girilen metnin tersi: {reversed_text}")