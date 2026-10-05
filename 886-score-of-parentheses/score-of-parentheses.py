class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        count=0
        ans=0
        for i in range(len(s)):
            if s[i] =='(':
                count+=1
            else:
                count-=1
                if s[i-1]=='(':
                    ans+=2**count
        return ans