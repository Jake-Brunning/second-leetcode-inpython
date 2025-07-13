class Solution:
    def matchPlayersAndTrainers(self, players: list[int], trainers: list[int]) -> int:
        players.sort()
        trainers.sort()

        # match each lowest player with each lowest trainer until we run out of trainers

        playerPointer = 0
        for trainerPointer in range(0, len(trainers)):
            if playerPointer == len(players):
                return playerPointer

            if players[playerPointer] <= trainers[trainerPointer]:
                playerPointer += 1

        return playerPointer

def main():
    sol = Solution()
    testTrainers = [8,2,5,8]
    testPlayers = [4,7,9]
    x = sol.matchPlayersAndTrainers(testPlayers, testTrainers)
    print(x)


if __name__ == '__main__':
    main()