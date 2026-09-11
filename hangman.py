import random
words=["python","computer","programming","developer","algorithm"]
word=random.choice(words)
guessed_letters=[]
wrong_guesses=0
max_wrong_guesses=6
display=["_"]*len(word)
print("================================")
print("       HANGMAN GAME")
print("================================")
print("Guess the word one letter at a time!")
print("You have 6 incorrect guesses.")
print()
while wrong_guesses<max_wrong_guesses and "_" in display:
    print("Word:"," ".join(display))
    print("Wrong guesses:",wrong_guesses,"/ 6")
    if guessed_letters:
        print("Guessed letters:",", ".join(guessed_letters))
    guess=input("Enter a letter: ").lower().strip()
    if len(guess)!=1 or not guess.isalpha():
        print("Please enter a single letter.")
        print()
        continue
    if guess in guessed_letters:
        print("You already guessed that letter.")
        print()
        continue
    guessed_letters.append(guess)
    if guess in word:
        print("Correct guess!")
        for i in range(len(word)):
            if word[i]==guess:
                display[i]=guess
    else:
        wrong_guesses+=1
        print("Wrong guess!")
    print()
if "_" not in display:
    print("================================")
    print("🎉 Congratulations! You won!")
    print("The word was:",word)
    print("================================")
else:
    print("================================")
    print("💀 Game Over!")
    print("The word was:",word)
    print("================================")
