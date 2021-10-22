n = int(input())
s = set(map(int, input().split()))
num=int(input())
for i in range(num):
    m=input()
    st=m.split(" ")
    if m=='pop':
        s.pop()
    elif st[0]=='discard':
        q=int(st[1])
        s.discard(q)
    elif st[0]=='remove':
        l=int(st[1])
        s.remove(l)
sum=0
for i in s:
    sum=sum+i
print(sum)
