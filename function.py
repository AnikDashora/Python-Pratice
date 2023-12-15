def calculator():
    x,z,y=int(input("value of x: ")),input("oppration: "),int(input("Value of y: "))
    if z=='+':
        print(f"{x}+{y} =",add(x,y))
    if z=='-':
        print(f"{x}-{y} =",sub(x,y))
    if z=="*":
        print(f"{x}x{y}=",mul(x,y))
    if z=="/":
        print(f"{x}/{y} =",divide(x,y))
    if z== "p" or z== "^" :
        print(f"{x}^{y} =",expo(x,y))   
    else:
        print("Error")    

def add(x,y):
    return (x+y) 

def sub(x,y):
    return (x-y)

def mul(x,y):
    return (x*y)

def divide(x,y):
    return (x/y)

def expo(x,y):
    return x**y



# def add(x,y):
#     print(x+y)




calculator()
# add(int(input("pick")),int(input("pick")))

# def result(a=1,b=2,c=3,d=4,f=5):
#     print(a+b+c+d+f)

# result()
# result(int(input("pick")),int(input("pick")),int(input("pick")),int(input("pick")),int(input("pick")))



# def hello(name):
#     print("hello",name)