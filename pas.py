
def pascal(n):

    def ncr(n,r):
        a = 1
        b = 1
        c = 1
        for i in range(1,n+1):
            a *= i
        for i in range(1,r+1):
            b *= i
        for i in range(1,n-r+1):
            c *= i

        return int(a/(b*c))


    l=[]
    for i in range(n):
        l_in = []
        for j in range(i+1):
            l_in.append(ncr(i,j))
        l.append(l_in)

    for i in l:
        print(i)
        
        
    


pascal(3)
