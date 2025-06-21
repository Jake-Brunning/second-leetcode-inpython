class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        #count how many times each letter occurs
        lettersOccur: dict[str, int] = {}

        for c in word:
            if c in lettersOccur:
                lettersOccur[c] = lettersOccur[c] + 1
            else:
                lettersOccur[c] = 1 #put in dict

        return self.deleteDown(list(lettersOccur.values()), 0, k)


    #get smallest and largest values. delete so there within k or so smallest is removed based on whats smaller
    def repeatSmallestLargest(self, freqs:list[int], currentDelets: int, k:int):
        #get both index 
        
        minVal = min(freqs)
        maxVal = max(freqs)

        if (maxVal - minVal <= k):
            return currentDelets
        else:



    def deleteDown(self, freqs: list[int], currentDeletes: int, k: int) -> int:
        freqs = freqs.copy()

        if self.allInKRange(freqs, k):
            return currentDeletes
        
        delts = []
        for i in range(0, len(freqs)):
            freqs[i] = freqs[i] - 1

            if freqs[i] == 0: #remove from list if its equal to 0
                freqs.pop(i)
                delts.append(self.deleteDown(freqs, currentDeletes+ 1, k))
                freqs.insert(i, 1)
            else:
                delts.append(self.deleteDown(freqs, currentDeletes + 1, k))
                freqs[i] = freqs[i] + 1

        return min(delts)
        


    #check if its a valid solution
    def allInKRange(self, values: list[int], k: int) -> bool:
        minVal = min(values)
        maxVal = max(values)
        return (maxVal - minVal) <= k

def main():
    sol = Solution()
    test = "rkcmm"
    k = 0
    x = sol.minimumDeletions(test, k)
    print(x)

if __name__ == '__main__':
    main()