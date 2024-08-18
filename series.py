n=10
num1=0
num2=1
next=num2
count=1

while count<=n:
  print("next number",end=" ")
  count+=1
  num1,num2=num2,next
  next=num1+num2

print() 
  
