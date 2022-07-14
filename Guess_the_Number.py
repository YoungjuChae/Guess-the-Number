# Author: Youngju Chae
# Guess The Number Game

# Importing necessary modules
import random
from art import logo_guess_the_number
from replit import clear

# Run the game
def guessNumber():
  clear()
  print(logo_guess_the_number)
  
  # Create necessary variables
  guesses = 0
  game_over = False
  
  # Introduce the game
  print('\tWelcome to the Number Guessing Game!')
  print("\tI'm thinking of a number between 1 and 100.")
  number = random.randint(1, 100)
  
  # Determine difficulty
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if difficulty == 'easy':
    guesses = 10
    print('\tYou have 10 attempts to guess the number.')
  elif difficulty == 'hard':
    guesses = 5
    print('\tYou have 5 attempts to guess the number.')
    
  # Determine the result
  while not game_over:
    choice = int(input('Make a guess: '))
    if choice == number:
      print(f'You got it! The answer was {number}')
      game_over = True
    elif choice > number:
      guesses -= 1
      print('\tToo high.')
      print(f'\tYou have {guesses} attempts remainging.')
    else:
      guesses -= 1
      print('\tToo low.')
      print(f'\tYou have {guesses} attempts remainging.')
    if guesses == 0:
      print(f'You have ran out of attempts. The actual number was {number}.')
      game_over = True
 
# Determine if player wants to play again
while(input("Do you want to play the Guess a Number game? y or n: ") == "y"):
  guessNumber() 
