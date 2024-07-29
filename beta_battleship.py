import random
import os
import sys
import time
from colorama import Fore, Back, Style
from ship_animations import ship_animation

# Creates a board for the player or computer

def createBoard(gridSize):

    board = [['O'] * int(gridSize) for col in range(int(gridSize))]    

    return board

# Prints a formatted board based on argument input

def printBoard(board):
    
    keys = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    print("   ", end="") #adds extra space before the print statement
    for item in range(1, len(board) + 1):
        end_str = " "
        if item > 9: # if number is two digits it will remove the space between them
            end_str = ""
        print("  " +  str(item).strip(), end = end_str)
    print("   ")
    for it in range(len(board)):
        print(keys[it] + ":", end = " | ")
        for item in range(len(board)):
            print(board[it][item], end = " | ")
        print(" ")

# Allows user and computer to shoot at each others ships

def bombTarget(userBomb, board, player, shipID1, shipID2, destName, destName2, subName, subName2):
        
    if player == "Player 1":

        if len(userBomb) > 4:
            while len(userBomb) > 4:
                print("\nInvalid input.")
                userBomb = input("\nInput a coordinate (Letter,Number): ")
        
        if "," not in userBomb:

            print("\nInvalid input.")
            userBomb = input("\nInput a coordinate (Letter,Number): ")
            bombTarget(userBomb, board, player, shipID1, shipID2, destName, destName2, subName, subName2)

        targetLoc = userBomb.split(",")
        xPos = targetLoc[0].capitalize()
        yPos = targetLoc[1]

        # Checks to see in X,Y if X is not a letter or Y is not a number

        if xPos.isalpha() == False:

            print("\nInvalid input.")
            userBomb = input("\nInput a coordinate (Letter,Number): ")
            bombTarget(userBomb, board, player, shipID1, shipID2, destName, destName2, subName, subName2)
            
        try:

            yPos = int(targetLoc[1])

        except ValueError:

            print("\nInvalid input.")
            userBomb = input("\nInput a coordinate (Letter,Number): ")
            bombTarget(userBomb, board, player, shipID1, shipID2, destName, destName2, subName, subName2)

        targetLoc = userBomb.split(",")
        xPos = targetLoc[0].capitalize()
        yPos = int(targetLoc[1])

        if yPos > gridSize or yPos < 1:

            print("\nInvalid input.")
            userBomb = input("\nInput a coordinate (Letter,Number): ")
            bombTarget(userBomb, board, player, shipID1, shipID2, destName, destName2, subName, subName2)

        placehold = f"({xPos},{yPos})"
        xLetter = strConvert(xPos)

        if board[xLetter][yPos - 1] == Fore.CYAN + "X" + Fore.RESET or board[xLetter][yPos - 1] == Fore.RED + "~" + Fore.RESET:
            
            print("\nYou have already attacked this spot.")
            userBomb = input("\nInput a coordinate (Letter,Number): ")
            bombTarget(userBomb, board, player, shipID1, shipID2, destName, destName2, subName, subName2)
    
        scoordlist = shipID2.get(destName2)
        sscoordlist = shipID2.get(subName2)
        counter = 0  
        
        if placehold in scoordlist:

            board[xLetter][yPos - 1] = Fore.RED + "~" + Fore.RESET
            scoordlist.remove(placehold)

            if counter > 0:
                ""
            else:

                ship_animation(1)
                counter += 1

            print("\nYou Hit!")
            shipID2.update({destName2: scoordlist})
            
        elif placehold in sscoordlist:

            board[xLetter][yPos - 1] = Fore.RED + "~" + Fore.RESET
            sscoordlist.remove(placehold)

            if counter > 0:
                ""
            else:

                ship_animation(1)
                counter += 1

            print("\nYou Hit!")
            shipID2.update({subName2: sscoordlist})
        
        elif placehold not in scoordlist:

            board[xLetter][yPos - 1] = Fore.CYAN + "X" + Fore.RESET

            if counter > 0:
                ""
            else:
                ship_animation(0)
                counter += 1

   
        
        elif placehold not in sscoordlist:

            board[xLetter][yPos - 1] = Fore.CYAN + "X" + Fore.RESET

            if counter > 0:
                ""
            else:
                ship_animation(0)
                counter += 1

         
 
    elif player == "Player 2":

        bombX = random.randint(0, gridSize - 1)
        xLetter = strConvert(bombX)
        bombY = random.randint(0,gridSize - 1)
        placeholdc = f"({xLetter},{bombY})"

        scoordlist2 = shipID1.get(destName)
        sscoordlist2 = shipID1.get(subName)
        

        if placeholdc in scoordlist2:

            board[bombX][bombY - 1] = Fore.RED + "~" + Fore.RESET
            scoordlist2.remove(placeholdc)
            ship_animation(1)
            print("\nThe Computer Hit!")
            shipID1.update({destName: scoordlist2})
            
        elif placeholdc in sscoordlist2:

            board[bombX][bombY - 1] = Fore.RED + "~" + Fore.RESET
            sscoordlist2.remove(placeholdc)
            ship_animation(1)
            print("\nThe Computer Hit!")
            shipID2.update({subName2: sscoordlist2})

        elif placeholdc not in scoordlist2:

            board[bombX][bombY] = Fore.CYAN + "X" + Fore.RESET
            ship_animation(0)
            print("\nThe Computer Missed!\n")
        
        elif placeholdc not in sscoordlist2:

            board[bombX][bombY] = Fore.CYAN + "X" + Fore.RESET
            ship_animation(0)
            print("\nThe Computer Missed!\n")
        

