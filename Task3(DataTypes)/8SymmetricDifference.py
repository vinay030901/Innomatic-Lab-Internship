l=int(input())
m=set(map(int,input().split()))
o=int(input())
n=set(map(int,input().split()))
q=n.symmetric_difference(m)
q_list=sorted(list(q))
for i in q_list:
    print(i)
