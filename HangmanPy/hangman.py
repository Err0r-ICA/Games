import random


# Keep track of scores
player_score = 0
computer_score = 0


# Select random word from file
def word():
    word_list = open("words.txt", "r").readlines()
    random_number = random.randint(0, len(word_list))
    word = word_list[random_number].rstrip()
    return word



# Game graphics
def hanged(man):
    graphic = [
    '''
       +------+
       |
       |
       |
       |
       |
    ==============
    ''',
    '''
       +------+
       |      |
       |      O
       |
       |
       |
    ==============
    ''',
    '''
       +------+
       |      |
       |      O
       |      |
       |
       |
    ==============
    ''',
    '''
       +------+
       |      |
       |      O
       |     -|
       |
       |
    ==============
    ''',
    '''
       +------+
       |      |
       |      O
       |     -|-
       |
       |
    ==============
    ''',
    '''
       +------+
       |      |
       |      O
       |     -|-
       |     /
       |
    ==============
    ''',
    '''
       +------+
       |      |
       |      O
       |     -|-
       |     / \\
       |
    ==============
    '''
    ]
    return graphic[man]


# Game starter
def start():
    print("")
    print("Let's play Hangman!")
    print("")
    while game():
        pass
    print("")
    scores()


# The game and rules
def game():
    the_word = word()
    word_list = the_word.split()
    print("The word has {} letters.".format(len(the_word)))
    clue = len(the_word) * ["-"]
    print("")
    print("".join(clue))
    tries = 6
    letters_tried = ""
    guesses = 0
    letters_right = 0
    letters_wrong = 0
    global computer_score, player_score

    while (letters_wrong != tries) and ("".join(clue) != the_word):
        letter = guess_letter()
        if len(letter) == 1 and letter.isalpha():
            if letters_tried.find(letter) != -1:
                print("You've already picked", letter)
            else:
                letters_tried += letter
                first_index = the_word.find(letter)
                if first_index == -1:
                    letters_wrong += 1
                    print("Sorry there isn't any {} in the word.".format(letter))
                else:
                    print("Yay! {} is correct.".format(letter))
                    for i in range(len(the_word)):
                        if letter == the_word[i]:
                            clue[i] = letter
        else:
            print("Choose another")

        print(hanged(letters_wrong))
        print("".join(clue))
        print("")
        print("Guesses :", letters_tried)

        if letters_wrong == tries :
            print("Game Over!")
            print("The word was {}".format(the_word))
            computer_score += 1
            break
        if "".join(clue) == the_word:
            print("You Win!")
            print("The word was {}".format(the_word))
            player_score += 1
            break

    return play_again()


# Get guess from user
def guess_letter():
    print("")
    letter = input("Guess a letter : ")
    letter.strip()
    letter.lower()
    print("")
    return letter


# Start game again
def play_again():
    print("")
    answer = input("Would you like to play again? y/n: ")
    if answer in ("y", "Y", "Yes", "yes", "YES", "Of course!"):
        return answer
    else:
        print("Thank you for playing my game. See you next time!")


# Show the scores
def scores():
    print("")
    global player_score, computer_score
    print("HIGH SCORES")
    print("Player: ", player_score)
    print("Computer: ", computer_score)



# Start game
if __name__ == "__main__":
    start()
