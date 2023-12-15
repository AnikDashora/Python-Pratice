# f1 = open("HELLO.txt",'w')
# print(f1.read())

# import os 
# print(os.getcwd()) #path of the file

# f1.write("WELCOME TO PYTHON")

# f1.close()
# f1 =open("HELLO.txt",'r')
# print(f1.read())
# print(f1.tell())


# f1.close()
# f1 = open("HELLO.txt",'r')
# print(f1.read(4))
# print(f1.read())
# f1.close()

# f1 = open("HELLO.txt",'a')

# f1.write(" HOW ARE YOU?")
# f1.close()


# f1=open("HELLO.txt",'r')
# print(f1.read(4))
# f1.close()

# f1=open("HELLO.txt",'r')
# f1.seek(5)
# print(f1.read(10))
# print(f1.read())

# f2=open("index.html",'w')
# f2.write("<html></html>")
# f2.close()
# import os 
# os.remove('index.html')


# f2=open("ANIKDASHORA.txt",'w')
# l=["WELCOME","\nWORLD","\nto in this"]
# f2.writelines(l)
# f2.close()

# f2 = open("ANIKDASHORA.txt",'r')
# print(f2.readlines())
# # print(f2.readline())
import re
str ="Regular expersion in python working is going on right now t#his day"
st = str.split()

x = re.findall("\w",str)
str = "".join(st)

str1 = "".join(x)
# print(str1)
if str1 == str:
    print("yes")
else:
    print("no")
