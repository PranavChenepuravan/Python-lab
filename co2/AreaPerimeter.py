class Rectangle():
    def op1(self):
        self.length=int(input("Enter the length: "))
        self.bridth=int(input("Enter the bridth: "))
        self.area=self.length*self.bridth
        print("Area")
        print(self.area)
        print("Perimeter")
        print((self.length+self.bridth)*2)
class Square():
    def op2(self):
        self.length=int(input("Enter the length: "))
        self.area=self.length*self.length
        print("Area")
        print(self.area)
        print("Perimeter")
        print((self.length+self.length)*2)
class Triangle():
    def op3(self):
        self.length=int(input("Enter the height: "))
        self.bridth=int(input("Enter the bridth(first side): "))
        self.s2=int(input("Enter the second side: "))
        self.s3=int(input("Enter the third side: "))     
        self.area=self.length*self.bridth
        print("Area")
        print(self.area)
        print("Perimeter")
        print(self.bridth+self.s2+self.s3)

print("-------------MENU---------------")
op=int(input("1.Rectangle\n2.Square\n3.Triangle\nEnter your choice: "))

if(op==1):
    f=Rectangle()
    f.op1()
elif(op==2):
    f=Square()
    f.op2()
elif(op==3):
    f=Triangle()
    f.op3()
else:
    print("Invalid")


        
        
