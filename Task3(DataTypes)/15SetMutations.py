n=int(input())
n_set=set(map(int,input().split()))
k=int(input())
for i in range(k):
    st=input().split()
    if st[0]=='intersection_update':
        j=st[1]
        j_set=set(map(int,input().split()))
        n_set.intersection_update(j_set)
    elif st[0]=='difference_update':
        j=st[1]
        j_set=set(map(int,input().split()))
        n_set.difference_update(j_set)
    elif st[0]=='update':
        j=st[1]
        j_set=set(map(int,input().split()))
        n_set.update(j_set)
    elif st[0]=='symmetric_difference_update':
        j=st[1]
        j_set=set(map(int,input().split()))
        n_set.symmetric_difference_update(j_set)
print(sum(n_set))
