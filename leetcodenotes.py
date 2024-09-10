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
    
#1. Two Sum
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map = {}

        for i,n in enumerate(nums):
            comp = target - n
            if comp in map:
                return [map[comp],i]
            else:
                map[n] = i

#49. Group Anagrams 
# from collections import defaultdict on leetcode simple tools import is already implemented but best practice to remember
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        map = defaultdict(list)

        for word in strs:
            key = [0] * 26
            for c in word:
                key[ord(c) - ord('a')] += 1
            map[tuple(key)].append(word)

        return map.values() 
    
#347. Top K Frequent Elements
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

#238. Product of Array Except Self      
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1] * len(nums)
        #[1,1,1,1]

        prefix = 1
        postfix = 1

        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
            #prefix = 24
            #nums = [1,2,3,4]
            #res = [1,1,2,6]

        for i in range(len(nums)-1,-1,-1):
            res[i] *= postfix
            postfix *= nums[i]
            #prefix = 24
            #nums = [1,2,3,4]
            #res = [24,12,8,6]

        return res