class Solution:
    #stores the indexes  which get to a value
    class location:
        num1Pointer = 0
        num2Pointer = 0
        value = 0
        num1r = True
        num2r = True

        def __init__(self, num1Poiner, num2Poiner, num1s, num2s, value):
            self.num1Pointer = num1Poiner
            self.num2Pointer = num2Poiner
            self.value = value

        #move this location to the next largest value
        def nextIndexAndValue(self, nums1: list[int], nums2: list[int]) -> int:
            num1Moves = nums1[self.num1Pointer + self.boolToNum(self.num1r)] * nums2[self.num2Pointer]
            num2Moves = nums1[self.num1Pointer] * nums2[self.num2Pointer + self.boolToNum(self.num2r)]

            #change to the smallest value
    
        def boolToNum(self, bool):
            if(bool):
                return 1
            else:
                return -1
        

    
    def kthSmallestProduct(self, nums1: list[int], nums2: list[int], k: int) -> int:
        # get the possible locations of the smallest values (largestSmallest and smallestLargest are in the world where [0] is negative)
        smallestLargest = self.location(0, len(nums2) - 1, True, False, nums1[0] * len(nums2) - 1) #- + 
        largestSmallest = self.location(len(nums1) - 1, 0, False, True, nums1[len(nums1) - 1] * nums2[0])# + -
        smallestSmallest = self.location(0, 0, False, False, nums1[0] * nums2[0])# + +
        largestLargest = self.location(len(nums1) - 1, len(nums2) - 1, True, True, nums1[len(nums1) - 1] * nums2[len(nums2) - 1])# - -

        #now we:
        #1) select smallest value
        #2) find next smallest value (num1Pointer++ or num2Pointer++ or another location)
        #3) repeat until we get to k




def main():
    pass

if __name__ == '__main__':
    pass