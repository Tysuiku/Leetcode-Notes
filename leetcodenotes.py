#Leetcode Notes

#217. Contains Duplicate
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        numset = set()

        for n in nums:
            if n in numset:
                return True
            else:
                numset.add(n)
        
        return False

#242. Valid Anagram

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        map1 = {}
        map2 = {}

        for c in s:
            map1[c] = map1.get(c,0)+1

        for c in t:
            map2[c] = map2.get(c,0)+1

        return map1 == map2
    
