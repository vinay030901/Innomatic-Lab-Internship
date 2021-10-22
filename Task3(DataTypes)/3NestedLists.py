if __name__ == '__main__':
    l=[]
    scores=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        l.append([name,score])
        scores.append(score)
        l.sort()
        scores.sort()
    l_set={i for i in scores}
    l_list=[i for i in l_set]
    l_list.sort()
    c=l_list[1]
    ans=[i for [i,j] in l if j==c]
    for i in ans:
        print(i)
