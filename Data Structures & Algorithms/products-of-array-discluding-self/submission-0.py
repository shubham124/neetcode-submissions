class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        prefix, suffix = [],[0]*n
        output = []
        
        for i in range(0,n):
            if i == 0:
                prefix.append(nums[i])
            else:
                prefix.append(prefix[i-1]*nums[i])
        for i in range(n-1,0,-1):
            if i == n-1:
                suffix[i]=nums[i]
            else:
                suffix[i]=suffix[i+1]*nums[i]
        for i in range(n):
            if i ==0:
                output.append(suffix[i+1])
            elif i==n-1:
                output.append(prefix[i-1])
            else:
                output.append(prefix[i-1]*suffix[i+1])
        return output

        