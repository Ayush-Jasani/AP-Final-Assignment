def moveZeros(nums):
  return [x for x in nums if x != 0] + [x for x in nums if x == 0]