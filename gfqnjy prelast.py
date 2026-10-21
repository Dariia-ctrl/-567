book_dist = {
    "title": "Кобзар",
    "author": "Тарас Шевченко",
    "copies": 15
}
print(book_dist["title"])

class Book:
    def __init__(self, title, price, copies): #
        self.title = title
        self.price = price
        self.copies = copies
    def available(self):
        return self.copies > 0

book1 = Book("Кобзар", 450, 15)
book2 = Book("Лісова пісня", 500, 0)
print("Перша:" , book1.title, book1.price)
print("Перша:" , book2.title, book2.price)

print(f'Кобзар доступний: {book1.available()}')
print(f'Лісова пісня доступна: {book2.available()}')

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def perimetr(self):
        return 2 * (self.width +  self.height)
    def area(self):
        return self.width * self.height

    def info(self):
        print(f'Розміри прямокутника {self.width}*{self.height}')
        print(f'S={self.area()}')
        print(f'P={self.perimetr()}')

a = int(input("Введіть ширину прямокутника"))
b = int(input("Введіть висоту прямокутника"))
rectangle = Rectangle(a, b)
rectangle.info()