p=int(input())
m=set(map(int,input().split()))
q=int(input())
n=set(map(int,input().split()))
r=m.union(n)
k=0
for i in r:
    k=k+1
print(k)
