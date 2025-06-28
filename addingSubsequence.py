class Solution:
    def maxSubsequence(self, nums: list[int], k: int) -> list[int]:
        og = nums.copy()
        nums.sort()
        hashedNums = set(nums[len(nums) - 1 - (k-1): len(nums)])
        toReturn = []
       
        # unfortunatly we need a subsequence so have to go find the indexes where elements are located
        for i in range(0, len(og)):
            if og[i] in hashedNums:
                toReturn.append(og[i])

        # get rid of unecessary repeats
        for i in range(0, len(toReturn) - k):
            toReturn.remove(min(toReturn))

        return toReturn



def main():
    test = [3,4,3,3]
    k = 2
    sol = Solution()
    x = sol.maxSubsequence(test, k)
    print(x)

if __name__ == '__main__':
    main()