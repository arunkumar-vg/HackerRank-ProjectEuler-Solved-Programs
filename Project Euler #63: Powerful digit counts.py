# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
a=1
for i in range(1,10):
    power=pow(i,n)
    if(power>=pow(10,n-1) and power<pow(10,n)):
        print(power)
    else:
        a+=1
    if(power>pow(10,n)):
        break


