# Enter your code here. Read input from STDIN. Print output to STDOUT

n=int(input())
maxi=0
for i in range(2,n):
    for j in range(2,n):
        power=pow(j,i)
        ds=0
        while(power>0):
            rem=power%10
            ds+=rem
            power//=10
        if(ds>maxi):
            maxi=ds
print(maxi)