# using for loop

n=int(input())
sum=0
for i in range(1,n):
    if n%i==0:
        sum=sum+i
        print(i) #print the factors
if sum==n:
    print("perfect number")
else:
    print("not a perfect number")

 = RESTART: C:/Users/batti/OneDrive/Desktop/practice python/New folder/By C Sir/perfect no.py
perfect


#  using function

def perfect(n):
    for i in range(1,n+1):
        sum=0
        if n%i==0:
            sum=sum+i
    if sum==n:
        print("perfect number")
    else:
        print("not a perfect number")
            
perfect(28)


= RESTART: C:/Users/batti/OneDrive/Desktop/practice python/New folder/By C Sir/perfect no.py
perfect


#use while loop

n=int(input())
i=1
sum=0
while(i<n):
    if n%i==0:
        sum=sum+i
    i=i+1
if sum==n:
    print("perfect number")
else:
    print("not a perfect number")




= RESTART: C:/Users/batti/OneDrive/Desktop/practice python/New folder/By C Sir/perfect no.py
perfect







    
