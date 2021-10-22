if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    l2={i for i in arr}
    l3=[i for i in l2]
    l3.sort()
    print(l3[-2])
