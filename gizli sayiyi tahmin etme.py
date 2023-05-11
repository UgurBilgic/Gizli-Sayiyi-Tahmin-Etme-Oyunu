gizli_numara = 7                #gizli bir sayı oluşturulur ve değer verilir
tahmin_sayısı = 0               #tahmin sayısı oyun başlangıcında olmadığı için 0 a eşitlenir
tahmin_limiti = 3               #kullanıcının maksimum 3 tahmin hakkı vardır 

while tahmin_sayısı < tahmin_limiti:    #tahmin limiti ve sayısı karşılaştırılır
    tahmin = input("Tahmininiz: ")
    tahmin_sayısı += 1
    if int(tahmin) == gizli_numara:     #tahmin ve gizli numara karşılaştırılır
        print("Bravo, bildiniz")
        break
    elif int(tahmin) != gizli_numara:   #tahmin ve gizli numara karşılaştırılır
        print("Tahmininiz yanlış")
    else:                               #3 denemeden sonra bu kod satırı çalışır
        print("Gizli numarayı bilemediniz :(")
        
input("Çıkmak için ENTER'a basınız")