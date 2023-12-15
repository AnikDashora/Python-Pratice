from sort_function_1 import creat_l
l = creat_l()
def array_manuplation(l):
    print(l)
    step =int(input("Step size: "))
    l_new=[]
    l_new.extend(l[(-1*step):])
    l_new.extend(l[:-1*step])
    return l_new

print(array_manuplation(l))