#Super market bill generation

oil=300
soap=100
dal=250
salt=200
sugar=150
cname=input("Enter the Customer name:")
cno=int(input("Enter Customer mobile number:"))
oilq=int(input("Enter the Number of packets:"))
soapq=int(input("Enter the Number of Soaps:"))
dalq=int(input("Enter the Number of packets:"))
saltq=int(input("Enter the Number of packets:"))
sugarq=int(input("Enter the Number of packets:"))
bill=(oil*oilq)+(soap*soapq)+(dal*dalq)+(salt*saltq)+(sugar*sugarq)
if bill>2000:
    disc=bill*15/100
elif bill>1500:
    disc=bill*10/100
elif bill>1000:
    disc=bill*5/100
tbill=bill-disc
gst=tbill*12/100
obill=tbill+gst
print("Customer name:",cname)
print("Customer mobile no:",cno)
print("bill:",bill)
print("gst 12%:",gst)
print("discount:",disc)
print("*****THANK YOU VISIT AGAIN******")
         






Enter the Customer name:Geetha 
Enter Customer mobile number:'234565432456
Enter the Number of packets:2
Enter the Number of Soaps:3
Enter the Number of packets:5
Enter the Number of packets:7
Enter the Number of packets:1
Customer name: Geetha 
Customer mobile no: 234565432456
bill: 3700
gst 12%: 377.4
discount: 555.0
*****THANK YOU VISIT AGAIN******
