from random_word import RandomWords
import re

print("Would you like to play hangman? (y/n)")
answer = input()
if "n" == answer:
    quit()

play = 'y'

while play == 'y':
    trys = 0
    word_display = []
    word = "a"
    make = "Please guess a letter"
    complete = False

    if not 4 < len(word) < 13:
        
        r = RandomWords()
        word = r.get_random_word()

    def display_setup():
        for x in range(0,len(word)):
            word_display.append("_")
        print(word_display)

    #print(str(word))

    print('Your word is ' + str(len(word)) + ' letters long')

    display_setup()

    print(make)

    #Mark this out later/ done
    #print(word)




    def attempt():
        global trys, complete
        guess = input()
        if guess == word:
            print(' YOU WON!')
            complete = True

        elif 0 < len(guess) < 2:
            if guess.isalpha() == False:
              print('Letters only please')
            elif guess in word:
                print('Nice! You got a letter right')
                replace = [m.start() for m in re.finditer(guess,word)]
                for i in replace:
                    word_display[i]=guess
                print(word_display)









            else:
                print('Sorry, thats not in this word')
                print('Only ' + str(5 - trys) + ' trys left')
                trys = trys + 1
    
        elif len(guess) > 1:
            print('Please only one letter at a time')



    while trys < 6 and complete == False:
        attempt()

    if complete == True:
        quit()

    if trys == 6:
    
        print('Oh no, you lose')
        print('The word was ' + word)
    
    print('Play again? (y/n)')
    play = input()