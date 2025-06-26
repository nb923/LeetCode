class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        letters = [0] * 26

        for letter in s.lower():
            letters[ord(letter) - 97] += 1

        for letter in t.lower():
            letters[ord(letter) - 97] -= 1

        for num in letters:
            if num != 0:
                return False

        return True
        