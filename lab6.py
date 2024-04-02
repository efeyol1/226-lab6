import math

n=int(input("enter n"))
x=int(input("enter x"))

mylist =[]
mylist2 =[]

double1 =0.0
double =1.0
for i in range (0,n):
    mylist.append(pow(n,i))

for a in range (0,x):
    mylist2.append(math.factorial(a))

print(mylist)
print(mylist2)
for h in range(0,x):
    double1 = lambda n,x : mylist[n] / mylist2[x]
    double+=double1(n-1,x-1)

print(double)


n=int(input("enter n:"))
def func(n):
    sum=0.0
    for k in range (1,n+1):
        sum+= pow(-1,k+1)/k

    print(sum)
func(n)
