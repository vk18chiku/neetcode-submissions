class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        start = 0
        end = len(numbers) - 1

        res = []

        while start < end:
            new_sum = numbers[start] + numbers[end]

            if new_sum == target:
                res.append(start + 1)
                res.append(end + 1)
                return res

            elif new_sum < target:
                start += 1

            else:
                end -= 1

        return res
        