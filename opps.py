'''objectname = classname(arguments)
'''#how to make object
# class myclass:
#     x=5
#     y=10.5
# p1=myclass()
# p1=myclass()
# # print(p1.x)
# print(myclass)
class tu:
    # name=input("your name ")
    uni="LPU"
    Pincode=14441
x=tu()
x1=tu()
# print(x1.uni,"pincode is ",x.Pincode)    
# class ttu:


# q=ttu()
# print(q)    

class _class:
    def set(self,name,section,marks):
        self.name=name
        self.section = section
        self.marks=marks
    def get(self):
        print("Name: "+self.name,"Section: "+self.section,"Marks: "+self.marks,sep="\n")

Anik = _class()
Himanshu = _class()
Amrit = _class()

# name = input("Your Name: ")
# sec = input("Your Section: ")
# marks =input("Your Marks: ")
# n="Himanshu"
# c="K23TU"
# m="100"
# Anik.set(name,sec,marks)#Agar value agalg hai tho hi value different aana wali hai
# Himanshu.set(n,c,m)
# Amrit.set(name,sec,marks)

# Anik.get()
# Himanshu.get()


class HI:
    def __init__(self,name,money,power):
        self.name=name
        self.money=money
        self.power = power
    

n=input("Your Name? ")
m=int(input("Cash your have? "))
p=input("Your power in percentage? ")

obj=HI(n,m,p)









