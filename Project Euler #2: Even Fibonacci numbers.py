#!/bin/python3

t=int(input())
ar=[]
for i in range(0,t):
    n=int(input())
    sum=0
    a=1
    b=1
    for j in range(0,n):
        c=a+b
        a=b
        b=c
        if(c>n):
            break

        if(c%2==0):
            sum=sum+c
    ar.append(sum)
for i in range(0,t):
    print(ar[i])