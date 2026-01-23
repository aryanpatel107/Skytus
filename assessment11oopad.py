import math

# 1. Create a base class Animal and subclasses Dog and Cat
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} says Woof!")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} says Meow!")


dog = Dog("Buddy")
cat = Cat("Whiskers")
dog.speak()  
cat.speak()  


# 2. Create a class hierarchy for Vehicle → Car → ElectricCar.

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def fuel_type(self):
        print(f"{self.brand} uses fuel")

class Car(Vehicle):
    def fuel_type(self):
        print(f"{self.brand} uses petrol or diesel")

class ElectricCar(Car):
    def fuel_type(self):
        print(f"{self.brand} uses electricity")


v = Vehicle("Generic Vehicle")
c = Car("Toyota")
e = ElectricCar("Tesla")
v.fuel_type()
c.fuel_type()
e.fuel_type()
 
# 3 Implement method overriding in a base and derived class.
 
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def fuel_type(self):
        print(f"{self.brand} uses fuel")

class Car(Vehicle):
    def fuel_type(self):
        print(f"{self.brand} uses petrol or diesel")

class ElectricCar(Car):
    def fuel_type(self):
        print(f"{self.brand} uses electricity")


v = Vehicle("Generic Vehicle")
c = Car("Toyota")
e = ElectricCar("Tesla")
v.fuel_type()
c.fuel_type()
e.fuel_type()


# 4 Demonstrate multiple inheritance with two parent classes.


class Father:
    def skills(self):
        print("Father has gardening skills")

class Mother:
    def skills(self):
        print("Mother has cooking skills")

class Child(Father, Mother):
    pass


child = Child()
child.skills()  

# 5 Create a polymorphic function that works with different shapes.

class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


def print_area(shape):
    print(f"Area: {shape.area():.2f}")


r = Rectangle(5, 10)
c = Circle(7)
print_area(r)
print_area(c)


# 6 Bank System with SavingsAccount and CurrentAccount

class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}, Balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}, Balance: {self.balance}")
        else:
            print("Insufficient balance")

class SavingsAccount(BankAccount):
    def add_interest(self, rate):
        self.balance += self.balance * rate / 100
        print(f"Interest added: Balance: {self.balance}")

class CurrentAccount(BankAccount):
    def overdraft_limit(self):
        return 5000


savings = SavingsAccount("S001", 1000)
savings.deposit(500)
savings.add_interest(5)

current = CurrentAccount("C001", 2000)
current.withdraw(2500)  


# 7 Create a polymorphic function that works with different shapes.


class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be positive")


p = Person("Alice", 25)
print(p.get_name())
p.set_age(30)
print(p.get_age())


# 8 Create a Teacher and Student class to show inheritance.

class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def display_info(self):
        print(f"Teacher: {self.name}, Subject: {self.subject}")

class Student(Teacher):
    def __init__(self, name, subject, grade):
        super().__init__(name, subject)  # Using super()
        self.grade = grade

    def display_info(self):
        print(f"Student: {self.name}, Subject: {self.subject}, Grade: {self.grade}")


teacher = Teacher("Mr. Smith", "Math")
student = Student("Alice", "Math", "A")
teacher.display_info()
student.display_info()

# 9 Create a MusicPlayer class and subclass Spotify to override play method.

class MusicPlayer:
    def play(self):
        print("Playing music on a generic music player")
        
class Spotify (MusicPlayer):
    def play(self):
        print("Playing music on spotify app")
        
player = MusicPlayer()
spotify = Spotify()

player.play()
spotify.play()


# 10 Demonstrate the use of super() in inheritance                

class Person:
    def __init__(self, name):
        self.name = name
        print("Person constructor called")

    def show(self):
        print(f"Name: {self.name}")

class Student(Person):
    def __init__(self, name, roll_no):
        super().__init__(name)   # calls parent class constructor
        self.roll_no = roll_no
        print("Student constructor called")

    def show(self):
        super().show()           # calls parent class method
        print(f"Roll No: {self.roll_no}")


s = Student("Alice", 101)
s.show()
        
                                