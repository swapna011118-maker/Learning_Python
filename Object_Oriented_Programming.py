
#
# CLASS AND OBJECT
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hi, I am {self.name}, {self.age} years old"

p1 = Person("Alice", 30)
print(p1.greet())


# INHERITANCE
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def role(self):
        return "Student"

s1 = Student("Bob", 20, "S101")
print(s1.greet(), s1.role())


# ENCAPSULATION
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        return self.__balance

    def get_balance(self):
        return self.__balance

acc = BankAccount(1000)
print(acc.deposit(500))
print(acc.get_balance())


# ABSTRACTION
class Shape:
    def area(self):
        pass


# POLYMORPHISM
class Rectangle(Shape):
    def __init__(self, l, w):
        self.l = l
        self.w = w

    def area(self):
        return self.l * self.w

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r * self.r

shapes = [Rectangle(4, 5), Circle(3)]
for s in shapes:
    print(s.area())


# DUCK TYPING
class Dog:
    def speak(self):
        return "Woof"

class Cat:
    def speak(self):
        return "Meow"

class Car:
    def speak(self):
        return "Vroom"

things = [Dog(), Cat(), Car()]
for t in things:
    print(t.speak())


# CLASS METHOD AND STATIC METHOD
class MathTools:
    factor = 2

    @classmethod
    def multiply(cls, x):
        return x * cls.factor

    @staticmethod
    def add(a, b):
        return a + b

print(MathTools.multiply(5))
print(MathTools.add(3, 4))


# COMPOSITION
class Engine:
    def start(self):
        return "Engine started"

class Vehicle:
    def __init__(self):
        self.engine = Engine()

    def run(self):
        return self.engine.start()

v = Vehicle()
print(v.run())


# RECURSION
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))


# RECURSION (FIBONACCI)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))
