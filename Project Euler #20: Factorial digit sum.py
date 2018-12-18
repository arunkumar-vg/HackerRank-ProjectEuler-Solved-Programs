n=int(input())
for i in range(0,n):
    val=int(input())
    fact=1
    for j in range(1,val+1):
        fact*=j
    sum=0
    while(fact!=0):
        rem=fact%10
        sum+=rem
        fact//=10
    print(sum)
    