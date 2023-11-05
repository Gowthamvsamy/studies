n=int(input("Enter n"))
'''for i in range (1,a+1):
    print(i)'''

t=n
i=0
j=0
while(n>0):
    l=n%2
    n=n//2
    j+=1
print(j)
for j in range(0,j+1):
    a=t%2
    t=t//2
    i=a*pow(10,j)+i
    print(n)
print(i)
