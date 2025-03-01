import random

veri = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

parola_uzunlugu = int(input("Lütfen parola uzunluğunu giriniz: \n "))

parola = ""

for _ in range(parola_uzunlugu):
    parola += random.choice(veri)

print(parola)

