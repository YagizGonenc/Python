# Hipotenus hesaplama
a = int(input("Birinci Sayı:"))
b = int(input("İkinci Sayı:"))
c = int(a**2 + b**2)**0.5
c

# Not ortalaması alma
a = int(input("Birinci not:"))
b = int(input("İkinci not:"))
c = int(input("Üçüncü Not:"))
d = float((a + b + c) / 3)
if d >= 60:
    print("Not ortalamanız:"), print(d)
    print("Tebrikler Geçtin")
elif d < 60:
    print("Not ortalamanız:"), print(d)
    print("Malesef Kaldı")

# Fiyat karşılaştırma
a = int(input("Market meyvesi fiyatı girin:"))
b = int(input("Pazar meyvesi fiyatı girin :"))
c = a-b
if c<0 :
    print(-c,"tl daha uygun"),print("Market daha uygun")
elif c>0 :
    print(c,"tl daha uygun"),print("Pazar daha uygun")

    # Çemberde çevre hesaplama
    a = int(input("yarı çap:"))
    b = float(input("pi sayısı:"))
    c = (2 * a * b)
    c

    # Çemberde alan hesaplama
    a = int(input("yarı çap:"))
    b = float(input("pi sayısı:"))
    c = (b * a ** 2)
    c