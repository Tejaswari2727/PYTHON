# without using  if conditional statement

n=int(input())
print("even"*(n%2==0),"Odd"*(n%2!=0))

# without using % operator

def tej(n):
    tej=True
    for i in range(1,n+1):
            if tej==True:
               tej=False
            else:
                tej=True
    return tej

n=3
if tej(n)==True:
    print("even")
else:
    print("odd")
            
# without using % operator                                   [OR]
                                             
                   
n=7
temp=n
while temp>1:
    temp=temp-2
print("even"*(temp==0)+"odd"*(temp==1))
