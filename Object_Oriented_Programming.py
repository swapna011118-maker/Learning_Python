#Classes are basically a blueprint of an object that is used to easily create an instance
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."
#Creating an instance of the class
person1 = Person("Alice", 30)
print(person1.greet())  # Output: Hello, my name is Alice and I am 30 years old.
#Inheritance allows a class to inherit attributes and methods from another class
class Student(Person):
    def __init__(self,name,age,student_id):
        super().__init__(name,age)
        self.student_id = student_id
    def study(self):
        return f"{self.name} is studying."
#Creating an instance of the subclass
student1 = Student("Bob", 20, "S12345")
print(student1.greet())  # Output: Hello, my name is Bob and I am 20 years old.
print(student1.study())  # Output: Bob is studying.
#Encapsulation is the concept of restricting access to certain attributes and methods
class BankAccount:
    def __init__(self,account_number,balance):
        self._account_number = account_number  # Not private but allows controlled access
        self.__balance = balance  # Private attribute
    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited: {amount}. New balance: {self.__balance}"
        else:
            return "Deposit amount must be positive."
    def withdraw(self,amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrew: {amount}. New balance: {self.__balance}"
        else:
            return "Insufficient funds or invalid amount."
    def get_balance(self):
        return self.__balance
    #Duck typing is a concept where the type or class of an object is less important than the methods it defines
class Animal:
    def speak(self):
        pass
class Dog(Animal):
    def speak(self):
        return "Woof!"  
class Cat(Animal):
    def speak(self):
        return "Meow!"
#Using duck typing
class Car(Animal):
    def speak(self):
        return "Vroom!"
animals = [Dog(), Cat(), Car()]
for animal in animals:
    print(animal.speak())  # Output: Woof! Meow! Vroom!
#Polymorphism allows methods to do different things based on the object it is acting upon
class Shape:
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius
shapes = [Rectangle(4,5), Circle(3)]
for shape in shapes:
    print(f"Area: {shape.area()}")  # Output: Area of Rectangle and Circle
#Recursion is a programming technique where a function calls itself in order to solve a problem
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
factorial_of_5 = factorial(5)
print(f"Factorial of 5 is: {factorial_of_5}")  #
#Recursion example-2
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
fibonacci_of_6 = fibonacci(6)
