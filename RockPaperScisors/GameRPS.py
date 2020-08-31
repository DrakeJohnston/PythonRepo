import random

still_playing = True
ai_score = 0
player_score = 0

while still_playing:
    rock = 0
    paper = 1
    scissors = 2
    errored = 10

    player_choice = input("Type Rock, Paper or Scissors. Case Sensitive!: ")

    if player_choice == "Rock":
        player_numb = rock
    elif player_choice == "Paper":
        player_numb = paper
    elif player_choice == "Scissors":
        player_numb = scissors
    else:
        player_numb = errored

    ai_choice = random.randint(rock, scissors)

    if player_numb == 0 & ai_choice == 2:  # player win conditions
        player_score += 1
        print('Player Wins!')
    elif player_numb == 2 & ai_choice == 1:
        player_score += 1
        print('Player Wins!')
    elif player_numb == 1 & ai_choice == 0:
        player_score += 1
        print('Player Wins!')

    elif player_numb == 2 & ai_choice == 0:  # ai win conditions
        ai_score += 1
        print('Ai Wins!')
    elif player_numb == 1 & ai_choice == 2:
        ai_score += 1
        print('Ai Wins!')
    elif player_numb == 0 & ai_choice == 1:
        ai_score += 1
        print('Ai Wins!')

    else:
        print('Its a tie!')

    # print(ai_choice)
    # print(player_numb)

    j = input('Play Again? Yes or No ')
    if j == "Yes":
        still_playing = True
    elif j == "yes":
        still_playing = True
    elif j == "No":
        still_playing = False
    elif j == "no":
        still_playing = False
    else:
        print("Unknown input created ending")
        still_playing = False

print("Player Final Score: " + str(player_score))
print("Ai Final Score: " + str(ai_score))
