class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        chars_s = list(s)
        chars_t = list(t)

        if sorted(chars_s) == sorted(chars_t):
            return True
        else:
            return False