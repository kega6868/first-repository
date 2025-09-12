from random import choice as ch

def possibility(user, pnj):
    if user == pnj:
        return "It's a draw!"
    elif (user == "✊" and pnj == "✌️") or (user == "✋" and pnj == "✊") or (user == "✌️" and pnj == "✋"):
        return "You win!"
    else:
        return "You lose!"

programme = True
possible_choices = ["✊", "✋", "✌️"]

while programme == True:
    print("=============================")
    print("Rock Paper Scissors ")
    print("=============================")
    print("")
    print("1) ✊")
    print("2) ✋")
    print("3) ✌️")
    pnj_choice = ch(possible_choices)
    user_choice = int(input("Pick a number: "))
    if user_choice == 1:
        user_choice = "✊"
    elif user_choice == 2:
        user_choice = "✋"
    elif user_choice == 3:
        user_choice = "✌️"
    else:
        print("Invalid choice!")
    possibility_result = possibility(user_choice, pnj_choice)
    print('You chose: ' + user_choice)
    print('The computer chose: ' + pnj_choice)
    print(possibility_result)
    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() != 'y':
        programme = False
        print("Thanks for playing!")
    

        







