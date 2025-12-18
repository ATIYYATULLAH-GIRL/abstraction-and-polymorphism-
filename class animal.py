from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def move(self):
        pass
class Human(Animal):
    def move(self):
        print("I can walk and run.")
class Dog(Animal):
    def move(self):
        print("I can bark")
Ruby=Human()
Ruby.move()
tommy=Dog()
tommy.move()