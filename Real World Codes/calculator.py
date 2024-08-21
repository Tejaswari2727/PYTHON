def add(n1,n2):
    return n1 * n2
def subtract(n1,n2):
    return n1 - n2
def multiply(n1,n2):
    return n1 * n2
def divide(n1,n2):
    return n1 / n2
print("please select operation -\n"
      '''
      1. Add
      2.Subtract
      3.Multiply
      4.Divide
      ''')
select=int(input("select operations form 1,2,3,4:"))
n1=int(input("enter first number:"))
n2=int(input("enter second number:"))
if select==1:
  print(n1,"+",n2,"=",add(n1,n2))
elif select==2:
  print(n1,"-",n2,"=",subtract(n1,n2))
elif select==3:
  print(n1,"*",n2,"=",multiply(n1,n2))
elif select==4:
  print(n1,"/",n2,"=",divide(n1,n2))
else:
  print("invalid input")

-----------------OP---------------------

  = RESTART: C:/Users/batti/OneDrive/Desktop/practice python/New folder/more practice/calculator.py
please select operation -

      1. Add
      2.Subtract
      3.Multiply
      4.Divide
      
select operations form 1,2,3,4:1
enter first number:10
enter second number:12
10 + 12 = 120
    
