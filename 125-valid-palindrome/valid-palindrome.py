class Solution:
    def isPalindrome(self, s: str) -> bool:
        rem_space_s=''.join(ch.lower() for ch in s if ch.isalnum())
        temp=rem_space_s
        rev_temp=temp[::-1]
        if rev_temp==rem_space_s:
            return True
        return False