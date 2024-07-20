# ASSIGNMENT SUBMITTED BY NISHANT SUBEDI (nishantsubedi.079@kathford.edu.np)

import random
import os

def createXs():
    flag = 0
    while True:
        r = random.randint(1, n)
        c = random.randint(1, m)
        if r != whereRow and c != whereCol:
            xlist.append(r)
            xlist.append(c)
            flag += 1
        if flag > 10:
            break

def showOHere(row, col):
    length = len(list)
    if length < 2:
        return False
    for i in range(0, length - 1, 2):
        if list[i] == row and list[i + 1] == col:
            return True
    return False

def checkForOut(choiceRow, choiceCol):
    i = 0
    length = len(xlist)
    for i in range(0, length - 1):
        if xlist[i] == choiceRow and xlist[i + 1] == choiceCol:
            return [True, xlist[i], xlist[i + 1]]
    return [False, 0, 0]

def mainGame():
    out = i = j = 0
    createXs()
    while True:
        choiceRow = int(input("Enter row to choose: "))
        choiceCol = int(input("Enter column to choose: "))
        if choiceRow > n or choiceCol > m or choiceCol < 1 or choiceRow < 1:
            print("\nInvalid choice, try again\n")
        else:
            os.system("cls" if os.name == "nt" else "clear")
            for i in range(1, n + 1):
                for j in range(1, m + 1):
                    y = checkForOut(choiceRow, choiceCol)
                    w, l, k = y
                    if w and l == i and k == j:
                        print("X", end=" ")
                        out = 1
                        continue
                    if choiceRow == whereRow and choiceCol == whereCol and i == whereRow and j == whereCol:
                        print("T", end=" ")
                        out = 2
                        continue
                    if choiceRow == i and choiceCol == j:
                        print("-", end=" ")
                        list.append(i)
                        list.append(j)
                        continue
                    if showOHere(i, j):
                        print("-", end=" ")
                        continue
                    print("*", end=" ")
                print()
                if i == n and out == 1:
                    print("You Loose!".center(50, "-"))
                    break
                if i == n and out == 2:
                    print("You Win!".center(50, "-"))
                    break
        if out != 0:
            print("Game Over".center(50, "-"))
            break

def startGame():
    os.system("cls" if os.name == "nt" else "clear")
    print("\nGAME STARTED\n\n")
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            print("*", end=" ")
        print()
    print()
    mainGame()

def createBoard():
    print("\nHere is your games board:\n")
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if whereRow == i and whereCol == j:
                print("T", end=" ")
                continue
            print("*", end=" ")
        print()

n = int(input("Enter the number of rows: "))
m = int(input("Enter the number of columns: "))
whereRow = int(input("Choose a row to hide the treasure (1 - " + str(n) + "): "))
if whereRow > n:
    print("Error value greater than game board row!")
else:
    whereCol = int(input("Choose a column to hide the treasure (1 - " + str(m) + "): "))
    if whereCol > m:
        print("Error value greater than game board row")
    else:
        xlist = list()
        list = list()
        createBoard()
        print("Press enter to start the game")
        input()
        startGame()
