class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned="".join(c for c in s if c.isalnum())
        cleaned=cleaned.lower()
        res=cleaned[::-1]
        print(res)
        if res==cleaned:
            return True
        return False