from abc import ABC, abstractmethod
class AbsClass(ABC):
    def print(self,x):
        print("Value passed is", x)
    @abstractmethod
    def task(self):
        print("We are inside abstract method")
class test_class(AbsClass):
    def task(self):
        print("We are inside test class")
obj1=test_class()
obj1.print(5)
obj1.task()