class Solution:
    def candy(self, ratings: list[int]) -> int:
        x = self.convertToNums(ratings)
        print(ratings)
        print(x)

        total = 0
        for i in x:
            total += i

        return total

    #normalise rating list so everything is 1 more or less than neighbours
    def convertToNums(self, ratings: list[int]) -> list[int]:
        #add one to each num to convert to candies
        ratings = [rating+1 for rating in ratings]

        #set the lowest value to 1, then propergate from there
        lowestIndex = self.getLowestValue(ratings)
        candies = ratings.copy()
        candies[lowestIndex] = 1

        #set values to as low as possible rightwards and leftwards of the lowest index
        #rightwards
        for i in range(lowestIndex + 1, len(ratings) - 1):
            if ratings[i] <= ratings[i + 1] and ratings[i] <= ratings[i - 1]:
                candies[i] = 1
                continue

            #if greater than neighbour add one else - 1
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
            else:
                candies[i] = candies[i - 1] - 1
                if(candies[i] == 0): #dont let a kid go below 1 candie
                    candies[i] += 1

        #sort out last index
        if ratings[len(ratings) - 1] <= ratings[len(ratings) - 2]:
            candies[len(ratings) - 1] = 1
        else:
            candies[len(ratings) - 1] = 1 + candies[len(ratings) - 2]

        #now move leftwards of lowest index
        for i in range(lowestIndex - 1, 0, -1):
            if ratings[i] <= ratings[i + 1] and ratings[i] <= ratings[i - 1]:
                candies[i] = 1
                continue
            
            if ratings [i] > ratings [i + 1]:
                candies[i] = candies[i + 1] + 1


        #sort out first index
        if ratings[0] <= ratings[1]:
            candies[0] = 1
        else:
            candies[0] = candies[1] + 1

        return candies


    def getLowestValue(self, list: list[int]) -> int:
        lowestValue = list[0]
        lowestIndex = 0

        for i in range(1, len(list)):
            x = list[i]
            if x < lowestValue:
                lowestValue = x
                lowestIndex = i

        return lowestIndex



def main():
    sol = Solution()
    test = [1,3,2,2,1]
    result = sol.candy(test)
    print(result)


if __name__ == '__main__':
    main()