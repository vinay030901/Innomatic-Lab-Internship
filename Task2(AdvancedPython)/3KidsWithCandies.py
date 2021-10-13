candies = [2,3,5,1,3]
extraCandies = 3
ans=[False]*len(candies)
for i in range(len(candies)):
    sum=candies[i]+extraCandies
    m=0
    for j in range(len(candies)):
        if j==i:
            pass
        if candies[j]>m:
            m=candies[j]
        if(sum>=m):
            ans[i]=True
        else:
            ans[i]=False
print(ans)