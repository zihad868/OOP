from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass # implements subclass 

class Dog(Animal):
    def make_sound(self):
        return 'Woof!'

class Cat(Animal):
    def make_sound(self):
        return 'Meow'

cat = Cat()

print(cat.make_sound())