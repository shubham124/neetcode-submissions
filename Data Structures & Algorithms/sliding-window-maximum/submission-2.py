class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Deque
        output = []
        l=r=0
        q = deque()
        while r < len(nums):
            while q and nums[q[-1]]<nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()

            if (r+1)>=k:
                output.append(nums[q[0]])
                l+=1
            r+=1
        return output

        # output = []
        # for i in range(len(nums)-k+1):
        #     maxi=nums[i]
        #     for j in range(i,i+k):
        #         maxi=max(maxi,nums[j])
        #     output.append(maxi)
        # return output

        # My first solution
        # max_num=[]
        # for i in range(len(nums)-k+1):
        #     max_num.append(max(nums[i:i+k]))
        # return max_num