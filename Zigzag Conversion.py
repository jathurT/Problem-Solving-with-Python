class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s
        # _ is a throwaway variable to indicate that the loop variable is not used
        # in this case, we are not using the index i
        # zigzag = ['' for _ in range(numRows)] is equivalent to zigzag = ['' for i in range(numRows)]
        zigzag = ['' for _ in range(numRows)] # create a list of numRows number of empty strings
        row, step = 0, 1
        for char in s:
            zigzag[row] += char # add the character to the string at the current row
            if row == 0:
                step = 1
            elif row == numRows - 1:
                step = -1
            row += step
        return ''.join(zigzag) # join the strings in the list zigzag and return the result