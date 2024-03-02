#!/usr/bin/env python3


"""class Dog:  # class
    def __init__(self, name, favourite_toy="Any"):  # constructor __init__ method
        self.name = name
        self.favourite_toy = favourite_toy

    def bark(self):  # bark method
        print("Woof!")

    def adopt(self, owner_name):
        self.owner = owner_name


fido = Dog("Fido")  # created an instance of the Dog class named Fido
print(fido.name)  # access the name attribute of the fido object and print it

fido.owner = "Sophie"
print(fido.owner)

snoopy =Dog('Snoopy', 'Tennis Ball')
print(snoopy.favourite_toy)"""


class Dog:
    def __init__(self, name, breed="Mutt"):
        self.name = name
        self.breed = breed


Tom = Dog("Tom", "Labrador Retriever")
print(Tom.name, Tom.breed) 