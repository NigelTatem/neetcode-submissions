from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        anagram_groups = []
        for word in strs:
            key = [0] * 26
            for c in word:
                key[ord(c) - ord('a')] += 1
            anagrams[tuple(key)].append(word)
        
        for anagram_group in anagrams.values():
            anagram_groups.append(anagram_group)
        
        return anagram_groups
