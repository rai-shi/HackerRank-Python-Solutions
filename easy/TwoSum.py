# challenge : come up with an algorithm that is less than O(n2) time complexity
def twoSum(nums: list[int], target: int) -> list[int]:

        # for left_idx, i in enumerate(nums[:]):
        #     for right_idx, j in enumerate(nums[left_idx+1:]):
        #         if (i+j) == target:
        #             return [left_idx, (left_idx+right_idx+1)]

        complement_list = {}
        for idx, num in enumerate(nums):
            complement = target - num
            if complement in complement_list:
                return [complement_list[complement], idx]
            complement_list[num] = idx
        return []