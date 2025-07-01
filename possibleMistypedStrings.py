class Solution:
    def possibleStringCount(self, word: str) -> int:
        # just find the most consecutive character
        previous = word[0]
        consecutiveCount = 0
        maxCount = 1 # starts at 1 due to the whole word being valid
        for i in range(1, len(word)):
            val = word[i]
            if val != previous:
                maxCount += consecutiveCount
                previous = val
                consecutiveCount = 0
            else:
                consecutiveCount += 1

    
        return maxCount + consecutiveCount



def main():
    sol = Solution()
    test = "abbcccc"
    x = sol.possibleStringCount(test)
    print(x)


if __name__ == '__main__':
    main()