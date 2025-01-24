class sekil():
    def _init_(self,genislik,yukseklik):
        self.genislik=genislik
        self.yukseklik=yukseklik

class dikdortgen(sekil):
    def alan_hesapla(self):
        return self.genislik*self.yukseklik
        
       
class kare(sekil):
    def _init_(self, kenar):
        super()._init_(kenar,kenar)
    def alan_hesapla(self):
        return self.genislik*self.yukseklik
# Örnekler oluşturma
# Dikdörtgen örneği
dikdortgen = dikdortgen(4, 5)
dikdortgen_alani = dikdortgen.alan_hesapla()
print(f"Dikdörtgenin alanı: {dikdortgen_alani}")

#kare ornegi
kare = kare(3)
kare_alani = kare.alan_hesapla()
print(f"Karenin alanı: {kare_alani}")