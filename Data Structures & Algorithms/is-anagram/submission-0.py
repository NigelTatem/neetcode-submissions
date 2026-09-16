class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sortedS = ''.join(sorted(s)) #sorts string into a list alphabetically
        sortedT = ''.join(sorted(t)) #join puts each element back together into string
        if sortedS == sortedT:
            return True
        return False