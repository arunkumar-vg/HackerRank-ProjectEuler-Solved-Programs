num=int(input())
arr=[]
for i in range(0,num):
    value=int(input())
    arr.append(value)
sum=0
for i in range(0,num):
    sum=sum+arr[i]
a=len(str(sum))
x=a-10
for i in range(0,x):
    sum=sum//10
print(sum)
