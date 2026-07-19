# %% book class
class book:
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
    def describe(self):
        print(f"{self.title} is a book written by {self.author} with {self.pages} pages")

book1 = book("Oromi", "Bealu Girma", 987)
book1.describe()
# %% Product class
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def restock(self, n):
        self.quantity += n

    def sell(self, n):
        self.quantity -= n
p = Product("Paracetamol", 25, 100)
p.restock(20)
p.sell(5)
print(p.quantity)


# %% Make it private
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.__quantity = quantity

    @property
    def quantity(self):
        return self.__quantity

    def restock(self, n):
        self.__quantity += n

    def sell(self, n):
        self.__quantity -= n
  
    @quantity.setter
    def quantity(self, value):
     if value < 0:
        raise ValueError("Quantity cannot be negative")
     self.__quantity = value

p1 = Product("Paracetamol", 25, 100)
p2 = Product("Ibuprofen", 30, 50)
p3 = Product("Amoxicillin", 40, 75)

p1.restock(20)   # only change p1

print(p1.quantity)  # expect 120 — changed
print(p2.quantity)  # expect 50  — unaffected
print(p3.quantity)  # expect 75  — unaffected

# %%
