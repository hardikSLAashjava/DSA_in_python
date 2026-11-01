class Solution(object):
    def plusOne(self, digits):
        l = []
        s = ""
        for i in range(len(digits)):
            s += str(digits[i])
        
        s = int(s)+1
        s = str(s)

        for i in range(len(s)):
            l.append(int(s[i]))

        return l