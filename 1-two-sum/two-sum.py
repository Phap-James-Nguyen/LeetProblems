class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        p2 = 0
        mydict = {}
        result = []

        for i in range(len(nums)):
            sub1 = target - nums[i]
            if nums[i] not in mydict:
                mydict[sub1] = i #key : value sub : index at number that needs it
        
            else:
                return [i,mydict[nums[i]]]
                
        
        