#Creates destroyers

def createDest(gridSize, placementType, board, player, shipID1, shipID2):
        
    if placementType == 1:

        if player == "Player 1":
            
            orientation = random.randint(0,1)
            generateX = random.randint(0,gridSize - 1)
            xLetter = strConvert(generateX)
            generateY = random.randint(1,gridSize - 1)
            str_correlate = f"({xLetter},{generateY})"
            destName = input("\nName your first ship: ")
            

            if orientation == 1:
            
            #vertical orientation & extremes

                if generateX == 0:

                    board[generateX][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                    board[generateX + 1][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                    xLetter2 = strConvert(generateX + 1)
                    str_correlate2 = f"({xLetter2},{generateY})"


                elif generateX == (gridSize - 1):

                    board[generateX][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                    board[generateX - 1][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                    xLetter2 = strConvert(generateX - 1)
                    str_correlate2 = f"({xLetter2},{generateY})"
                    
   

                else:
                    
                    # centered vertical
                    toporbottom = random.randint(0,1)

                    if toporbottom == 0:

                        #top
                        board[generateX][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                        board[generateX - 1][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                        xLetter2 = strConvert(generateX - 1)
                        str_correlate2 = f"({xLetter2},{generateY})"
                        
                 

                    elif toporbottom == 1:

                        #bottom
                        board[generateX][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                        board[generateX + 1][generateY - 1] = Fore.GREEN + "#" + Fore.RESET 
                        xLetter2 = strConvert(generateX + 1)
                        str_correlate2 = f"({xLetter2},{generateY})"
                        
                     

            elif orientation == 0:

            #horizontal extremes
        
                if generateY == 1:

                    board[generateX][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                    board[generateX][generateY] = Fore.GREEN + "#" + Fore.RESET
                    xLetter2 = strConvert(generateX)
                    str_correlate2 = f"({xLetter2},{generateY + 1})"
                    
               

                elif generateY == (gridSize - 1):

                    board[generateX][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                    board[generateX][generateY - 2] = Fore.GREEN + "#" + Fore.RESET
                    xLetter2 = strConvert(generateX)
                    str_correlate2 = f"({xLetter2},{generateY - 1})"
                    
          

                else:

                    # centered horizontal
                    toporbottom = random.randint(0,1)

                    if toporbottom == 0:

                        #right
                        board[generateX][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                        board[generateX][generateY] = Fore.GREEN + "#" + Fore.RESET
                        xLetter2 = strConvert(generateX)
                        str_correlate2 = f"({xLetter2},{generateY + 1})"
                    

                    elif toporbottom == 1:

                        #left
                        board[generateX][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                        board[generateX][generateY - 2] = Fore.GREEN + "#" + Fore.RESET
                        xLetter2 = strConvert(generateX)
                        str_correlate2 = f"({xLetter2},{generateY - 1})"
                 
                    
            coordlist = [str_correlate,str_correlate2]
            shipID1.update({destName: coordlist})
            print(shipID1)
            return destName

        elif player == "Player 2":

            orientation = random.randint(0,1)
            generateX = random.randint(0,gridSize - 1)
            xLetter = strConvert(generateX)

            generateY = random.randint(1,gridSize - 1)
            str_correlate = f"({xLetter},{generateY})"

            shipNameChoice = random.randint(0,5)
            destName2 = f"USS {shipNamePoss[shipNameChoice]}"

            if orientation == 1:
            
            #vertical orientation & extremes

                if generateX == 0:

                    board[generateX][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                    board[generateX + 1][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                    xLetter2 = strConvert(generateX + 1)
                    str_correlate2 = f"({xLetter2},{generateY})"


                elif generateX == (gridSize - 1):

                    board[generateX][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                    board[generateX - 1][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                    xLetter2 = strConvert(generateX - 1)
                    str_correlate2 = f"({xLetter2},{generateY})"
                    

                else:
                    
                    # centered vertical
                    toporbottom = random.randint(0,1)

                    if toporbottom == 0:

                        #top
                        board[generateX][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                        board[generateX - 1][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                        xLetter2 = strConvert(generateX - 1)
                        str_correlate2 = f"({xLetter2},{generateY})"
                        

                    elif toporbottom == 1:

                        #bottom
                        board[generateX][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                        board[generateX + 1][generateY - 1] = Fore.GREEN + "#" + Fore.RESET 
                        xLetter2 = strConvert(generateX + 1)
                        str_correlate2 = f"({xLetter2},{generateY})"
                        

            elif orientation == 0:

            #horizontal extremes
        
                if generateY == 1:

                    board[generateX][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                    board[generateX][generateY] = Fore.GREEN + "#" + Fore.RESET
                    xLetter2 = strConvert(generateX)
                    str_correlate2 = f"({xLetter2},{generateY + 1})"
                    

                elif generateY == (gridSize - 1):

                    board[generateX][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                    board[generateX][generateY - 2] = Fore.GREEN + "#" + Fore.RESET
                    xLetter2 = strConvert(generateX)
                    str_correlate2 = f"({xLetter2},{generateY - 1})"
                    

                else:

                    # centered horizontal
                    toporbottom = random.randint(0,1)

                    if toporbottom == 0:

                        #right
                        board[generateX][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                        board[generateX][generateY] = Fore.GREEN + "#" + Fore.RESET
                        xLetter2 = strConvert(generateX)
                        str_correlate2 = f"({xLetter2},{generateY + 1})"
                        

                    elif toporbottom == 1:

                        #left
                        board[generateX][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                        board[generateX][generateY - 2] = Fore.GREEN + "#" + Fore.RESET
                        xLetter2 = strConvert(generateX)
                        str_correlate2 = f"({xLetter2},{generateY - 1})"
                        
            coordlist2 = [str_correlate,str_correlate2]
            shipID2[destName2] = coordlist2
            return destName2
        
    elif placementType == 0:

        if player == "Player 1":

            #Manual Placement
            printBoard(board)
            destName = input("\nName your first ship: ")

            # Converts coordinates to indexes, Letter[0] & number[1]
            shipLoc = input("Input a coordinate to sail your ship: ")
            parkedShip = shipLoc.split(",")

            xLetter = parkedShip[0]
            yNumber = int(parkedShip[1])
            # yNumber = parkedShip[1]

            # Formats the coordinates & adds them to the destroyer list
            str_correlate = f"({xLetter},{yNumber})"
            newCol = strConvert(xLetter)

            board[newCol][yNumber - 1] = Fore.GREEN + "#" + Fore.RESET
            shipLoc2 = input("Enter the coordinates of an adjacent cell vertically or horizontally: ")
            parkedShip2 = shipLoc2.split(",")
            xLetter2 = parkedShip2[0]
            yNumber2 = int(parkedShip2[1])
            str_correlate2 = f"({xLetter2},{yNumber})"

            newCol = strConvert(xLetter2)
            board[newCol][yNumber2 -1] = Fore.GREEN + "#" + Fore.RESET
            coordlist = [str_correlate,str_correlate2]
            shipID1[destName] = coordlist
            print(shipID1)
            return destName

        elif player == "Player 2":

            orientation = random.randint(0,1)
            generateX = random.randint(0,gridSize - 1)
            xLetter = strConvert(generateX)
            generateY = random.randint(1,gridSize - 1)
            str_correlate = f"({xLetter},{generateY})"

            shipNameChoice = random.randint(0,5)
            destName2 = f"USS {shipNamePoss[shipNameChoice]}"

            if orientation == 1:
            
            #vertical orientation & extremes

                if generateX == 0:

                    board[generateX][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                    board[generateX + 1][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                    xLetter2 = strConvert(generateX + 1)
                    str_correlate2 = f"({xLetter2},{generateY})"


                elif generateX == (gridSize - 1):

                    board[generateX][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                    board[generateX - 1][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                    xLetter2 = strConvert(generateX - 1)
                    str_correlate2 = f"({xLetter2},{generateY})"
                    

                else:
                    
                    # centered vertical
                    toporbottom = random.randint(0,1)

                    if toporbottom == 0:

                        #top
                        board[generateX][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                        board[generateX - 1][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                        xLetter2 = strConvert(generateX - 1)
                        str_correlate2 = f"({xLetter2},{generateY})"
                        

                    elif toporbottom == 1:

                        #bottom
                        board[generateX][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                        board[generateX + 1][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                        xLetter2 = strConvert(generateX + 1)
                        str_correlate2 = f"({xLetter2},{generateY})"
                        

            elif orientation == 0:

            #horizontal extremes
        
                if generateY == 1:

                    board[generateX][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                    board[generateX][generateY] = Fore.GREEN + "#" + Fore.RESET
                    xLetter2 = strConvert(generateX)
                    str_correlate2 = f"({xLetter2},{generateY + 1})"
                    

                elif generateY == (gridSize - 1):

                    board[generateX][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                    board[generateX][generateY - 2] = Fore.GREEN + "#" + Fore.RESET
                    xLetter2 = strConvert(generateX)
                    str_correlate2 = f"({xLetter2},{generateY - 1})"
                    

                else:

                    # centered horizontal
                    toporbottom = random.randint(0,1)

                    if toporbottom == 0:

                        #right
                        board[generateX][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                        board[generateX][generateY] = Fore.GREEN + "#" + Fore.RESET
                        xLetter2 = strConvert(generateX)
                        str_correlate2 = f"({xLetter2},{generateY + 1})"
                        

                    elif toporbottom == 1:

                        #left
                        board[generateX][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                        board[generateX][generateY - 2] = Fore.GREEN + "#" + Fore.RESET
                        xLetter2 = strConvert(generateX)
                        str_correlate2 = f"({xLetter2},{generateY - 1})"

            coordlist2 = [str_correlate,str_correlate2]
            shipID2[destName2] = coordlist2
            return destName2

#Creates Subs

def createSub(gridSize, placementType, board, player, shipID1, shipID2):

    if placementType == 1:

        str_correlate3 = ""

        if player == "Player 1":

            orientation = random.randint(0,1)
            generateX2 = random.randint(0,gridSize - 1)
            xLetter = strConvert(generateX2)

            generateY = random.randint(1,gridSize - 1)
            str_correlate = f"({xLetter},{generateY})"

            subName = input("\nName your second ship: ")


            if orientation == 1:

                #vertical orientation & extremes

                if generateX2 == 0:

                    if board[generateX2][generateY - 1] == Fore.GREEN + "#" + Fore.RESET or board[generateX2 + 1][generateY - 1] == Fore.GREEN + "#" + Fore.RESET:

                        print("\nYour second ship was auto-generated at the same location as the first one. Please Restart.\n")
                        createSub(gridSize, placementType, board, player, shipID1, shipID2)

                    board[generateX2][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                    board[generateX2 + 1][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                    xLetter2 = strConvert(generateX2 + 1)
                    str_correlate2 = f"({xLetter2},{generateY})"
                    printBoard(board)

                elif generateX2 == (gridSize - 1):

                    if board[generateX2][generateY - 1] == Fore.GREEN + "#" + Fore.RESET or board[generateX2 - 1][generateY - 1] == Fore.GREEN + "#" + Fore.RESET:

                        print("\nYour second ship was auto-generated at the same location as the first one.\n")
                        createSub(gridSize, placementType, board, player, shipID1, shipID2)

                    board[generateX2][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                    board[generateX2 - 1][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                    xLetter2 = strConvert(generateX2 - 1)
                    str_correlate2 = f"({xLetter2},{generateY})"

                   

                else:

                    # centered vertical
                    toporbottom = random.randint(0,1)

                    if toporbottom == 0:

                        #top

                        if board[generateX2][generateY - 1] == Fore.GREEN + "#" + Fore.RESET or board[generateX2 - 1][generateY - 1] == Fore.GREEN + "#" + Fore.RESET:

                            print("\nYour second ship was auto-generated at the same location as the first one.\n")
                            createSub(gridSize, placementType, board, player, shipID1, shipID2)

                        board[generateX2][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                        board[generateX2 - 1][generateY - 1] = Fore.GREEN + "#" + Fore.RESET

                        xLetter2 = strConvert(generateX2 - 1)
                        str_correlate2 = f"({xLetter2},{generateY})"
                

                    elif toporbottom == 1:

                        #bottom

                        if board[generateX2][generateY - 1] == Fore.GREEN + "#" + Fore.RESET or board[generateX2 + 1][generateY - 1] == Fore.GREEN + "#" + Fore.RESET:

                            print("\nYour second ship was auto-generated at the same location as the first one.\n")
                            createSub(gridSize, placementType, board, player, shipID1, shipID2)

                        board[generateX2][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                        board[generateX2 + 1][generateY - 1] = Fore.GREEN + "#" + Fore.RESET 
                        xLetter2 = strConvert(generateX2 + 1)
                        str_correlate2 = f"({xLetter2},{generateY})"
                        
                   

            elif orientation == 0:

                #horizontal extremes

                if generateY == 1:

                    if board[generateX2][generateY - 1] == Fore.GREEN + "#" + Fore.RESET or board[generateX2][generateY] == Fore.GREEN + "#" + Fore.RESET:

                        print("\nYour second ship was auto-generated at the same location as the first one.\n")
                        createSub(gridSize, placementType, board, player, shipID1, shipID2)

                    board[generateX2][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                    board[generateX2][generateY] = Fore.GREEN + "#" + Fore.RESET
                    xLetter2 = strConvert(generateX2)
                    str_correlate2 = f"({xLetter2},{generateY + 1})"

                  
                elif generateY == (gridSize - 1):

                    #bottom

                    if board[generateX2][generateY - 1] == Fore.GREEN + "#" + Fore.RESET or board[generateX2][generateY - 2] == Fore.GREEN + "#" + Fore.RESET:

                        print("\nYour second ship was auto-generated at the same location as the first one.\n")
                        createSub(gridSize, placementType, board, player, shipID1, shipID2)

                    board[generateX2][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                    board[generateX2][generateY - 2] = Fore.GREEN + "#" + Fore.RESET
                    xLetter2 = strConvert(generateX2)
                    str_correlate2 = f"({xLetter2},{generateY - 1})"

                 

                else:

                    # centered horizontal
                    toporbottom = random.randint(0,1)

                    if toporbottom == 0:

                        #right

                        if board[generateX2][generateY - 1] == Fore.GREEN + "#" + Fore.RESET or board[generateX2][generateY] == Fore.GREEN + "#" + Fore.RESET:

                            print("\nYour second ship was auto-generated at the same location as the first one.\n")
                            createSub(gridSize, placementType, board, player, shipID1, shipID2)

                        board[generateX2][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                        board[generateX2][generateY] = Fore.GREEN + "#" + Fore.RESET
                        xLetter2 = strConvert(generateX2)
                        str_correlate2 = f"({xLetter2},{generateY + 1})"
                        
                     

                    elif toporbottom == 1:

                            #left

                            if board[generateX2][generateY - 1] == Fore.GREEN + "#" + Fore.RESET or board[generateX2][generateY] == Fore.GREEN + "#" + Fore.RESET:

                                print("\nYour second ship was auto-generated at the same location as the first one.\n")
                                createSub(gridSize, placementType, board, player, shipID1, shipID2)

                            board[generateX2][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                            board[generateX2][generateY - 2] = Fore.GREEN + "#" + Fore.RESET

                            xLetter2 = strConvert(generateX2)
                            str_correlate2 = f"({xLetter2},{generateY - 1})"
               
    

            coordlist = [str_correlate,str_correlate2]
            shipID1.update({subName: coordlist})
            print(shipID1)
            return subName

        elif player == "Player 2":

            orientation = random.randint(0,1)
            generateX2 = random.randint(0,gridSize - 1)
            xLetter = strConvert(generateX2)

            generateY = random.randint(1,gridSize - 1)
            str_correlate = f"({xLetter},{generateY})"

            if orientation == 1:

                #vertical orientation & extremes
                if generateX2 == 0:

                    if board[generateX2][generateY - 1] == Fore.GREEN + "#" + Fore.RESET or board[generateX2 + 1][generateY - 1] == Fore.GREEN + "#" + Fore.RESET:

                        createSub(gridSize, placementType, board, player, shipID1, shipID2)

                    board[generateX2][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                    board[generateX2 + 1][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                    xLetter2 = strConvert(generateX2 + 1)
                    str_correlate3 = f"({xLetter2},{generateY})"


                elif generateX2 == (gridSize - 1):

                    if board[generateX2][generateY - 1] == Fore.GREEN + "#" + Fore.RESET or board[generateX2 - 1][generateY - 1] == Fore.GREEN + "#" + Fore.RESET:

                        createSub(gridSize, placementType, board, player, shipID1, shipID2)

                    board[generateX2][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                    board[generateX2 - 1][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                    xLetter2 = strConvert(generateX2 - 1)
                    str_correlate3 = f"({xLetter2},{generateY})"


                else:

                    # centered vertical
                    toporbottom = random.randint(0,1)

                    if toporbottom == 0:

                        #top

                        if board[generateX2][generateY - 1] == Fore.GREEN + "#" + Fore.RESET or board[generateX2 - 1][generateY - 1] == Fore.GREEN + "#" + Fore.RESET:

                            createSub(gridSize, placementType, board, player, shipID1, shipID2)

                        board[generateX2][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                        board[generateX2 - 1][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                        xLetter2 = strConvert(generateX2 - 1)
                        str_correlate3 = f"({xLetter2},{generateY})"

                    elif toporbottom == 1:

                        #bottom

                        if board[generateX2][generateY - 1] == Fore.GREEN + "#" + Fore.RESET or board[generateX2 + 1][generateY - 1] == Fore.GREEN + "#" + Fore.RESET:

                            createSub(gridSize, placementType, board, player, shipID1, shipID2)

                        board[generateX2][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                        board[generateX2 + 1][generateY - 1] = Fore.GREEN + "#" + Fore.RESET 
                        xLetter2 = strConvert(generateX2 + 1)
                        str_correlate3 = f"({xLetter2},{generateY})"


            elif orientation == 0:

                #horizontal extremes

                if generateY == 1:

                    if board[generateX2][generateY - 1] == Fore.GREEN + "#" + Fore.RESET or board[generateX2][generateY] == Fore.GREEN + "#" + Fore.RESET:

                        createSub(gridSize, placementType, board, player, shipID1, shipID2)

                    board[generateX2][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                    board[generateX2][generateY] = Fore.GREEN + "#" + Fore.RESET
                    xLetter2 = strConvert(generateX2)
                    str_correlate3 = f"({xLetter2},{generateY + 1})"


                elif generateY == (gridSize - 1):

                    if board[generateX2][generateY - 1] == Fore.GREEN + "#" + Fore.RESET or board[generateX2][generateY - 2] == Fore.GREEN + "#" + Fore.RESET:

                        createSub(gridSize, placementType, board, player, shipID1, shipID2)

                    board[generateX2][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                    board[generateX2][generateY - 2] = Fore.GREEN + "#" + Fore.RESET
                    xLetter2 = strConvert(generateX2)
                    str_correlate3 = f"({xLetter2},{generateY - 1})"


                else:

                    # centered horizontal
                    toporbottom = random.randint(0,1)

                    if toporbottom == 0:

                        #right

                        if board[generateX2][generateY - 1] == Fore.GREEN + "#" + Fore.RESET or board[generateX2][generateY] == Fore.GREEN + "#" + Fore.RESET:

                            createSub(gridSize, placementType, board, player, shipID1, shipID2)

                        board[generateX2][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                        board[generateX2][generateY] = Fore.GREEN + "#" + Fore.RESET
                        xLetter2 = strConvert(generateX2)
                        str_correlate3 = f"({xLetter2},{generateY + 1})"

                    elif toporbottom == 1:

                        #left

                        if board[generateX2][generateY - 1] == Fore.GREEN + "#" + Fore.RESET or board[generateX2][generateY - 2] == Fore.GREEN + "#" + Fore.RESET:

                            createSub(gridSize, placementType, board, player, shipID1, shipID2)

                        board[generateX2][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                        board[generateX2][generateY - 2] = Fore.GREEN + "#" + Fore.RESET
                        xLetter2 = strConvert(generateX2)
                        str_correlate3 = f"({xLetter2},{generateY - 1})"

            shipNameChoice = random.randint(0,5)
            subName2 = f"USS {subNamePoss[shipNameChoice]}"
            coordlist2 = [str_correlate,str_correlate3]
            shipID2.update({subName2: coordlist2})
            return subName2

    elif placementType == 0:

        if player == "Player 1":

            #Manual Placement
           
            subName = input("\nName your second ship: ")

            # Converts coordinates to indexes, Letter[0] & number[1]
            shipLoc = input("Input a coordinate to sail your ship: ")
            parkedShip = shipLoc.split(",")
            xLetter = parkedShip[0]
            yNumber = int(parkedShip[1])

            # Formats the coordinates & adds them to the ship list
            str_correlate = f"({xLetter},{yNumber})"
            newCol = strConvert(xLetter)

            if board[newCol][yNumber] == Fore.GREEN + "#" + Fore.RESET:

                print("\nYou are trying to place your second ship atop your first. Restart.\n")
                createSub(gridSize, placementType, board, player, shipID1, shipID2)

            board[newCol][yNumber - 1] = "#"
            shipLoc2 = input("Enter the coordinates of an adjacent cell vertically or horizontally: ")
            parkedShip2 = shipLoc2.split(",")
            xLetter2 = parkedShip2[0]
            yNumber2 = int(parkedShip2[1])
            str_correlate2 = f"({xLetter2},{yNumber})"

            newCol = strConvert(xLetter2)

            if board[newCol][yNumber2] == Fore.GREEN + "#" + Fore.RESET:

                print("\nYou are trying to place your second ship atop your first. Restart.\n")
                createSub(gridSize, placementType, board, player, shipID1, shipID2)


            board[newCol][yNumber2 -1] = "#"
            coordlist = [(str_correlate,str_correlate2)]
            shipID1.update({subName: coordlist})
            print(shipID1)
            return subName

        elif player == "Player 2":

            orientation = random.randint(0,1)
            generateX2 = random.randint(0,gridSize - 1)
            xLetter = strConvert(generateX2)

            generateY = random.randint(1,gridSize - 1)
            str_correlate = f"({xLetter},{generateY})"

            if orientation == 1:

                #vertical orientation & extremes
                if generateX2 == 0:

                    if board[generateX2][generateY - 1] == Fore.GREEN + "#" + Fore.RESET or board[generateX2 + 1][generateY - 1] == Fore.GREEN + "#" + Fore.RESET:

                        createSub(gridSize, placementType, board, player, shipID1, shipID2)

                    board[generateX2][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                    board[generateX2 + 1][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                    xLetter2 = strConvert(generateX2 + 1)
                    str_correlate2 = f"({xLetter2},{generateY})"

                elif generateX2 == (gridSize - 1):

                    if board[generateX2][generateY - 1] == Fore.GREEN + "#" + Fore.RESET or board[generateX2 - 1][generateY - 1] == Fore.GREEN + "#" + Fore.RESET:

                        createSub(gridSize, placementType, board, player, shipID1, shipID2)

                    board[generateX2][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                    board[generateX2 - 1][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                    xLetter2 = strConvert(generateX2 - 1)
                    str_correlate2 = f"({xLetter2},{generateY})"

                else:

                    # centered vertical
                    toporbottom = random.randint(0,1)

                    if toporbottom == 0:

                        #top

                        if board[generateX2][generateY - 1] == Fore.GREEN + "#" + Fore.RESET or board[generateX2 - 1][generateY - 1] == Fore.GREEN + "#" + Fore.RESET:

                            createSub(gridSize, placementType, board, player, shipID1, shipID2)

                        board[generateX2][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                        board[generateX2 - 1][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                        xLetter2 = strConvert(generateX2 - 1)
                        str_correlate2 = f"({xLetter2},{generateY})"

                    elif toporbottom == 1:

                        #bottom

                        if board[generateX2][generateY - 1] == Fore.GREEN + "#" + Fore.RESET or board[generateX2 + 1][generateY - 1] == Fore.GREEN + "#" + Fore.RESET:

                            createSub(gridSize, placementType, board, player, shipID1, shipID2)

                        board[generateX2][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                        board[generateX2 + 1][generateY - 1] = Fore.GREEN + "#" + Fore.RESET 
                        xLetter2 = strConvert(generateX2 + 1)
                        str_correlate2 = f"({xLetter2},{generateY})"


            elif orientation == 0:

                #horizontal extremes

                if generateY == 1:

                    if board[generateX2][generateY - 1] == Fore.GREEN + "#" + Fore.RESET or board[generateX2][generateY] == Fore.GREEN + "#" + Fore.RESET:

                        createSub(gridSize, placementType, board, player, shipID1, shipID2)

                    board[generateX2][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                    board[generateX2][generateY] = Fore.GREEN + "#" + Fore.RESET
                    xLetter2 = strConvert(generateX2)
                    str_correlate2 = f"({xLetter2},{generateY + 1})"


                elif generateY == (gridSize - 1):

                    if board[generateX2][generateY - 1] == Fore.GREEN + "#" + Fore.RESET or board[generateX2][generateY - 2] == Fore.GREEN + "#" + Fore.RESET:

                        createSub(gridSize, placementType, board, player, shipID1, shipID2)

                    board[generateX2][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                    board[generateX2][generateY - 2] = Fore.GREEN + "#" + Fore.RESET
                    xLetter2 = strConvert(generateX2)
                    str_correlate2 = f"({xLetter2},{generateY - 1})"

                else:

                    # centered horizontal
                    toporbottom = random.randint(0,1)

                    if toporbottom == 0:    

                        #right

                        if board[generateX2][generateY - 1] == Fore.GREEN + "#" + Fore.RESET or board[generateX2][generateY] == Fore.GREEN + "#" + Fore.RESET:

                            createSub(gridSize, placementType, board, player, shipID1, shipID2)

                        board[generateX2][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                        board[generateX2][generateY] = Fore.GREEN + "#" + Fore.RESET
                        xLetter2 = strConvert(generateX2)
                        str_correlate2 = f"({xLetter2},{generateY + 1})"

                    elif toporbottom == 1:

                        #left

                        if board[generateX2][generateY - 1] == Fore.GREEN + "#" + Fore.RESET or board[generateX2][generateY - 2] == Fore.GREEN + "#" + Fore.RESET:

                            createSub(gridSize, placementType, board, player, shipID1, shipID2)

                        board[generateX2][generateY - 1] = Fore.GREEN + "#" + Fore.RESET
                        board[generateX2][generateY - 2] = Fore.GREEN + "#" + Fore.RESET
                        xLetter2 = strConvert(generateX2)
                        str_correlate2 = f"({xLetter2},{generateY - 1})"

            shipNameChoice = random.randint(0,5)
            subName2 = subName2 = f"USS {subNamePoss[shipNameChoice]}"
            coordlist2 = [str_correlate,str_correlate2]
            shipID2.update({subName2: coordlist2})
            return subName2


# Converts a number to a letter

def strConvert(col):
    keys = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

    if str(col).isalpha() == True:
            
        # If col is a string, find its index in the keys list
        try: 

            newCol = keys.index(col.capitalize())
        except: 
            # Handle the case where the string is not in keys
            raise ValueError("Invalid column value: " + col)
    
    elif str(col).isnumeric() == True:

        # If col is an integer, use it as an index to get the corresponding letter
        try:
            newCol = chr(col + 65)
        except:
            # Handle the case where the integer is out of range
            raise ValueError("Invalid column index: " + str(col))
    else:
        # Handle the case where col is neither a string nor an integer
        raise ValueError("Invalid column type: " + str(col))

    return newCol

#Checks for wins

def wincond(gooping, shipID1, shipID2, destName, destName2, subName, subName2):

    p1DestSunk = shipID2.get(destName2)
    p1SubSunk = shipID2.get(subName2)
    p2DestSunk = shipID1.get(destName)
    p2SubSunk = shipID1.get(subName)
    
    if len(p1DestSunk) == 0:

        print(f"{destName2} is sunk! ")

    if len(p1SubSunk) == 0:

        print(f"{subName2} is sunk!")

    if len(p2DestSunk) == 0:

        print(f"{destName} is sunk! ")

    if len(p2SubSunk) == 0:

        print(f"{subName} is sunk! ")
    

    if len(p1DestSunk) == 0 and len(p1SubSunk) == 0:
        gooping = False
        print("You Win!")
    elif len(p2DestSunk) == 0 and len(p2SubSunk) == 0:
        gooping = False
        print("The Computer Wins!")
    return gooping

gooping = True

shipID1 = {}

shipID2 = {}

coordlist = []

shipNamePoss = ["Glizzy Gang", "Chud Man", "Big Chungus", "Sussy Sigma", "Sleepy Joe", "Skibidi Slicer"]

subNamePoss = ["Lebonbon", "Boe Jiden", "Tonald Drump", "Fortiniteylababag", "Nah I'd Win", "Bush Camper"]

destName = ""

destName2 = ""

subName = ""

subName2 = ""


player = "Player 1"

# Basic standard welcome info 

print("\nWelcome to BattleShip!\n")
print("In BattleShip, two players engage in a turn-based battle, competing to sink all of the opponent's ships before they lose all of their own.\n")
print("Player 1 will start first. If an opposing ship is hit, your turn will continue. Otherwise, player 2's turn will begin.\n")

print("Ships that are " + Fore.BLUE + "sailing" + Fore.RESET + " will be " + Fore.GREEN + "Green" + Fore.RESET + " and ships that have been " + Fore.YELLOW + "sunk " + Fore.RESET + "are "+ Fore.RED + "Red.\n" + Fore.RESET)
  
gridSize = 10 # int(input("\nEnter your grid size (# input)[26 Max]: "))


# Board for player 1, shows ships & enemy attack coordinates
board = createBoard(gridSize)

# Board for computer's info
grid = createBoard(gridSize)

try:

    placementType = int(input("\nInput 1 to automatically place ships or 0 to manually place ships: "))

    if placementType < 0 or placementType > 1:

        while placementType < 0 or placementType > 1:

            placementType = int(input("\nInvalid input. 1 - Automatic | 0 - Manual Placement: "))

except ValueError:
    print("\nInvalid input.\n")
    time.sleep(1)
    os.execl(sys.executable, sys.executable, *sys.argv)

player = "Player 1"
destName = createDest(gridSize, placementType, board, player, shipID1, shipID2)
subName = createSub(gridSize, placementType, board, player, shipID1, shipID2)

# createSub(gridSize, placementType, board, player)

player = "Player 2"
destName2 = createDest(gridSize, placementType, grid, player, shipID1, shipID2)
subName2 = createSub(gridSize, placementType, grid, player, shipID1, shipID2)


while(gooping):

    player = "Player 1"
    print(f"\nIt is {player}'s turn.\n")

    print(shipID2)

    userBomb = input(f"\n{player}, Please select a section to hit with your artillery: ")
    bombTarget(userBomb, board, player,shipID1, shipID2, destName, destName2, subName, subName2)
    printBoard(board)
    gooping = wincond(gooping, shipID1, shipID2, destName, destName2, subName, subName2)

    if gooping == False:
        break

    time.sleep(2)

    # Sets player to computer

    player = "Player 2"
    print(f"\nIt is the computer's turn.\n")

    time.sleep(1)

    bombTarget(userBomb, grid, player,shipID1, shipID2, destName, destName2, subName, subName2)
    printBoard(board)
    gooping = wincond(gooping ,shipID1, shipID2, destName, destName2, subName, subName2)
    
    if gooping == False:
        break