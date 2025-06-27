import itertools
class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        maxLength = len(s) // k

        #means its not possible
        if maxLength == 0:
            return "" 
       
        whereOccurs: dict[str, list[int]] = {} #counts where each letter occurs

        for i in range(0, len(s)):
            chrLookingAt = s[i]
            #add to whereOccurs
            if chrLookingAt in whereOccurs:
                whereOccurs[chrLookingAt].append(i)
            else:
                whereOccurs[chrLookingAt] = [i]

        #mark which letters could be used in a largest substring
        #i.e letter occurs more than k times
        possibleLetters = []
        for ch in whereOccurs.keys():
            if len(whereOccurs[ch]) >= k:
                possibleLetters.append(ch)
        
        #check all possible subsequences including repeated letters
        lexographicallyLargest = [] #unfortunatly, we need the 'lexographically largest'. so need to check all of a certain length if possible.
        foundThisSize = False
        for i in range(maxLength, 0, -1):
            for combo in itertools.product(possibleLetters, repeat=i):
                if self.subSequencePossible(combo, whereOccurs, k):
                    lexographicallyLargest.append(combo)
                    foundThisSize = True
            
            if foundThisSize: #if we found a string this size
                return self.tupleToString(max(lexographicallyLargest))
 
        return ""

    def tupleToString(self, tuple: tuple) -> str:
        return ''.join(tuple)


    def subSequencePossible(self, subSequence: tuple, whereOccurs: dict[str, list[int]], k: int) -> bool:
        last = -1
        for i in range(0, k):
            for j in range(0, len(subSequence)):
                 occurences = whereOccurs[subSequence[j]]
                 works = False
                 for w in occurences: #get the next occuring letter
                     if w > last:
                         last = w
                         works = True
                         break
                 if not works:
                     return False
        
        return True
                        
        


def main():
    sol = Solution()
    test = "letsleetcode"
    k = 2
    x = sol.longestSubsequenceRepeatedK(test, k)
    print(x)

if __name__ == '__main__':
    main()