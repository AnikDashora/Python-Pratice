def sort(r = 0):
    l= creat_l()
    if r == 0 or r == False:
        for k in range(len(l)):
            for i in range(len(l)-1):
                if l[i] > l[i+1]:
                    q=l.pop(i)
                    l.insert(i+1,q)
                else:
                    pass  
        return l    
    elif r == 1 or r == True:
        for k in range(len(l)):
            for i in range(-1,-1*len(l),-1):
                if l[i] > l[i-1]:
                    q=l.pop(i)
                    l.insert(i-1,q)
                else:
                    pass
        return l
    else:
        print("please enter a valid value of 'r'")

def sort_1(r = 0):
    l=creat_l()
    l_sort=[]
    if r == 0 or r == False:
        for i in range(len(l)):
            l_sort.append(min(l))
            l.remove(min(l))
        print(l_sort)
    elif r == 1 or r == True:
        for i in range(len(l)):
            l_sort.append(max(l))
            l.remove(max(l))
        print(l_sort)
    else:
        print("please enter a valid value in 'r'")
            
# def sort_2(r = 0):
#     l=creat_l()
#     l_new=[]
#     if r == (0 or False):



def creat_l():

    n=int(input("How many elements you need in your List: "))
    l=[]
    for i in range(n):
        l.append(int(input("The element: ")))
    return l    