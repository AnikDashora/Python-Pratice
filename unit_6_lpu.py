# import os
class InvalidData(Exception):
    pass
a,b=int(input("what is a?")),int(input("what is b?"))
# l1=[10,20,30,40,50]
# print((os.path.isfile("HELLO.txt")))

# try:
#     f= open("hel.txt","r")
#     f.close()
#     c=a/b
#     print("Ans",c)
#     print(l1[7])
# except Exception as e:
#     print(e)


# # print("thank you")


# a,b=


try:
    if b == 0 :
        raise InvalidData("EXC raised")
    c = a/b
    print(c)

except InvalidData as e:
    print(e)

