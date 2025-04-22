# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
nums=[2,4,6,4];

def product(nums):
    n=len(nums);
    ans=[1]*n;
    
    for i in range (n):
        for j in range (n):
            if i != j:
                ans[i] *= nums[j]
    return ans;
print(product(nums))