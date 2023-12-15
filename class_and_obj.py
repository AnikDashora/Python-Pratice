# class TU:
#     name=input("Your Name? ")
#     Age=int(input("Your Age? "))
# obj1 = TU()

# print(obj1.name,obj1.Age,sep="\n")

class STUD:
    branch = "CSE"
    name = "ABCD"
    roll_no = 1230
    def read(self):
        print("READING")

# s1 = STUD()
# s2 = STUD()

# s1.read()

class grandparent:
    def display(self):# This woun't work as display is also defined in another class so the latest definnation will be taking
        print("WE ARE BIGGEST")
    def saying(self):
        print("WE ARE SAYING")

class parent(grandparent):
    def display(self):
        print("PARENT CLASS")
    

class child(parent):
    def show(self):
        print("CHILD CLASS")


c=child() # making a obj
# c.saying()


'''HIERARCHICAL INHERITANCE:'''

class parent:
    def pdisplay(self):
        print("PARENT CLASS")

class child1(parent):
    def child1(self):
        print("CHILD1")

class child2(parent):
    def child2(self):
        print("CHILD2")


c1=child1()
c2=child2()

# c1.pdisplay()
# c2.pdisplay()


# c1.child1()
# c2.child2()


'''MULTIPLE INHERITANCE'''

class father:
    def fdisplay(self):
        print("FATHER")

class mother:
    def mdisplay(self):
        print("MOTHER")

class child(father,mother):
    def cdisplay(self):
        print('CHILD')

c=child()

# c.fdisplay()
# c.mdisplay()
# c.cdisplay()


'''ENCAPSULATION -- WRAPPING OF DATA , WE can make public or private (content)'''

class Encap:
    __a = 10 # private 
    def display(self):
        return("Welcome")

obj = Encap()
# print('obj.a',obj.display(),sep="\n")


'''ABSTRACT CLASS AND METHODS'''
from abc import ABC,abstractmethod

class abd(ABC):
    @abstractmethod #decorator 
    def display(self):
        None

class demo(abd):
    def display(self):
        print("Welcome")

obj = demo()

# obj.display()


'''PLOYMORPHISM ,, OVERLOADING:'''


class mol:
    def a_b(self,a=None,b=None):
        if a != None and b != None:
            print(a,b)
        elif a != None:
            print(a)

o1=mol()

# o1.a_b(a="a")

"""OVERRIDING:"""

class father:
    def Transport(self):
        print("Cycle")



class son(father):
    def Transport(self):
        print("Bike")

o1=son()
# o1.Transport()

class m:
    def getstr(self,n):
        self.n = n
    def setstr(self):
        print(self.n.upper())

n=input("name?")
obj = m()

obj.getstr(n)
obj.setstr()