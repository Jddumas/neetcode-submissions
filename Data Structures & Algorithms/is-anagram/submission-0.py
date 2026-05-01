class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #understand
        # must contain the exact same letters
        # plan
        # use hashmap, letter key and # is value then compare
        dict1 = {}
        dict2 = {}
        for letter in s:
            # if it does not find a letter, add it
            if not dict1.get(letter):
                dict1[letter] = 1
            else:
                dict1[letter] += 1
        for letter in t:
            # if it does not find a letter, add it
            if not dict2.get(letter):
                dict2[letter] = 1
            else:
                dict2[letter] += 1
        
        if dict1 == dict2:
            return True
        else:
            return False
        