dict_head = {
    "Anik":100,
    "Ram":10,
    "Tukaram":109,

}

dict_body={
    1:"Anik",
    2:"Ram",
    3:"Tukaram"

}

dict_head.update({"AANNIIKK":110000})
# print(dict_head)

l=[[1,2,3],
   [4,5,6],
   [7,8,9]
]

l1= [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]
for i in range(len(l)):
    for j in range(len(l[1])):
        l1[j][i] = l[i][j]

for i in l1:
    print(i)

print(2.1>2)