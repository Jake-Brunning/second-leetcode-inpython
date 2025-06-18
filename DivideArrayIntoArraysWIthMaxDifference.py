
class Solution:
    possible = True

    #take 3 ints from the sorted list and check they are in k range
    def take3(self, nums, lower, k) -> list[int]:
        a = nums[lower]
        b = nums[lower + 1]
        c = nums[lower + 2]

        if(a + k < c):
            self.possible = False
            return []

        return [a, b, c]
        

    def divideArray(self, nums: list[int], k: int) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        result = []

        #take smallest onwards
        for i in range(0, n, 3):
            result.append(self.take3(nums, i, k))
        
        #return nothing if one of the arrays are invalid
        if not self.possible:
            return []
        return result
        

def main():
    sol = Solution()
    test = [1,3,4,8,7,9,3,5,1]
    k = 2
    print(sol.divideArray(test, k))
    
if __name__ == "__main__":
    main()