# 1. Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
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





# 2. Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

my_number = [1, 0, 9, 0, 5, 0, 7,0, 8, 4]
my_number.sort()
# print(my_number)
def my_function(my_number):
    non_zero = [ x for x in my_number
                 if x != 0]
    zero = [0] * (len(my_number) - len(non_zero))
    return non_zero + zero
print(my_function(my_number))




