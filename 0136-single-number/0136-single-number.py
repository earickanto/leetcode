class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        for i in nums:
            count =0 
            for j in nums:
                if i==j:
                    count+=1 

            if count == 1:
                return i       