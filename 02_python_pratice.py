# i=0
# while i<=11:
#     print(i)
#     i=i+1


# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()        



# n=int(input("Enter number:"))
# s=0
# for i in range(n+1):
#     s=s+i
# print("Sum is",s)    


# for i in range(1,11):
#     print(f"The value of {n} x {i} =",n*i)


# numbers=[12,75,150,180,145,525,50]
# for i in numbers:
#     if i>500:
#         break 
#     elif i>150:
#         continue
#     elif i%5==0:
#         print(i)
    


# n=int(input("Enter: "))
# l=[]
# for i in range(n):
#     x=input("enter name:")
#     l.append(x)
# print(l)    

# i=0
# while n!=0:
#     n=n//10
#     i=i+1


# print(i)



# for i in range(n,0,-1):
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     print()  



# l=[]
# l2=[]
# l3=[]
# for i in range(0,n):
#     x=int(input("enter number: "))
#     l.append(x)
# print(l)

# for j in range(n,0,-1):
#     l2.append(l[j-1])

# print(l2)

# for k in range(n):
#     l3.append(min(l))
#     l.remove(min(l))
# print(l3)    


# n=["snowball","chewy","bubbles","gruff"]
# a=["cat","dog","fish","goat"]
# age=[1,2,2,6]
# u=list(zip(n,a,age))
# for i in u:
#     print(str(i).replace('(' , ' ').replace(')' , ' ').replace(',', '').replace("'", ''))


# data = "10,20,30,30,20,10,10,25,30,25,41,50,50,41,25,30,20,10"
# data_list = [int(x) for x in data.split(",")]
# print(data_list)
# l=[]
# for i in data_list:
#     if i not in l:
#         l.append(i)
# print(l) 





# d={"hi","bye"}
# d1={"hello","tata"}
# x=dict.fromkeys(d,d1)
# print(x)
# l="hi11"
# l1="22"
# l2="hI,how are you "
# x=l2.find('ho')
# print(x)



# str="Anik@dashora#lpu!roomnumber"
# a="abcdefghijklmnopqrestuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
# str1=""
# for i in str:
#     if i in a:
#         str1+=i
# print(str1)  
# 
#       



import pandas as pd
s=pd.Series([1,2,3,4])
print(s)