o=input()
x=map(int,input().split())
y=set(map(int,input().split()))
z=set(map(int,input().split()))
h=0
for i in x:
    if i in y:
        h=h+1
        pass
    if i in z:
        h=h-1
print(h)
