class Solution:
    def romanToInt(self, s: str) -> int:
        s=list(s)
        for numeral in range(0,len(s)):
            match s[numeral]:
                case 'I':
                    s[numeral]=1
                case 'V':
                    s[numeral]=5
                case 'X':
                    s[numeral]=10
                case 'L':
                    s[numeral]=50
                case 'C':
                    s[numeral]=100
                case 'D':
                    s[numeral]=500
                case 'M':
                    s[numeral]=1000

        for numeral in range(0,len(s)):
            if numeral+1 != len(s) and s[numeral]<s[numeral+1]:
                s[numeral+1]=s[numeral+1]-s[numeral]
                s[numeral]=0

            elif numeral+1 != len(s) and s[numeral]>=s[numeral+1]:
                next
            else:
                next

        s=sum(s)
        return(s)
