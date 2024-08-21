cb=200
mb=300
wb=100

print("****WELCOME TO ADITYA RESTARUANT****")
cname=input("enter the customer name:")
cphnno=input("enter the customer phone number:")
cbq=int(input("enter no of chicken biryani packets:"))
mbq=int(input("enter no of mutton biryani packets:"))
wbq=int(input("enter no of water bottles:"))
bill=(cb*cbq)+(mb*mbq)+(wb*wbq)
if bill>=500:
    disc=bill*10/100
elif bill>=300:
    disc=bill*5/100
elif bill>=200:
    disc=bill*2/100
else:
    disc=0
price=bill-disc
gst=price*12/100
amount=price+gst
print("customer name:",cname)
print("customer phone number:",cphnno)
print("bill to be paid:",amount)
print("Thank you")
print("visit again")






'''

output:-----
****WELCOME TO ADITYA RESTARUANT****
enter the customer nameTEJU
enter the customer phone number123456789
enter no of chicken biryani packets3
enter no of mutton biryani packets2
enter no of water bottles4
customer name: TEJU
customer phone number 123456789
bill to be paid 1612.8
Thank you
visit again



'''
