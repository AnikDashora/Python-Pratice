#for memory location we can use id() function
# for type we havr type() function
# for "List" we use '[]', for "tuple" we use '()',for "set" we use '{}',for dict we use {"key":"value"}
#for keyword we need to import keyword and to print the list of keyword we can use keyword.kwlist and to
# check whether the word is a keyword we can use keyword.iskeyword() function

# a=10
# b=10
# c=20
# d="hello"
# d1="Dashora"
# e=12.25
# f=10+5j
# g=True
# l=[1,2,3,"Anik"]
# t=(1,2,3,"Anik")
# s={1,2,3,"Anik"}
# dict={"age":17,"name":"Anik"}
# print(id(a),id(b),id(c),id(d),sep="\n")
# print(type(a),type(b),type(c),type(d),type(e),type(f),type(g),type(l),type(t),type(s),type(dict),sep="/n")

# import keyword
# print(keyword.kwlist)
# print(keyword.iskeyword("True"))

'''for oprator we have 
Arithmethic operator(+,-,*,/,//,**,%)
relational operator(<,>,==,!=,<=,>=)
Logical operation(and(true is both are ture),or(ture if one is true),not()(true if the answer is false))
bitwise operator(only on int and bool value)
& -- and(if both 1 then output will 1 and if not the the output will be 0)
| -- or (if any 1 then output 1 otherwise 0)
^ -- xor (if both are same output 0 otherwise then output 1)
~ -- complement (-(x+1))
<< -- lestshift (shift bit value toward lest and then print new value )
>> -- rightshift (shift bit value toward right and then print new value)
assignment opertor(=)
special operator--
    a) identity operator
        is and is not  
    b)menbership operator
        in and not in         

''' 
# print(5 & 6)
# print(5 | 6)
# print(5^6)
# print(~4)
# print(~-4)
# print(55>>4)
# print(55<<4)
# print(a is b)
# print(a is not b)
# print(a  is c)
# print(a is not c)
# print(1 in l)
# print(1 not in l)
# print(6 in l)
# print(6 not in l)

'''order of opertor--
   ** -- expo 
   ~,+,-- complement,unary plus,unary minus
   *,/,%,// -- multi,divi,modulo,floor
   +,- -- add,sub
   <<,>> -- left,rightshift
   & -- bitwise and
   ^,| -- bitwise xor,or
   <,>,<=,>= -- compare
   ==,!= -- equality
   =,+= -- assinment
   is,isnot -- identity
   in,notin -- membership
   and,or,not -- logical   '''

#in string oprator +(add to string),*(print multiple values)

# print(d+d1)
# print(2*d)

'''Random number -- 
for this we have to import random function'''
# import random
# print(random.random()) # float value in b/w 0.0 to 1.0
# print(random.uniform(2,4)) # float value in b/w a,b
# print(random.randint(2,4)) # int value b/w a,b
# print(random.getrandbits(3))# "getrandbits(k) here k is bits it will return int value b/w min and max of given k"
#print(random.choice(l)) # random element from the seq

'''boolean exp -- True or False'''

'''conditionals statements --- if,else,elif
    if (condition):
        statement1
        statement2
        statement(n)

    else:
         s1
          s2
           s3
            sn '''


#n=int(input("pick: "))
# q=int(input("PICK: "))
# o=int(input("PICK: "))
# if n==0:
#     print("0")
# else:
#     print("not 0") 


# if n>0:
#     print("+ve")
# else:
#     print("-ve")

# '''nested if -- when if is inside another if '''
# if (n>q):
#     if (n>o):
#         print("n is big")
#     else:
#         print("o is big")
# elif q >o:
#     print("q is big")
# else:
#     print("o is big ")  


'''loops-- 
while and for loop 
we need loop variable 
condition for termination
updatetion of loop variable 

while loop -- 
while condition:
      satement1
      statement2
      starement3
statementx
           
'''


i=0
# while i<=n:
#     print(i)
#     i=i+1    

'''for i in sequence(list,tuple,dict,range)
   for i in range(start,end,stepsize)
for i in seq:
      statement1
      statement2
      statementn   
 
                               '''   
 


# for i in range(5,0,-1):
#     print(i)

# for x in range(0,random.randint(1,5)):
#     print(x)

print(153%10)
print(153//10)