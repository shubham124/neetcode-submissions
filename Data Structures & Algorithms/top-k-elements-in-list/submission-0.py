
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        output = []
        count_val= Counter(nums)
        #orted_data_desc = dict(sorted(data.items(), key=lambda item: item[1], reverse=True))

        dec_sort = dict(sorted(count_val.items(), key=lambda item:item[1], reverse=True))
        for key, value in dec_sort.items():
            output.append(key)
        return output[0:k]