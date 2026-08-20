# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3 []
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        r, l = 0, len(numbers) - 1
        
        while(r<=l):
            Sum = numbers[r] + numbers[l] 
            if Sum == target:
                return [r+1, l+1]
            elif Sum < target:
                r = r + 1
            else:
                l = l - 1
            

```
