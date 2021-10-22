ans=True
a=set(input().split())
n=int(input())
for i in range(n):
    q=set(input().split())
    if not q.issubset(a):
        ans=False
    if(len(q)>=len(a)):
        ans=False
print(ans)
