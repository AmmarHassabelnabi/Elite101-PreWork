import os
import sys
import time

import readchar
from readchar import key, readkey


def type(ai_text, speed=0.03):
  for character in ai_text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(speed)
  print("")
#typing effect inspired by https://stackoverflow.com/questions/20302331/typing-effect-in-python

def welcome():
  type("Hello! I am DineBot! Your versatile AI assistant for Dining Delight.")
  time.sleep(0.5)
  type("I am here to help create dining reservations, as well as answer any questions you may have about our menu, prices, store hours, specials/deals, or location.")
  time.sleep(0.5)
  type("To begin, I need to learn more about you to optimize your experience.")
  time.sleep(0.5)
  name = input("""\nWhat is your name?
You: """)
  type(f"\nNice to meet you {name}!\n")
  time.sleep(0.5)
  age = int(input("""What is your age?
You: """))
  type('\nThank you! How can I assist you today?')

def user_options():
  type("""
1. I would like to make a reservation.
2. I would like to know more about your menu and prices.
3. I would like to know the hours of operation.
4. I would like to know about your specials/deals.
5. I would like to know the location of Dining Delight.
6. I would like to leave a review.
7. Exit application.

""")
  user_choice = input("You: ")  

  if user_choice == '1':
    book_table()
  if user_choice == '2':
    main_menu()



def main_menu():
  menu = print("""
  Dining Delight Menu
-----------------------  
|     Appetizers      |
|                     |
|      Entrees        |
|                     |
|      Drinks         |
|                     |
|      Deserts        |
-----------------------

""")
  menuSelection = input('You: ')
  
  if menuSelection == '1':
    os.system('clear')
    type("Appetizers")
    main_menu()
  elif menuSelection == '2':
    os.system('clear')
    type("Entrees.")
    main_menu()
  elif menuSelection == '3':
    os.system('clear')
    type("Drinks")
    main_menu()
  elif menuSelection == '4':
    os.system('clear')
    type("Deserts")
    main_menu()
  elif menuSelection == '5':
    type("Goodbye!")
    exit()
  else:
    print("Invalid response. Please try again.")
    main_menu()

def book_table():
  hi = 0




welcome()
user_options()
main_menu()




