import random


name = input("Enter your name: ")
print("Welcome ", name)
print("==============================================")
print("Try to guess the City Name in less than 10 attempts")
print("Good Luck!")
print("==============================================")


def hangman():

    word = random.choice(["mumbai", "delhi", "banglore", "hyderabad", "chennai", "kolkata", "pune", "jaipur", "lucknow", "kanpur", "nagpur", "bhopal",
                          "patna", "agra", "allahbad", "kota", "shimla", "satara", "dhule", "jammu", "thane", "indore", "bhopal"])
    validChoices = "abcdefghijklmnopqrstuvwxyz"
    guessmade = ""
    turns = 10

    guess_list = []


    while len(word)>0:
        main = ""

        for alphabet in word:
            if alphabet in guessmade:
                main = main + alphabet
            else:
                main = main + "_" + " "

        if main == word:
            print("You crack the word :", word)
            print("Congratulations, You Win!")
            break

        print("Guess the word :", main)
        guess = input()

        if guess in validChoices:
            guessmade = guessmade + guess
            if guess not in word:
                print("That letter isn't here")
                turns = turns - 1
                if turns == 9:
                    print("9 turns left")
                    print(" ----- ")
                if turns == 8:
                    print("8 turns left")
                    print(" ----- ")
                    print("     O ")
                if turns == 7:
                    print("7 turns left")
                    print(" ----- ")
                    print("     O ")
                    print("     | ")
                if turns == 6:
                    print("6 turns left")
                    print(" ----- ")
                    print("     O ")
                    print("     | ")
                    print("    /  ")
                if turns == 5:
                    print("5 turns left")
                    print(" ----- ")
                    print("     O ")
                    print("     | ")
                    print("    / \ ")
                if turns == 4:
                    print("4 turns left")
                    print(" ----- ")
                    print("   \ O ")
                    print("     | ")
                    print("    / \ ")
                if turns == 3:
                    print("3 turns left")
                    print(" ----- ")
                    print("   \ O /")
                    print("     | ")
                    print("    / \ ")
                if turns == 2:
                    print("2 turns left")
                    print(" --------- ")
                    print("       \ O /  |")
                    print("         | ")
                    print("        / \ ")
                if turns == 1:
                    print("1 turns left")
                    print(" --------- ")
                    print("       \ O _|/ ")
                    print("         | ")
                    print("        / \ ")
                if turns == 0:
                    print("You Loose!")
                    print("You let a kind man die!")
                    print(" --------- ")
                    print("         | ")
                    print("         O_| ")
                    print("        /|\ ")
                    print("        / \ ")
                    break

            elif guess == "":
                print("Enter something, don't u want to play?!")
            elif guess in guess_list:
                print("You have already guessed that letter!")
                print("Here is what you have guessed before :", guess_list)
            else:
                guess_list.append(guess)
        else:
            print("Enter Valid Character")
            print("Warning: 1. Character should not be in Uppercase")
            print("         2. Character should not be a Numeric Value")
            print("         3. Do not enter more than one value at a time")

    select = input("Do you want to continue yes or no :")
    if select == "yes":
        hangman()
    else:
        print("Thanks for playing!")


hangman()
print()

