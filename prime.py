def prime(n):
    if n == 1:
        print("It is not a Prime Number")
    else:
        ans = True
        for i in range(2,n):
            if n%i == 0:
                ans = False
                break
        if ans:
            print("It is a Prime number")
        else:
            print("It is not a Prime number")
        

prime(4)
prime(45)
prime(10)
prime(15)
prime(53)
prime(87)
prime(52)
prime(11)
prime(17)
prime(0)
prime(1965)