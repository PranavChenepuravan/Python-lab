def add():
    a=int(input("Enter the first number: "))
    b=int(input("Enter the second number: "))
    s=a+b
    print(a,"+",b,"=",s)
    exit
def dif():
    a=int(input("Enter the first number: "))
    b=int(input("Enter the second number: "))
    d=a-b
    print(a,"-",b,"=",d)
def mul():
    a=int(input("Enter the first number: "))
    b=int(input("Enter the second number: "))
    m=a*b
    print(a,"*",b,"=",m)
def div():
    a=int(input("Enter the first number: "))
    b=int(input("Enter the second number: "))
    di=a/b
    print(a,"/",b,"=",di)
print("------MENU-------")
op=int(input("1.Sum\n2.Difference\n3.Multiple\n4.Division\nEnter the option:"))
if(op==1):
    add()
elif(op==2):
    dif()
elif(op==3):
    mul()
elif(op==4):
    div()
else:
    print("Enter option is invalid")
    
