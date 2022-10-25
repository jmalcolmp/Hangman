import random

# Hangman photo
Hangman = ["\O_O/"]
# Word bank for Fruits
WordFruit = ["Apple", "Apricot", "Banana", "Blueberry", "Cherry", "Cherimoya", "Durian", "Feijoa", "Fig", "Grape",
             "Grape fruit", "Grilled pineapple", "Guava", "Honeydew", "Kiwi Fruit", "Lemon", "Lime", "Longan",
             "Dragon eyes", "Lychee", "Mandarin", "Mango", "Mangosteen", "Nashi", "Nectarine", "Orange",
             "Passion Fruit", "Pawpaw", "Papaya", "Peach", "Pear", "Persimmon", "Pineapple", "Plum", "Pomegranate",
             "Pomelo", "Citrus", "Rambutan", "Raspberry", "Rhubarb", "Rockmelon", "Star Fruit", "Carambola",
             "Strawberry", "Tamarillo", "Tangelo", "Watermelon"]

# Word bank for Vegetables
WordVeggies = ["Potato", "Avocado", "Celery", "Avocado", "Bean", "Beetroot", "Bok choy", "Pak Choy", "Chard",
               "Broccoli", "Brussels sprouts", "Cabbage", "Capsicum", "Carrot", "Parsnip", "Cauliflower",
               "Celeriac", "Celery", "Gai Lan", "Wong Bok", "Citrus coleslaw", "Corn", "Sweet Corn", "Cucumber",
               "Eggplant", "Aubergine", "Brinjal", "Fennel", "Lettuce", "Onion", "Peas", "Pumpkin", "Radish",
               "Spinach", "Squash",
               "Kumera", "Tabbouleh", "Tomato", "Turnip",
               "Zucchini", "Courgette"]

# Slang for Fruit or Vegetables
CatFruit = str(["Fruit", "Fruits"]).lower()
CatVeggies = str(["Veggies", "veggies", "Veggis",
                  "veggis", "Vegtables", "vegtables", "Vegetables", "vegetables"]).lower()
Yes = ["Yes", "Yeah", "Yea", "Sure", "Yup", "Yuppers", "Ok", "Okay", "Maybe", "Totally", "I do", "Y", " Yes", " Yeah",
       " Yea", " Sure", " Yup", " Yuppers", " Ok", " Okay", " Maybe", " Totally", " I do", " Y", "yes", "yeah", "yea",
       "sure", "yup", "yuppers", "ok", "okay", "maybe", "totally", "i do", "y", " yes", " yeah", " yea", " sure",
       " yup", " yuppers", " ok", " okay", " maybe", " totally", " i do", " y", "I'm ready", "i'm ready", " I'm ready",
       " i'm ready"]
guess = [0, 1, 2, 3, 4, 5]
guessedLetters = []
guessedWrong = []
guessLeft = guess[-1]


def hangman():
    # User Input
    choice = str(input("Please Choose a Category; Fruits, Veggies or Quit?: ")).lower()

    # Randomly chooses a word based off User Input
    if choice in CatFruit:
        wordFruit = str((random.choice(WordFruit))).lower()

        def miniGame1():
            while guess[-1] > 0:
                guessLetter = input("Please guess a letter or quit: ").lower()
                if guessLetter == wordFruit:
                    print("Congratz you won the game!")
                    hangman()
                elif guessLetter == "quit":
                    print("Game Over! The word was " + wordFruit)
                    quit()
                elif guessLetter in guessedLetters:
                    print("Please do not repeat letters \n")
                elif guessLetter in guessedWrong:
                    print("Please do not repeat letters \n")
                elif guessLetter in wordFruit:
                    print(guessLetter + " is a letter in the Fruit!")
                    guessedLetters.append(guessLetter)
                    print("Correct: " + str(guessedLetters) + " Wrong: " + str(guessedWrong) + "\n")
                else:
                    guess.pop(-1)
                    guessedWrong.append(guessLetter)
                    if guess[-1] <= 0:
                        print("Game Over! The word was " + wordFruit)
                        hangman()
                    else:
                        print("You used a guess attempt! There are " + str(guess[-1]) + " remaining")
                        print("Correct: " + str(guessedLetters) + " Wrong: " + str(guessedWrong) + "\n")
                        miniGame1()

        miniGame1()
        hangman()
    elif choice in CatVeggies:
        wordVeggies = str((random.choice(WordVeggies))).lower()

        def miniGame2():
            while guess[-1] > 0:
                guessLetter = input("Please guess a letter or quit: ").lower()
                if guessLetter == wordVeggies:
                    print("Congratz you won the game!")
                    hangman()
                elif guessLetter == "quit":
                    print("Game Over! The word was " + wordVeggies)
                    quit()
                elif guessLetter in guessedLetters:
                    print("Please do not repeat letters \n")
                elif guessLetter in guessedWrong:
                    print("Please do not repeat letters \n")
                elif guessLetter in wordVeggies:
                    print(guessLetter + " is a letter in the Veggie!")
                    guessedLetters.append(guessLetter)
                    print("Correct: " + str(guessedLetters) + " Wrong: " + str(guessedWrong) + "\n")
                else:
                    guess.pop(-1)
                    guessedWrong.append(guessLetter)
                    if guess[-1] <= 0:
                        print("Game Over! The word was " + wordVeggies)
                        hangman()
                    else:
                        print("You used a guess attempt! There are " + str(guess[-1]) + " remaining")
                        print("Correct: " + str(guessedLetters) + " Wrong: " + str(guessedWrong) + "\n")
                        miniGame2()

        miniGame2()
        hangman()
    else:
        leave = str(input("Would you like to exit?: "))
        if leave in Yes:
            exit()
        else:
            hangman()


hangman()
