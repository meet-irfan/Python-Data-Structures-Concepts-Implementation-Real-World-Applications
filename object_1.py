# -*- coding: utf-8 -*-
"""object-1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1EOd8gz7zK5EmWcsZNyURd9PZyXQikTIi
"""

class Dog:
    species = "Canine"  # Class attribute

    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age  # Instance attribute

# Creating an object of the Dog class
dog1 = Dog("Buddy", 3)

print(dog1.name)
print(dog1.species)