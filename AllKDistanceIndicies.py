class Solution:
    def findKDistantIndices(self, nums: list[int], key: int, k: int) -> list[int]:
        temp = []
        
        #make indexes to add, to use when we find a k
        indexes = []
        for i in range(-k, k + 1):
            indexes.append(i)

        

        for i in range(0, len(nums)):
            num = nums[i]
            if num == key: #add all indexes k around
                temp += self.manipIndexes(indexes, i)

        #remove all negative indexes
        toReturn = []
        for i in range(0, len(temp)):
            if temp[i] > -1 and temp[i] < len(nums):
                toReturn.append(temp[i])

        return list(set(toReturn))

        

    def manipIndexes(self, indexes: list[int], offset):
        toReturn = indexes.copy()
        
        for i in range(0, len(toReturn)):
            toReturn[i] += offset

        return toReturn


def main():
    k = 2
    key = 2
    test = [2,2,2,2,2]
    sol = Solution()
    x = sol.findKDistantIndices(test, key, k)
    print(x)


if __name__ == '__main__':
    main()