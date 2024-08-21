
'''
#WAP print factors of a number

n=int(input())
c=0
for i in range(1,n+1):
    if n%i==0:
        print(i)


#WAP to print given no is prime or not

n=int(input())
c=0
for i in range(1,n+1):
    if n%i==0:
        print(i)
if c==2:
    print("prime number")
else:
    print("not a prime number")


'''



def prime(n):
    fc=0
    for i in range(1,n+1):
        if n%i==0:
            fc=fc+1
    '''if fc==2:
      print("prime")
    else:
      print("not a prime")

#t=int(input())
#for i in range(t):'''
n=int(input())
prime(n)
