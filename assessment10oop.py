# 1 Create a Car class with attributes like brand, model, and speed, and methods to accelerate/brake.

# class Car:
#     def __init__(self, brand, model, speed=0):
#        self.brand = brand
#        self.model = model
#        self.speed = speed
       
#     def accelerate(self, value):
#         self.speed += value 
#         print("Speed after accelerating:", self.speed)
        
#     def brake(self, value):
#         self.speed -= value 
#         if self.speed < 0:
#            self.speed = 0
#         print("Speed after breaking:", self.speed)
        
        
# car = Car("Toyota", "Camry")
# car.accelerate(60)
# car.brake(20)
    

                   
# 2 Create a BankAccount class with deposit and withdraw methods.
class Car:
    def __init__(self, brand, model, speed=0):
        self.brand = brand
        self.model = model
        self.speed = speed

    def accelerate(self, value):
        self.speed += value
        print(f"Accelerated: Current speed is {self.speed} km/h")

    def brake(self, value):
        self.speed = max(0, self.speed - value)
        print(f"Braked: Current speed is {self.speed} km/h")
        
car = Car("Toyota", "Corolla")
car.accelerate(50)
car.brake(20)
       
        
# # 2 class BankAccount:
#     def __init__(self, balance=0):
#         self.balance = balance
        
#     def deposit(self, amount):
#             self.balance += amount
#             print("Balance after deposit:", self.balance)
            
#     def withdraw(self, amount):
#                 if amount <= self.balance:
#                     self.balance -=amount
#                     print("Balance after withdrawal:", self.balance)
#                 else:
#                     print("Insufficient  balance")
                    

# account = BankAccount(1000)
# account.deposit(500)
# account.withdraw(300)           
                    
## 3 Create a Student class with a method to calculate average marks.

# class Student:
#     def __init__(self, name,marks):
#         self.name = name
#         self.marks = marks
        
#     def calculate_average(self):
#         return sum(self.marks ) / len(self.marks)
    
# Student = Student("Henil", [80, 90,85])
# print("Average Marks:", Student.calculate_average())
 
#$ 4 Create a Rectangle class with methods to find area and perimeter.

# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
        
#     def area(self):
#         return self.length* self.width
    
#     def perimeter(self):
#         return 2* (self.length + self.width)
    
    
# rect = Rectangle(10,5) 
# print("Rectangle Area:", rect.area())
# print("Rectangle Perimeter:",rect.perimeter())
       


## 5 Create an Employee class that displays salary details.

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
        
#     def display_salary(self):
#         print("Employee Name:",self.name)
#         print("Salary:", self.salary)
        
# emp = Employee("Meet", 50000)
# emp.display_salary()
            

## 6 Create a Book class to store title, author, and price, and display details.

# class Book:
#     def __init__(self, title, author, price):
#         self.title = title
#         self.author = author
#         self.price = price
        
#     def display_details(self):
#         print("Title:", self.title)
#         print("Author:", self.author)
#         print("Price:",self.price)
        
# book = Book("Python Programming","Guido",450)
# book.display_details()

            
## 7 Create a Circle class to find area and circumference.

# class Circle:
#     def __init__(self, radius):
#      self.radius = radius
     
#     def area(self):
#         return 3.14 * self.radius * self.radius
#     def circumference(self):
#         return 2 * 3.14 * self.radius
    
# circle = Circle(7)
# print("Circle Area:",circle.area())
# print("circle.circumference", circle.circumference())

      
    
## 8 Create a Laptop class with a method to apply discounts on price. 

# class Laptop:
#     def __init__(self, brand, price):
#         self.brand = brand
#         self.price = price
        
#     def apply_discount(self, percent):
#         discont = (self.price * percent) / 100
#         self.price -= discont
#         print("Price after discount:", self.price)
        
# laptop = Laptop("Dell", 60000)
# laptop.apply_discount(10)

            
# # 9 Create a Flight class with seat booking functionality.

# class Flight:
#     def __init__(self, flight_number, seats):
#         self.flight_number = flight_number
#         self.seats = seats
        
#     def book_seat(self):
#         if self.seats > 0:
#            self.seats -= 1
#            print("Seat booked successfully")
#         else:
#            print("No seat available")
            
            
# flight = Flight("AI101", 2)
# flight.book_seat()
# flight.book_seat()
# flight.book_seat()
            
                 

# # 10 Create a Shop class with a method to add and list products.	

# class Shop:
#     def __init__(self):
#         self.product = []
    
#     def add_product(self, name, price):
#         product = {
#             "name": name,
#             "price": price
#         }     
#         self.product.append(product)
        
#     def list_product(self):
#         if not self.product:
#             return "NO products available."
        
#         return[
#             f"{product['name']} - ${product['price']:.2f}"
#             for product in self.product
#         ]
        
        
# shop = Shop()
# shop.add_product("Apple",0.99)
# shop.add_product("Bread",2.50)

# for item in shop.list_product():
#  print(item)

        
        
            