n=int(input("Enter decimal value"))
i=0
c=0
while(n>0):
    a=n%2
    n=int(n/2)
    i=i+a*pow(10,c)
    c=c+1
print(i)
