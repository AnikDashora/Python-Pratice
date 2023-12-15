# import re
# x=input("Enter: ")
# r=re.findall("^[a-z]_[a-z]$",x)
# if r:
#     print(r)
# else:
#     print("no")



# def text_match(text):
#         patterns = '^[a-z]+_[a-z]+$'
#         if re.search(patterns,  text):
#                 return 'Found a match!'
#         else:
#                 return('Not matched!')

# print(text_match("aab_cbbbc"))
# print(text_match("aab_Abbbc"))
# print(text_match("Aaab_abbbc"))



# try:
#     a = input("ENTER FILE NAME? ")
#     f = open(a,"r")
#     print(f.read())
#     f.close()

# except FileNotFoundError:
#     print("Please enter thr right name of the file you have to open")
# try:
#     a,b = int(input("A: ")),int(input("B: "))
#     c = a/b
# except ValueError:
#     print("ENTER CORRECT INPUT")


l=[[1,2,3,7,19],
   [4,5,6,9,19],
   [7,8,9,0,19],
   [2,7,9,5,19],
   [1,2,3,7,19]
]
s = 0
s1=0
for i in range(len(l)):
    for j in range(len(l[0])):
        if i == j:
            s1 += l[i][j]
        if i + j == len(l)-1:
            s += l[i][j]
        

print(s+s1)


# print(_sum)


# a = int(input("Enter: "))
# l = [str(i)  for i in range(a)]
# print(l)

# for i in l:
#     As = 0
#     for j in range(len(i)):
#         As += int(i[j]) ** len(i)
#     if As == int(i):
#         print(int(i))
#     else:continue

# str = "abcderaacd  bb a"
# import re
# print(re.findall("[ab]{1,2}",str))



import re

def text_match(text):
        patterns = '[A-Z]+[a-z]+$'
        if re.search(patterns, text):
                print(re.findall(patterns,text))
        else:
                print('Not matched!')
(text_match("AaBbGg"))
(text_match("Python"))
(text_match("python"))
(text_match("PYTHON"))
(text_match("aA"))
(text_match("Aa"))


def text_match(text):
        patterns = '[A-Z]+[a-z]+$'
        if re.search(patterns, text):
                print(re.findall(patterns,text))
        else:
                print('Not matched!')
(text_match("AaBbGg"))
(text_match("Python"))
(text_match("python"))
(text_match("PYTHON"))
(text_match("aA"))
(text_match("Aa"))

