import random
words=["python","computer","programming","developer","algorithm"]
word=random.choice(words)
guessed_letters=[]
wrong_guesses=0
max_wrong_guesses=6
display=["_"]*len(word)
hangman_stages=[
"""  +---+
  |   |
      |
      |
      |
=======""",
"""  +---+
  |   |
  O   |
      |
      |
=======""",
"""  +---+
  |   |
  O   |
  |   |
      |
=======""",
"""  +---+
  |   |
  O   |
 /|   |
      |
=======""",
"""  +---+
  |   |
  O   |
 /|\\  |
      |
=======""",
"""  +---+
  |   |
  O   |
 /|\\  |
 /    |
=======""",
"""  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
======="""
]
print("="*42)
print("          HANGMAN GAME")
print("="*42)
print("Guess the hidden word one letter at a time!")
print("You have 6 incorrect guesses.")
print("="*42)
while wrong_guesses<max_wrong_guesses and "_" in display:
    print()
    print(hangman_stages[wrong_guesses])
    print()
    print("Word        :", " ".join(display))
    print("Wrong Guess :", wrong_guesses,"/ 6")
    if guessed_letters:
        print("Guessed     :", ", ".join(guessed_letters))
    print("-"*42)
    guess=input("Enter a letter: ").lower().strip()
    if len(guess)!=1 or not guess.isalpha():
        print("Please enter exactly one alphabet letter.")
        continue
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue
    guessed_letters.append(guess)
    if guess in word:
        print("Correct! The letter is in the word.")
        for i in range(len(word)):
            if word[i]==guess:
                display[i]=guess
    else:
        wrong_guesses+=1
        print("Wrong guess!")
if "_" not in display:
    print()
    print("="*42)
    print("       CONGRATULATIONS! YOU WON 🎉")
    print("="*42)
    print("The word was:",word)
    print("Wrong guesses:",wrong_guesses)
else:
    print()
    print(hangman_stages[wrong_guesses])
    print()
    print("="*42)
    print("             GAME OVER")
    print("="*42)
    print("The word was:",word)
    print("Better luck next time!")
print("="*42)
