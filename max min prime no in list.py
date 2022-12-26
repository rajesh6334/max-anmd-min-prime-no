#maximum and minimum prime number in the list
l=[]
n=int(input())
m=int(input())
for i in range(n,m+1):
    f=0
    for j in range(n,i+1):
        if i%j==0:
            f=f+1
    if f==2:
        l.append(i)
print(l)


print('min prime is:',min(l))
print('max prime is:',max(l))
