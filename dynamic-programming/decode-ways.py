class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """

        table = [0] * (len(s) + 1)

        table[0] = 1

        if s and s[0] == '0':
            return 0
        else:
            table[1] = 1

        for i in range(1, len(s)):
            if 1 <= int(s[i]) and 9 >= int(s[i]):
                table[i + 1] += table[i]
            
            if 10 <= int(s[i - 1:i + 1]) and 26 >= int(s[i - 1:i + 1]):
                table[i + 1] += table[i - 1]

        return table[len(s)]




        