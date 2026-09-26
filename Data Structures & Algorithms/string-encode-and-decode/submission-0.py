class Solution:

    def encode(self, strs: List[str]) -> str:
        # iterative approach: iterate through the list fo strings and add it to the encoded string with a delimiter to preserve the list could be space.    
        # O(n)
        encoded_string = ""
        for string in strs:
            encoded_string += str(len(string)) + "#" + string
        return encoded_string

    def decode(self, s: str) -> List[str]:
        # using the delimiter. can split the encoded string to its respective string
        # resulting encoded string with have a delimiter at the end can be cleaned up before split as it outputs a list
        decoded = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j = j+1
            # example for 5#Hello
            length = int(s[i:j])
            # 3:8
            start = j + 1
            end = start + length
            decoded.append(s[start:end])
            i = end
        return decoded