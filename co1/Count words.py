name=input("Enter a string : ")
sep=name.split()
le=len(sep)
for i in range(0,le,1):
  wrd=sep[i]

for i in range(0,le,1):
 for j in range(i+1,le,1):
   if sep[i]==sep[j]:
      print(sep[i]," is repeating")
