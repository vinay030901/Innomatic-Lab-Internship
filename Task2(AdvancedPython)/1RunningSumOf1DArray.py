nums=[1,2,3,4]
if len(nums)==1:
    print(nums)
for i in range(1,len(nums)):
    nums[i] += nums[i-1]
print( nums)