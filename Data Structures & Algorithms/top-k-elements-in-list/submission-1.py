
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        output = []
        count_val= Counter(nums)
        freq = [[] for i in range(len(nums)+1)]

        for key,val in count_val.items():
            freq[val].append(key)
        res = []
        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                res.append(num)
                if len(res)==k:
                    return res 


        # My Initial logic
        # dec_sort = dict(sorted(count_val.items(), key=lambda item:item[1], reverse=True))
        # for key, value in dec_sort.items():
        #     output.append(key)
        # return output[0:k]