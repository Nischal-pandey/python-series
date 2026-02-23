class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age   # private variable

    def show(self):
        print(f"Name: {self.name}, Age: {self.__age}")

s1 = Student("Nischal", 21)
s1.show()
# s1.__age  # ❌ Cannot access directly (private)