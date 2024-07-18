# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 1
        r = n
        m = (l+r)//2

        while(l<r):
            m = (l+r)//2
            if isBadVersion(m):
                if not isBadVersion(m-1):
                    return m
                else:
                    r = m-1
            else:
                l = m + 1
        return l
            
