class Solution:
    def maximumLength(self, nums: list[int]) -> int:
        # all odd, all even, or alternate even odd / odd even

        normalised = nums.copy()
        for i in range(0, len(normalised)):
            normalised[i] = normalised[i] % 2
        
        oddCount = 0
        evenCount = 0
        oddEven = 0
        EvenOdd = 0

        expectOddInOddEven = True
        expectEvenInEvenOdd = True

        # go through and find the largest subsequence
        for i in range(0, len(normalised)):
            if normalised[i] == 0:
                evenCount += 1
            else:
                oddCount += 1
            
            if expectEvenInEvenOdd and normalised[i] == 0:
                EvenOdd += 1
                expectEvenInEvenOdd = False
            elif not expectEvenInEvenOdd and normalised[i] == 1:
                EvenOdd += 1
                expectEvenInEvenOdd = True
                
            if expectOddInOddEven and normalised[i] == 1:
                oddEven += 1
                expectOddInOddEven = False
            elif not expectOddInOddEven and normalised[i] == 0:
                oddEven += 1
                expectOddInOddEven = True

        return max(oddCount, evenCount, oddEven, EvenOdd)

def main():
    sol = Solution()
    test = [1,2,3,4]
    x = sol.maximumLength(test)
    print(x)

if __name__ == '__main__':
    main()