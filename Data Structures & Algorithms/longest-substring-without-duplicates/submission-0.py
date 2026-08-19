class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left,right=0,0
        maxstr=0
        window=set()
        while right < len(s):
            if s[right] not in window:
                window.add(s[right])
                right+=1
                maxstr=max(maxstr,len(window))
            else:
                window.remove(s[left])
                left+=1

        return maxstr