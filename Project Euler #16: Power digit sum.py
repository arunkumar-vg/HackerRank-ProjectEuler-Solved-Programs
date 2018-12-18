n=int(input())
for i in range(0,n):
    val=int(input())
    power=pow(2,val)
    rem=0
    sum=0
    while(power!=0):
        rem=power%10
        sum+=rem
        power//=10
    print(sum)
    