class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        list1 = []
        list2 = []
        for i in range(len(s)):
            list1.append(s[i])
            list2.append(t[i])
        list1.sort()
        list2.sort()
        if list1 == list2:
            return True
        return False

        
        