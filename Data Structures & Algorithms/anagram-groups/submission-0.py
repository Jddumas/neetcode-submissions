class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #input = arr of strings
        #output list of lists of anagrams
        #group all word anagrams together in a list of lists
        #create a hashmap, key = sorted name, value = original name
        dict1 = {}
        for string in strs:
            sortedstr = ''.join(sorted(string))
            #add to dict value
            if sortedstr in dict1:
                dict1[sortedstr].append(string)
            # add key and value
            else:
                dict1[sortedstr] = [string]

        return list(dict1.values())

        