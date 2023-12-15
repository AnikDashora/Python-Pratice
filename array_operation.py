from sort_function_1 import creat_l

l=creat_l()

a=max(l)**2
b=True
c=0
for i in l:
    for j in l:
        if (i*j > a):
            c = i*j
            
            b=False
        else:
            b = True

if b : 
    print(f"max product factor is {max(l)}^2",a)
else:
    print(f"max product is {a} and its factors in the list is {i}, {j}")



