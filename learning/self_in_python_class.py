# class Person:
#     def __init__(self, name, age):
#         self.name = name  # Assigning to the instance attribute
#         self.age = age

#     def greet(self):
#         return f"Hello, my name is {self.name} and I am {self.age} years old."

# # Create an instance of the Person class
# person1 = Person("Alice", 30)
# print(person1.greet())

class Counter:
    def __init__(self):
        self.count = 0  # Initialize the counter

    def increment(self):
        self.count += 1  # Modify the instance attribute using self

    def get_count(self):
        return self.count

# Create an instance and use the methods
counter = Counter()
counter.increment()
counter.increment()
counter.increment()
print(counter.get_count())  # Output: 2


        

    