num=int(input("Enter a single digit number : "))
a=num%10
fdg=(num*10)+num
sdg=(num*100)+fdg
add=a+fdg+sdg
print(num,"+",fdg,"+",sdg,"= ",add)
