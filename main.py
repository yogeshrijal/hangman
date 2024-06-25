
from hangman_word import word_list
from hangman_art import logo, stages
import random
chosen_word = random.choice(word_list)
display=[]
word_legnth=len(chosen_word)
lives=6
print(logo)
for _ in chosen_word:
    display+= ["_"]
print(display)


end=False
while end==False:
    guess = input("enter your guess  letter : ").lower()
    if guess in display:
        print(f" letter already guessed {guess}")
        continue
    for position in range(word_legnth):
         letter=chosen_word[position]
         if letter==guess:
          display[position]=letter
    if guess  not in chosen_word:
        print("incorrect guess")
        lives-= 1
        print(stages[lives])
        if lives==0 :
              end=True
              print("YOU LOST:)")
    print(display)
    if  "_" not in display:
        end =True
        print("YOU WON!!!!)")
    if (guess in display):
        print("correct guess, move on!")


