import math
class Solution:
    def divideString(self, s: str, k: int, fill: str) -> list[str]:
        
        stringPointer = 0
        groupAmount = 0
        toReturn = []
        groupMaking = ""
        ceil = len(s)

        for i in range(0, math.ceil(len(s) / k) * k):
            if i < len(s) and len(groupMaking) < k:
                groupMaking += s[i]
            elif i < len(s) and len(groupMaking) >= k:
                toReturn.append(groupMaking)
                groupMaking = s[i]
            else:
                groupMaking += fill
        toReturn.append(groupMaking)
        return toReturn
        


def main():
    fill = 'x'
    test = "abcdefghiddd"
    k = 3
    sol = Solution()
    x = sol.divideString(test, k, fill)
    print(x)


if __name__ == '__main__':
    main()