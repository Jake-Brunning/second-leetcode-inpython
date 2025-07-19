class Solution:
    def removeSubfolders(self, folder: list[str]) -> list[str]:
        toReturn = []
        hashedFolder = set(folder)

        for fol in folder:
            # go through rest of folders and check if this starts with any of them
          
                
            if self.checkSubfolder(fol, hashedFolder):
                toReturn.append(fol)
    
        return toReturn

    def checkSubfolder(self, folder: str, hashedFolder: set[str]) -> bool:
        temp = "/"
        for i in range(1, len(folder) - 1):
            charLookingAt = folder[i]
            if charLookingAt == '/':
                if temp in hashedFolder:
                    return False

            temp += charLookingAt    
            
        return True
            
            



def main():
    sol = Solution()
    test =["/a","/a/b","/c/d","/c/d/e","/c/f"]
    x = sol.removeSubfolders(test)
    print(x)

if __name__ == '__main__':
    main()