import re
# str = "HELLO PYTHON PROGRAMMING"
# findall
# return is list of all matches if exsoct else empty list


# findall(pattern , source_sting)

# x= re.sub("G","h",str)
# # print(str.count("x"))
# print(x)
# str1 = "HELLO"
# t=re.sub("PYTHON","PYTHONNNNNNNNNNNNNNNNN",str)
# print(t)

str = "Example of Meta123 charact45ers in Regular Experssion."
x=re.findall('[ar]',str)
print(x)
x=re.findall('^Ex',str) # start with
print(x)
x=re.findall('ssion$',str) #ends with
print(x)

x=re.findall('...ar...',str) # print the charater[value] == number of dots
print(x)

x=re.findall('s*',str) # it will check for zero and more occurances
print(x)
x=re.findall('es*',str) # it will check for zero and more occurances
print(x)

x=re.findall('m+',str) # print one or more occurance
print(x)


# a,b = [1,2],["a"]
# print((zip(a,b)))


# z=input().split()
# # c = int(z)
# # print(c)
# abc = map(int,z)
# print(tuple(abc))

x= re.findall("e{2}s{2}",str) # number of occurance in a list
print(x)
# SPECIAL SEQ
#  \s white space cheather

x = re.findall("\s",str)
print(x)

# \S (no spaces will be returned)
x = re.findall("\S",str)
print(x)

# /d (digits return)(0-9)

x = re.findall("\d+",str)
print(x)

#/D (exclude digits)

x = re.findall("\D",str)
print(x)

#\w (return word,lower,uppercase,digits)(not speacial chater)
x = re.findall("\w",str)
print(x)
#\W(speacial chater)
x = re.findall("\W",str)
print(x)


x = re.findall("\S+",str)
print(x)

x = re.findall("[0-9][0-9][0-9][6]",str)
print(x)

