# Function definitions

def calculate_circle_area(radius):
    area = 3.14*radius**2
    return area

def print_greeting():
    print("Welcome to the game.")

def announce_winner(player1_name, player1_score, player2_name, player2_score):
    if (player1_score > player2_score):
        player1W = player1_name, "has won the game."
        return player1W
    else:
        player2W = player2_name, "has won the game."
        return player2W

def calculate_simple_interest(principal, rate, time):
    interest = principal*rate*time/100
    return interest

import random
def roll__die():
    print(random.randint(1,6))

def convert_minutes(minutes):
    pass

# Main Code


# radius = int(input("Input a circle radius. "))
# total = calculate_circle_area (radius)
# print("Circle Area:", total)

# print_greeting()

# player1_name = input("Input player 1's name. ")
# player2_name = input("Input player 2's name. ")
# player1_score = int(input("Input player 1's score. "))
# player2_score = int(input("Input player 2's score. "))
# winner = announce_winner (player1_name, player1_score, player2_name, player2_score)
# print(winner)

# principal = int(input("Enter your principal interest money. "))
# rate = int(input("Enter your rate of interest percent as a number. "))
# time = int(input("Enter the number of years the money has been sitting. "))
# simple_interest = calculate_simple_interest(principal, rate, time)
# print("Simple Interest:", simple_interest)

