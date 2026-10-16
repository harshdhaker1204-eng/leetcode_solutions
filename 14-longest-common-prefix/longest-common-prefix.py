class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        reference=strs[0]
        for i in range(len(reference)):
            char=reference[i]
            for s in strs[1:]:
                if i>=len(s) or s[i]!=char:
                    return reference[:i]
        return reference
