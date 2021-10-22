def average(array):
    s=set(array)
    k=0
    sum=0
    for i in s:
        k=k+1
        sum=sum+i
    ans=sum/k
    float_format={":.3f".format(ans)}
    return ans

if __name__ == '__main__':