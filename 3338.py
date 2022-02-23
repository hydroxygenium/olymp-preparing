N, M = map(int, input().split())
nums =  list(map(int, input().split()))

base_product = 1
for i in nums:
    base_product *= i

sum_nums = sum(nums) + base_product

for j in range(M-1):
    base_product = base_product**2
    sum_nums+=base_product

print(sum_nums%10)
