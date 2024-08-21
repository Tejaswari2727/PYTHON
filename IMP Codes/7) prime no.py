def chk(n):
    if n>1:
        for num in range(2,n+1):
            if n%2==0:
              print("not a prime")
        else:
                print("prime")
    else:
        print("not a prime")
n=int(input())
chk(n)


'''      
= RESTART: C:/Users/batti/OneDrive/Desktop/practice python/New folder/By C Sir/prac.py
7
prime





n=8
for i in range(2,n):

    if n%i==0:
        print("no")
        break
else:
    print("prime")


    = RESTART: C:/Users/batti/OneDrive/Desktop/practice python/New folder/By C Sir/prac.py
7
prime




n=int(input())
for i in range(1,n+1):
    c=0
    for j in range(1,i+1):
      if n%j==0:
          c=c+1
if c==2:
    print("prime")
else:
    print("not a prime")



= RESTART: C:/Users/batti/OneDrive/Desktop/practice python/New folder/By C Sir/prac.py
13
prime








def prime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c=c+1
    if c==2:
        print("prime")
    else:
        print("not a prime")
n=int(input())
prime(n)

= RESTART: C:/Users/batti/OneDrive/Desktop/practice python/New folder/By C Sir/prac.py
7
prime
'''























