#ATM bill generation

username='Teju'
password=123
user_name=input("enter the username:")
passwords=int(input("enter the password:"))
s='''
  1.option1
  2.option2
  3.option3
  4.option4
  '''
Amount=1000
if user_name==username and passwords==password:
    while True:
        print(s)
        option=int(input())
        if option==1:
            credit=int(input("enter amount:"))
            print("the total amount is:",Amount+credit)
        elif option==2:
            debit=int(input("enter amount"))
            print("the total amount is:",Amount-debit)
        elif option==3:
            print("###Mini statement###")
        elif option==4:
            break
        else:
            print("invalid")
else:
    print("Not found")