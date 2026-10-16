class Solution:
    def myAtoi(self, s: str) -> int:
        i=0
        n=len(s)
        # step 1:skip leading spaces
        while i<n and s[i]==' ':
            i+=1
        # step 2 : Handle sign
        sign=1
        if i<n and s[i]=='-':
            sign=-1
            i+=1
        elif i<n and s[i]=='+':
            i+=1
        #step 3 convert digits
        num=0
        while i <n and s[i].isdigit():
            digit=int(s[i])
            num=num*10+digit
            i+=1
        #step 4 apply sign
        num=num*sign
        #step 5: clamp to 32 -bit integer range
        INT_MIN=-2**31
        INT_MAX=2**31-1

        if num<INT_MIN:
            return INT_MIN
        if num>INT_MAX:
            return INT_MAX
        return num
