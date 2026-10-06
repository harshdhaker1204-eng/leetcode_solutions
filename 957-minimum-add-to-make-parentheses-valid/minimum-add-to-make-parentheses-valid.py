class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        ans=0
        balance=0
        for i in s:
            if i=="(":
                balance+=1
            if i==")":
                if balance>0:
                    balance-=1
                else:
                    ans+=1
        answer=ans+balance
        return answer