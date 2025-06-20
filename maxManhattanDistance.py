class Solution:

    def maxDistance(self, s: str, k: int) -> int:
        return self.solve(s, k)

    def solve(self, s: str, k: int) -> int:
        #modify the least frequent letters first to the ones in their opposite 
        numOfN = 0
        numOfE = 0
        numOfW = 0
        numOfS = 0

        total = 0

        for str in s:
            if(str == 'N'):
                numOfN +=1
            elif(str == 'E'):
                numOfE += 1
            elif(str == 'S'):
                numOfS += 1
            else:
                numOfW += 1
            
            #see how many modifications we can make
            northtimes = min(numOfN, numOfS, k)
            westTimes = min(numOfE, numOfW, k - northtimes)

            total = max(total, self.dist(numOfN, numOfS, northtimes)+self.dist(numOfE, numOfW, westTimes))

        return total 
        

    def dist(self, drt1: int, drt2: int, times: int) -> int:
        return (abs(drt1 - drt2) + times * 2)   




def main():
    sol = Solution()
    test = "NWSE"
    k = 1
    print(sol.maxDistance(test, k))



if __name__ == '__main__':
    main()