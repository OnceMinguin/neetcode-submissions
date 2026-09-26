class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}
        result = [strs]
        for string in strs:
            char_count = {}
            for char in string:
                if char in char_count:
                    char_count[char] += 1
                else:
                    char_count[char] = 1
            key = tuple(sorted(char_count.items()))
            if key in anagram_dict:
                anagram_dict[key].append(string)
            else:
                anagram_dict[key] = [string]
        return list(anagram_dict.values())