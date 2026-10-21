#1
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)
    def info(self):
        print(self.width, "×", self.height, ": площа =", self.area(), ", периметр =", self.perimeter())

width = float(input("Введіть ширину першого прямокутника: "))
height = float(input("Введіть висоту першого прямокутника: "))
rectangle1 = Rectangle(width, height)

width = float(input("Введіть ширину другого прямокутника: "))
height = float(input("Введіть висоту другого прямокутника: "))
rectangle2 = Rectangle(width, height)

rectangle1.info()
rectangle2.info()

#2

class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        if grade >= 1 and grade <= 12:
            self.grades.append(grade)
        else:
            print("Некоректна оцінка. Введіть число від 1 до 12.")

    def average(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)

    def __str__(self):
        return "ПІБ: " + self.name + ", оцінки: " + str(self.grades) + ", середній бал: " + str(round(self.average(), 2))


name = input("Введіть ПІБ першого учня: ")
student1 = Student(name)

number = int(input("Скільки оцінок у першого учня? "))
for i in range(number):
    grade = int(input("Введіть оцінку: "))
    student1.add_grade(grade)

name = input("Введіть ПІБ другого учня: ")
student2 = Student(name)

number = int(input("Скільки оцінок у другого учня? "))
for i in range(number):
    grade = int(input("Введіть оцінку: "))
    student2.add_grade(grade)

print(student1)
print(student2)

#3
class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []
    def add_grade(self, grade):
        if grade >= 1 and grade <= 12:
            self.grades.append(grade)
        else:
            print("Некорректная оценка. Введите число от 1 до 12.")
    def average(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / (len(self.grades) + 1)
    def __str__(self):
        return "ПІБ: " + self.name + ", оцінки: " + str(self.grades) + ", середній бал: " + str(round(self.average(), 2))

students = []

for i in range(5):
    name = input("Введіть ПІБ учня: ")
    student = Student(name)
    number = int(input("Скільки оцінок у учня? "))
    for j in range(number):
        grade = int(input("Введіть оцінку: "))
        student.add_grade(grade)
    students.append(student)
print("\nУсі учні:")
for student in students:
    print(student)
best_average = students[0].average()
for student in students:
    if student.average() > best_average:
        best_average = student.average()
print("\nУчні з найвищим середнім балом:")
for student in students:
    if student.average() == best_average:
        print(student.name, "-", round(student.average(), 2))

#4
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance = self.balance + amount
            print("Поповнення:", amount)
        else:
            print("Помилка поповнення")
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance = self.balance - amount
            print("Зняття:", amunt)
        else:
            print("Помилка зняття")
    def info(self):
        print("Власник:", self.owner)
        print("Баланс:", self.balance)

owner = input("Введіть ім'я першого власника: ")
balance = float(input("Введіть баланс: "))
account1 = BankAccount(owner, balance)
owner = input("Введіть ім'я другого власника: ")
balance = float(input("Введіть баланс: "))
account2 = BankAccount(owner, balance)

account1.deposit(500)
account1.deposit(-100)
account1.withdraw(200)
account1.withdraw(100000)
account2.deposit(300)
account2.deposit(0)
account2.withdraw(100)
account2.withdraw(-50)

print("Перший рахунок:")
account1.info()
print("Другий рахунок:")
account2.info()
