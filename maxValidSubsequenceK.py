class Solution:
    def maximumLength(self, nums: list[int], k: int) -> int:

        normalised = nums.copy()
        for i in range(0, len(normalised)):
            normalised[i] = normalised[i] % k

        # the 2 options are the number repeats or 2 numbers alternate. need to find which is higher
        # find the max repeated number sequence
        maxRepeat: list[int] = [0 for i in range(0, k)]
        for i in range(0, len(normalised)):
            maxRepeat[normalised[i]] += 1
        
        maxRepeated = max(maxRepeat)

        if maxRepeated > len(normalised) / 2: # if over half the sequence is the same theres not going to be a larger alternating one
            return maxRepeated 

        # find the maximum alternating sequence
        starts = [0 for i in range(0, k)] # index represents what the sequence starts with
        alternate = [False for i in range(0, k)] # index represents what start sequence we are looking at

        for num in normalised:
            if not alternate[num]:
                starts[num] += 1
                alternate[num] = True
            
            if alternate[num]:
                # need to check if 
    

def main():
    pass


if __name__ == '__main__':
    main()