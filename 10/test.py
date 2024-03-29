def sum13(nums):
  val = 0
  if len(nums) < 1:
    return 0
  for x in range(len(nums)):
    if nums[x] != 13:
      val += nums[x]
  return val
print(sum13([1, 2, 13, 2, 1, 13]))