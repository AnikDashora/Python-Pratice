# n=int(input("Table of: "))
# for i in range(1,11):
#     z=n*i
#     print(f"{n} x {i} =",z)

# a=12
# b=12
# z=2
# n=int(input("Enter you number: "))
# print(a+b)
# print(n%2)#2th
# x=input("What you feel: ")#4th
# print(type(x))

# q=34#4th
# w=80
# print(q>w)
# print(w<q)


# r=int(input("1st number: "))#5th
# t=int(input("2st number: "))
# print((r+t)/2)

# print(n**2)# 6th

# a='anik'
# b="anik"
# # print(a is b)

# v='this is anik\'s sister'
# print(v)

# for i in range(1,6):
#     for j in range(i):
#         print("*",end="")
#     print()       

# for i in range(6,0,-1):
#     for j in range(i):
#         print("*",end="")
#     print()    
# n="ANIKDASHORA"
# z=len(n)
# for i in range(z):
#     if n[i]=="A" or n[i]=="a":
#         print(n[i])
# print(n[0::3])
# for i in range(0,5):
#     print(5*' *')

# q=int(input("enter number: "))
       
# for i in range (0,q):
#     print(" "*(q-i),end=" ")
#     for j in range(i+1):
#         print(ncr(i,j),end=" ")
#     print()        

# def add(*no):
#     s=0
#     for i in no:
#         s=s+i
#     print(s)        

# # # print(add(1,1))
# # # name=input("name:")
# # # surname=input("surname:")

# # def msg(name="A",surname="D"):
# #     print("hello",name,surname)

# # # msg(name="Anik",surname="Dashora")
# # # msg(surname="Dashora",name="Anik")
# # msg(name="Anik",surname="Dashora")  
# # msg() 
# add(1.5,2,5.5)





# name='Anik Dashora'
# list=list(name)

# # for i in range (len(name)) :
# #     if name[i] =='A':
# #         print(f"There is letter 'A' in name at {i}")

# # print("Good afternoon",name)
# list[6]='A'
# print(list)
# str=''
# for i in range (len(name)):
#     str=str+list[i]
# print(str)    

# s={}
# print(type(s))

# def good_day(name):
#     print("Good Day",name)
# good_day(input("your name: "))    

# def fact(n):
#     if n>=0:
#         if n==0:
#             return 1
#         else:
#             product=n*fact(n-1)
#             return product 
#     else:
#         return "not possible"    

# str=input("Enter: ")
# str1=""
# for i in range(len(str)):
#     str1+= i*str[i]

# print(str1)   
# def table():
#     n=int(input("Enter: "))
#     for i in range(1,11):
#         print(f"{n} X {i} =",n*i)
# table()
# l1=["Harry","sohan","sachin","Rahul"]
# for i in l1:
#     if i[0] == "s":
#         print("hello",i)
#     else:
#         continue        
# n=int(input("enter: "))
# i=1
# while i<=10:
#     print(f"{n} X {i} =",n*i)
#     i+=1


# n=int(input("Enter: "))
# number=[i for i in range(10,21)]
# l=[]
# for i in number:
#     for j in range(1,i+1):
#         if i%j == 0:
#             l.append(j)
#             print(l)
#         else:
#             continue

#     if len(l)>2:
#         print(f"{i} is not prime number")
#     else:
#         print(f"{i} is a prime number")


# def fact(n):
#     if n == 0:
#         return 1
#     else:
#         return n*fact(n-1)
# print(fact(5))    



def max_in_list():
    n=int(input("Number of elements: "))
    l=[]
    for i in range(n):
        l.append(int(input("Enter number: ")))
    print("Max number in list is:",max(l))
# max_in_list()

# n=input("camelcase: ")
# n_new=list(n)
# for i in n_new:
#     if i.isupper():
#         n_new.insert((n_new.index(i)-1),"_")
#     else:
#         continue            

# print(n_new)



# l=input("Enter: ").split(" ")
# print(" ".join(l[::-1]))

target = 10

l=[0,1,2,3,4,5,6,7,8,9,10]

# for i in range(int(len(l)//2)+1):
#     for j in l:
#         if i + j == target:
#             print(f"(i,j) = {(i,j)}")




# str = input("Enter: ")
def is_paramodail(str):

    for i in range(len(str)):
        if str[i] == str[-1*(i+1)]:
            # print("IT IS")
            continue
            
        else:
            # print("It is not a parmodiam")
            break 

    if i+1 == len(str):
        print("IT IS")
    else:
        print("IT IS NOT ")

# is_paramodail("NAMAN")
# is_paramodail("AANIK")



def missing_no(l):
    l.sort()
    l1=[]
    for i in range(len(l)):
        if i+1 == len(l):
            break
        else:
            if l[i+1] - l[i] == 1:
                continue
            else:
                for j in range(l[i]+1,l[i+1]):
                    l1.append(j)
            print(f"IN BETWEEN {l[i]} and {l[i+1]} THE NUMBERS IS/ARE:",end=" ")
            print(*l1,sep=", ")
            l1.clear()        
l=[1,3,5,9,15]    
# missing_no(l)
# 

# t=(1,2,3,4,[5,6,7],8,9)   
# t[4]= 12
# print(t)
# class a:
#     def set(self,name):
#         self.name =name
#     def get(self):
#         print(self.name.upper())

# x=input("Enter: ")
# obj = a()
# obj.set(x)
# obj.get()


n=input("Enter: ")
def parmodam_(n):
    for i in range(len(n)):
        if len(n)//2 == i:
            break
        else:
            if n[i] == n[-1-i]:
                continue
            else:
                break

    if i == len(n)//2:
        print("it is")
    else:
        print("it is not")

def parmodam_1(n):
    str = ""
    for i in range(-1,-1*len(n)-1,-1):
        str += n[i]

    if n == str:
        print("it is")
    else:
        print("it is not")


# parmodam_(n)
# class HELLO(Exception):
#     pass

# for n in range(0,10):
#     try:
#         if n ==7:
#             raise HELLO("HI")
#         prn
#     except HELLO as e:
#         print(n**2)

def perfect_no(n):
    l=[]
    for i in range(1,n):
        if n%i == 0:
            l.append(i)
        else:
            continue
    if sum(l) == n:
        print("IT is")
    else:
        print("Is is not")


# perfect_no(int(n))

import re
# str = "print('hell5o6 wo8rl7d 5768')"
# x= re.findall('[5768][0-9][0-9][0-9]',str)
# print(x)



