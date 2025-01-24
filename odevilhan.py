#question 1
""""
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
"""

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