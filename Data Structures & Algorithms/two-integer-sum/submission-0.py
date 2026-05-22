class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_index = defaultdict() 
        print(nums)
        for index in range(len(nums)):
            num = nums[index]
            print("Num: ",num)
            complementary = target - num
            print("Complementary: ", complementary)
            print(num_index)
            if complementary in num_index:
                return [num_index[complementary],index]
            num_index[num]=index
        