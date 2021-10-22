n=int(input())
l=[]
s=set(l)
for i in range(n):
    p=input()
    s.add(p)
k=0
for i in s:
    k=k+1
print(k)
