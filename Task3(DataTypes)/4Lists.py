if __name__ == '__main__':
    N = int(input())
    l=[]
    for k in range(N):
        s=input()
        m=s.split(" ")
        if m[0]=='insert':
            i=int(m[1]) 
            j=int(m[2])
            l.insert(i,j)
        elif s=='print':
            print(l)
        elif m[0]=='remove':
            i=int(m[1])
            l.remove(i)
        elif m[0]=='append':
            i=int(m[1])
            l.append(i)
        elif s=='pop':
            l.pop(len(l)-1)
        elif s=='sort':
            l.sort()
        elif s=='reverse':
            l.reverse()
