import os
import sys
import time


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
  print("""
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
    os.system('clear')
    type("\nPlaceholder 1")
    user_options()
  if user_choice == '2':
    os.system('clear')
    type("\nPlaceholder 2")
    user_options()
  if user_choice == '3':
    os.system('clear')
    type("\nPlaceholder 3")
    user_options()
  if user_choice == '4':
    os.system('clear')
    type("\nPlaceholder 4")
    user_options()
  if user_choice == '5':
    os.system('clear')
    type("\nPlaceholder 5")
    user_options()
  if user_choice == '6':
    os.system('clear')
    type("\nPlaceholder 6")
    user_options()
  if user_choice == '7':
    os.system('clear')
    type("Thank you for using DineBot! Have a great day!")


def chatbot():
  welcome()
  user_options()

chatbot()