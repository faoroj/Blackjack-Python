from art import logo
import random


def start_game():
    global cards
    for num in range(0, 2):
        random_card = random.randint(0, len(cards))
        user_cards.append(cards[random_card])

    for num in range(0, 2):
        random_card = random.randint(0, len(cards))
        computer_cards.append(cards[random_card])


def check_user_score(score):
    global game
    global user_cards
    global computer_cards
    if score > 21:
        print(f"Your final hand: {user_cards}, final score: {score}\nComputer's final hand {computer_cards}, "
              f"final score: {sum(computer_cards)} You went over")
        game = False
    else:
        print(f"Your cards: {user_cards}, current score: {user_score}\nComputer's first card: {computer_cards[0]}")


def check_blackjack(user_total, computer_total):
    global game
    if user_total == 21:
        print(f"Your final hand: {user_cards}, final score: {user_total}\nComputer's final hand {computer_cards}, "
              f"final score: {sum(computer_cards)}\n Win, you have a blackjack")
        game = False

    elif computer_total == 21:
        print(f"Your final hand: {user_cards}, final score: {user_total}\nComputer's final hand {computer_cards}, "
              f"final score: {sum(computer_cards)}\n Lose, computer has a blackjack")
        game = False


def draw_card():
    random_card = random.randint(0, len(cards))
    return random_card


def find_winner(user_final_score, computer_final_score):
    if user_final_score > computer_final_score:
        print(f"Your final hand: {user_cards}, final score: {user_final_score}\nComputer's final hand {computer_cards},"
              f"final score: {computer_final_score}\n You win")
    else:
        print(f"Your final hand: {user_cards}, final score: {user_final_score}\nComputer's final hand {computer_cards},"
              f"final score: {computer_final_score}\n You Lose")


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

game = True

while game:
    user_cards = []
    computer_cards = []
    play_game = input("Do you want to play a game of Blackjack? Type 'Y' or 'N': ").upper()
    if play_game == "N":
        exit()

    print(logo)
    start_game()
    user_score = sum(user_cards)
    print(f"Your cards: {user_cards}, current score: {sum(user_cards)}\nComputer's first card: {computer_cards[0]}")
    check_blackjack(user_score, sum(computer_cards))

    while True:
        keep_drawing = input("Type 'Y' to get another card, type 'N' to pass: ").upper()
        if keep_drawing == "Y":
            user_cards.append(cards[draw_card()])
            user_score = sum(user_cards)
            check_user_score(user_score)

        else:
            break

    computer_score = sum(computer_cards)
    while computer_score < 17:
        computer_cards.append(cards[draw_card()])
        computer_score = sum(computer_cards)

    find_winner(user_score, computer_score)