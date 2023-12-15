def max_num(a,b,c):
    l=[a,b,c]
    print(max(l))

# max_num(int(input("Enter number1: ")),int(input("Enter number2: ")),int(input("Enter number3: ")))

def list_sum(*numbers):
    l=[*numbers]
    w=0
    for i in l:
        w=w+i
    print(w)
# list_sum(8,2,3,0,7)

def list_mul(*numbers):
    l=[*numbers]
    q=1
    for i in l:
        q=q*i
    print(q)
# list_mul(8,2,3,-1,7)

def str_rev(n):
    str1=""
    for i in range(1,len(n)+1):
        str1=str1+n[(-1)*i]
    print(str1)

# str_rev("1234abcd")

def factorial(n):
    t=1
    for i in range(1,n+1):
        t=t*i
    print(t)

# factorial(5)

def no_in_range(n):
    if int(input("Enter numer1: "))<n<int(input("Enter number2: ")):
        print(f"{n} is in the range")
    else:
        print(f"{n} is not in range")

# no_in_range(5)  


def distict_list(n):
    l=[]
    for i in range(n):
        l.append(int(input("Enter number: ")))
    ul=[]
    for j in l:
        if j not in ul:
            ul.append(j)        
    print(ul)

# distict_list(5)
def distict_list_1(n):
    l=[]
    for i in range(n):
        l.append(int(input("Enter number: ")))
    s=set(l)
    ul=list(s)
    print(ul)
# distict_list_1(7)  
# 
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)  
# print(fact(5))    

def even_list(n):
    l=[]
    evenlist=[]
    for i in range(n):
        l.append(int(input("Enter number: ")))
    for i in l:
        if i%2==0:
            evenlist.append(i)
        else:
            continue 
    print(evenlist)                   
# even_list(10)
def perfrct_number(n):
    l=[]
    for i in range(1,n):
        if n%i==0:
            l.append(i)

    s=sum(l)
    if s==n:
        print("perfect number")
    else:
     print("not a perfect number")
# perfrct_number(6)
def palindorme_str(str):
    rev_str=""
    for i in range(len(str)-1,-1,-1):
        rev_str+=str[i]
    if rev_str==str:
        print("it's a palindorme")
    else:
        print("not a palindorme")

# palindorme_str(input("enter: "))   
str=input("Enter: ")
ch="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in str:
    if i not in ch:
        print("")
