def fntocel():
    fn=float(input("Enter the temparature in Fahrenheit: "))
    cel=((fn-32)*(5/9))
    print(fn,"Fahrenheit = ",cel," Celsius")

def celtofn():
    cel=float(input("Enter the temparature in Celsius: "))
    fn=((cel*9/5)+32)
    print(cel,"Celsius = ",fn," Fahrenheit")
a=int(input("Choose your option 1.Fahrenheit->Celsius 2.Celsius->Fahrenheit : "))
if(a==1):
   fntocel()
elif(a==2):
    celtofn()
else:
    print("Invalid selection")
