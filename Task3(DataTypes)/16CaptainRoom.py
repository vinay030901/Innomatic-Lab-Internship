n=int(input())
dic={}
rooms=input().split()
for i in rooms:
    i=int(i)
    if i in dic:    
        dic[i]=dic[i]+1
    else:
        dic[i]=1
for i,j in dic.items():
    if j!=n:
        print(i)
