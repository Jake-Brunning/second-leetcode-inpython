class Solution:
    def findLHS(self, nums: list[int]) -> int:
        nums.sort()

        #get largest gap between two values
        currentMax = 0
        potentialSizes = []
        
        for i in range(0, len(nums)):
            currentMax = max(currentMax, self.checkSize(nums, i))

        return currentMax
        

    def checkSize(self, nums: list[int], startIndex: int) -> int:
        startVal = nums[startIndex]
        backPointer = startIndex + 1
        size = 1 # assume there is a valid end
        valid = False
        # loop through until we get a larger than one gap
        while(backPointer < len(nums)):
            diff = abs(startVal - nums[backPointer])
            
            if diff == 0:
                size += 1
                backPointer += 1
                continue

            if diff == 1:
                size += 1
                valid = True
                backPointer += 1
                continue
            
            else: # difference is not 0 or 1 so is invalid
                if valid:
                    return size
                else:
                    return 0

        if valid:
            return size
        else:
            return 0

def main():
    test = [1,3,2,2,5,2,3,7]
    sol = Solution()
    x = sol.findLHS(test)
    print(x)


if __name__ == '__main__':
    main()