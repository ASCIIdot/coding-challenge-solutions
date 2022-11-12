class Solution:
    def isPalindrome(self, x: int) -> bool:
        array = [d for d in str(x)]
        array2 = array[::-1]
        if array == array2:
            return True
