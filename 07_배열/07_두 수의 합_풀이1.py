# 풀이1 브루트 포스로 계산
# 5,284 밀리초

def twoSum(slef, num: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
