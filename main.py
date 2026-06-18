import random

class RockPaperScissors:

    def play_game(self):

        choices = ["rock", "paper", "scissors"]

        while True:
            try:
                user = input("\nEnter Rock, Paper or Scissors: ").lower()

                if user not in choices:
                    raise ValueError("Invalid Choice!")

                computer = random.choice(choices)

                print("Computer Choice:", computer)

                if user == computer:
                    print("Result: TIE")

                elif (user == "rock" and computer == "scissors") or \
                     (user == "paper" and computer == "rock") or \
                     (user == "scissors" and computer == "paper"):
                    print("Result: YOU WIN!")

                else:
                    print("Result: COMPUTER WINS!")

                again = input("\nDo you want to play again? (yes/no): ").lower()

                if again != "yes":
                    print("Thanks for Playing!")
                    break

            except ValueError as e:
                print(e)
                print("Please enter only Rock, Paper or Scissors.")

# Main Program
game = RockPaperScissors()
game.play_game()