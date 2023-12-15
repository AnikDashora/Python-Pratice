# # l=[1,2,3,"abc",20.5]
# # print(type(l))
# # l1=list((1,2,3))
# # print(l1)
# # print(l[5:1:-1])
# l=[2,3,4]
# l1=["Lokesh","varun",25,"50","Rohit","Arsh"]
# print(len(l1))
# print(type(l1))
# print(l1)
# l1.append("Kanak")
# l1.append(1)
# c=l1.copy()
# # l1.clear()
# l1.append("Rohit")
# l1.extend(l)
# print(l1)
# # print(c)
# # print(len(l1))
# print(l1.count("Rohit"))
# print(l1.index(2))
# # l1.insert(-2222,1)
# print(len(l1))
# # l1.pop("Rohit")
# l1.reverse()
# # print(l1)


# l=[25,2,5,1,0]

# l.sort(reverse=1)
# print(l)
# l.pop(1)
# print(l)




# l=[]
# for i in range(10):
#     l.append(i)

# print(l)

# new_l=[exp for item in iterable if condition]

# list comphension
l=[i for i in range(10)]
print(l)

f=["apple","banana","cherry","kiwi","mango"]
f_l=[]
for i in f:
    if "a" in i:
        f_l.append(i)
print(f_l)  

f_n_l=[i for i in f if ("a" in i or "A" in i) ]
print(f_n_l)




list_square=[i**2 for i in range(10) if i<5  ]
print(list_square)





























