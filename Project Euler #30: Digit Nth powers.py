n=int(input())
sum=0
for i in range(2,999999):
    k=i
    rem=0
    s=0
    while(k!=0):
        rem=k%10
        s+=pow(rem,n)
        k//=10
    if(s==i):
        sum+=i
print(sum)
