class Solution:
    def isValid(self, word: str) -> bool:
        MINCHARS = 3
        if (len(word) < MINCHARS):
            return False
        
        # convert the word to lowercase so its easier
        word = word.upper()
        
        vowelCount = 0
        MINVOWELS = 1 # inclusive, 1 or more
        constantantCount = 0
        MINCONSTS = 1

        # check it has enough vowels + consts and it only contains digits and english letters
        for character in word:
            asciiVal = ord(character)

            # check its not digit or a letter (digits between 48-57 incl, letters )
            if (asciiVal < 48 or (asciiVal > 57 and asciiVal < 65) or (asciiVal > 90)):
                return False
        
            if(character == 'A' or character == 'E' or character == 'I' or character == 'O' or character == 'U'):
                vowelCount += 1
            elif(asciiVal <= 90 and asciiVal >= 65):
                constantantCount += 1

        if vowelCount >= MINVOWELS and constantantCount >= MINCONSTS:
            return True
        else:
            return False



def main():
    sol = Solution()


if __name__ == '__main__':
    main()