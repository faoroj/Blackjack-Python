from art import logo
import sys
import random


def draw_card():
    return random.choice(cards)


def check_user_score(score):
    if score > 21:
        print(f"Your finl hand: {user_cards}, final score: {score}\nComputer's final hand {computer_cards}, "
              f"final score: {sum(computer_cards)} You went over")
        return True
    else:
        print(f"Your cards: {user_cards}, current score: {user_score}\nComputer's first card: {computer_cards[0]}")
        return False


def check_blackjack(user_total, computer_total):
    if user_total == 21:
        print(f"Your final hand: {user_cards}, final score: {user_total}\nComputer's final hand {computer_cards}, "
              f"final score: {sum(computer_cards)}\n Win, you have a blackjack")
        return True

    elif computer_total == 21:
        print(f"Your final hand: {user_cards}, final score: {user_total}\nComputer's final hand {computer_cards}, "
              f"final score: {sum(computer_cards)}\n Lose, computer has a blackjack")
        return True
    return False


def find_winner(user_final_score, computer_final_score):
    if user_final_score > computer_final_score:
        print(f"Your final hand: {user_cards}, final score: {user_final_score}\nComputer's final hand {computer_cards},"
              f"final score: {computer_final_score}\n You win")

    elif computer_final_score > 21:
        print(f"Your final hand: {user_cards}, final score: {user_final_score}\nComputer's final hand {computer_cards},"
              f"final score: {computer_final_score}\n You win, computer went over")
    elif user_final_score == computer_final_score:
        print(f"Your final hand: {user_cards}, final score: {user_final_score}\nComputer's final hand {computer_cards},"
              f"final score: {computer_final_score}\n It's a draw")
    else:
        print(f"Your final hand: {user_cards}, final score: {user_final_score}\nComputer's final hand {computer_cards},"
              f"final score: {computer_final_score}\n You Lose")


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
game = True

while game:
    user_cards = [draw_card() for _ in range(2)]
    computer_cards = [draw_card() for _ in range(2)]
    user_score = sum(user_cards)
    keep_playing = True

    play_game = input("Do you want to play a game of Blackjack? Type 'Y' or 'N': ").upper()
    if play_game == "N":
        sys.exit()

    print(logo)
    print(f"Your cards: {user_cards}, current score: {user_score}\nComputer's first card: {computer_cards[0]}")
    if check_blackjack(user_score, sum(computer_cards)):
        continue

    while keep_playing:
        keep_drawing = input("Type 'Y' to get another card, type 'N' to pass: ").upper()
        if keep_drawing == "Y":
            user_cards.append(draw_card())
            user_score = sum(user_cards)
            if check_user_score(user_score):
                game = False
                keep_playing = False

        else:
            break

    if user_score > 21:
        break

    computer_score = sum(computer_cards)
    while computer_score < 17:
        computer_cards.append(draw_card())
        computer_score = sum(computer_cards)

    find_winner(user_score, computer_score)
