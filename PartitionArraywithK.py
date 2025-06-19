class solution:
    def partitionArray(self, nums: list[int], k: int) -> int:
        nums.sort()

        #literallly just go down and add 1 each time gap is too big
        lowestCurrentNum = nums[0]
        amountOfSubarrays = 1
        for i in range(1, len(nums)):
            value = nums[i]
            if value - lowestCurrentNum > k: #means its invalid
                amountOfSubarrays += 1
                lowestCurrentNum = value
        
        return amountOfSubarrays
                

def main():
    sol = solution()
    test = [1,2,3]
    k = 0
    result = sol.partitionArray(test, k)
    print(result)

if __name__ == '__main__':
    main()