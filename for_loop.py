n=int(input("SELECT ANY NUMBER "))
x=1
y=0
c=0
w=0
for i in range(1,n,2):
    x*=i
print("product of odd number = ",x)
print("-----------------------------")



for i in range(1,n+1):
    if i%2 == 0:
        y+=1
    elif i%2 == 1:
        c+=1    
print("total number of even no:",y) 
print("total number of odd no:",c) 

for i in range(1,n+1):
    print(i)
    if i==5:
        break

print("--------------------")
for i in range(1,n+1):
    if (i==5):
        continue
    print(i)  




print("----------------------------")

q=input("Your Name-- ")
for i in q:
    print(i, end=" ")
    w+=1
print(w)  


s=str(n)
l=len(s)

print(type(l))
print(len(l))



print("--------------------------")


print(n**l)


       


    

