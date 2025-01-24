#question 1

class Rectangle:
    def __init__(self,genislik, yukseklik):
        self.genislik = genislik
        self.yukseklik = yukseklik
    def alan(self):
        return self.genislik * self.yukseklik
    def cevre(self):
        return (self.genislik + self.yukseklik) * 2
hesap = Rectangle(5,7)
print("Rectangle Alanı: ", hesap.alan())
print("Rectangle cevre: " , hesap.cevre())


#question 2

class School:
    def __init__(self, name, foundation_year):
        self.name = name 
        self.foundation_year = foundation_year
        self.students = []
        self.teachers = {}
        
    def add_new_student(self, student_name, student_class):
        self.students.append({"name": student_name, "class": student_class})
        print(f"Student {student_name} added to class {student_class}.")

    def add_new_teacher(self, teacher_name, branch):
        self.teachers[teacher_name] = branch
        print(f"Teacher {teacher_name} added with branch {branch}.")

    def view_student_list(self):
        print("List of Students:")
        for student in self.students:
            print(f"Name: {student['name']}, Class: {student['class']}")

    def view_teacher_list(self):
        print("List of Teachers:")
        for teacher_name, branch in self.teachers.items():
            print(f"Name: {teacher_name}, Branch: {branch}")


school = School("Kazım Karabekir", 1998)


school.add_new_student("İlhan", "10th Grade")
school.add_new_student("Kagan", "11th Grade")


school.add_new_teacher("Mr. Akdeniz", "Mathematics")
school.add_new_teacher("Ms. Karadeniz", "Physics")


school.view_student_list()
school.view_teacher_list()


# Soru-3
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

# Soru-4
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"Marka: {self.make}, Model: {self.model}, Yıl: {self.year}"

class OffRoadVehicle(Vehicle):
    def __init__(self, make, model, year, four_wheel_drive):
        super().__init__(make, model, year)
        self.four_wheel_drive = four_wheel_drive

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, 4 Çeker: {self.four_wheel_drive}"

class SportsCar(Vehicle):
    def __init__(self, make, model, year, max_speed):
        super().__init__(make, model, year)
        self.max_speed = max_speed

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Maksimum Hız: {self.max_speed} km/s"

suv = OffRoadVehicle("Toyota", "Land Cruiser", 2021, True)

sports_car = SportsCar("Ferrari", "488 Spider", 2022, 330)

print(suv.display_info())
print(sports_car.display_info())

# Soru-5

class Musteri:
    def __init__(self, isim, soyad, tc_identification, telefon):
        self.isim = isim
        self.soyad = soyad
        self.tc_identification = tc_identification
        self.telefon = telefon

    def display_information(self):
        print("Müşteri Bilgileri:")
        print(f"Ad: {self.isim}")
        print(f"Soyad: {self.soyad}")
        print(f"TC Kimlik No: {self.tc_identification}")
        print(f"Telefon: {self.telefon}")


class Hesap(Musteri):
    def __init__(self, musteri, hesap_numarasi, bakiye=0):
        super().__init__(musteri.isim, musteri.soyad, musteri.tc_identification, musteri.telefon)
        self.hesap_numarasi = hesap_numarasi
        self.bakiye = bakiye

    def deposit(self, amount):
        if amount > 0:
            self.bakiye += amount
            print(f"{amount} TL hesaba yatirildi. Güncel bakiye: {self.bakiye} TL")
        else:
            print("Yatirilacak miktar pozitif bir sayi olmalidir.")

    def money_check(self, amount):
        if amount > self.bakiye:
            print("Hesapta yeterli bakiye bulunmuyor. İşlem gerçekleşmedi.")
        elif amount <= 0:
            print("Çekilecek miktar pozitif bir sayi olmalidir.")
        else:
            self.bakiye -= amount
            print(f"{amount} TL hesaptan çekildi. Güncel bakiye: {self.bakiye} TL")

    def display_balance(self):
        print(f"Hesap Bakiyesi: {self.bakiye} TL")


# Müşteri oluşturma
musteri1 = Musteri("Okay", "Dost", "12345678901", "05351234567")

# Hesap oluşturma ve müşteri bilgilerini ekleme
hesap1 = Hesap(musteri1, "TR123456789", 1000)  # Başlangıç bakiyesi 1000 TL

# Müşteri bilgilerini görüntüleme
hesap1.display_information()

# Hesap işlemleri
hesap1.display_balance()
hesap1.deposit(500)  # 500 TL yatır
hesap1.money_check(300)  # 300 TL çek
hesap1.money_check(1500)  # Yetersiz bakiye kontrolü
hesap1.display_balance()
