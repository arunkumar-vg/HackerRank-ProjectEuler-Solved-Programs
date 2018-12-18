#!/bin/python3

limit=int(input())
arr=[]
for i in range(0,limit):
    value=int(input())
    arr.append(value)
for k in range(0,limit):
    n=1
    while(n>0):
        count=0
        for i in range(1,arr[k]+1):
            if(n%i==0):
                count+=1
        if(count==arr[k]):
            print(n)
            break
        n+=1

