def fib():
    l=int(input("Enter the limit of fibnoacci :"))
    val=0
    for i in range(0,l+1,1):
        if(i>=1):
            j=i
            k=j-1
            m=j+k
            print(m)
        else:
            print(i)
n=fib()
print(n)
