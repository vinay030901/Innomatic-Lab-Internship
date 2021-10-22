p=int(input())
m=set(map(int,input().split()))
q=int(input())
n=set(map(int,input().split()))
ans=m.intersection(n)
k=0
for i in ans:
    k=k+1
print(k)
