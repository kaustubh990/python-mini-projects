#del keyword in Python is used to delete objects. It can be used to delete variables, items from a list, or keys from a dictionary.
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Alice", 20)
print(student1.name)  # Output: Alice
del student1  # Deleting the student1 object
# print(student1.name)  # This will raise an error because student1 has been deleted


