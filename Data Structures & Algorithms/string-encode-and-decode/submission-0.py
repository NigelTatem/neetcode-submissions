class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []

        for s in strs:
            encoded.append(str(len(s)) + '#' + s)
        
        return ''.join(encoded)


    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0

        while i < len(s):
            j = s.find('#', i)

            length = int(s[i:j])

            start_of_str = j + 1
            end_of_str = start_of_str + length
            decoded.append(s[start_of_str:end_of_str])

            i = end_of_str

        return decoded
