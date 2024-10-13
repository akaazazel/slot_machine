import random
import time


class SlotMachine:
    def __init__(self, balance):
        self.balance = balance
        self.symbol_value = {"A": 2, "B": 3, "C": 5, "D": 10}
        self.reels = [
            ["A", "A", "A", "B", "B", "B", "C", "C", "D", "D"],
            ["A", "A", "A", "B", "B", "C", "C", "C", "D", "D"],
            ["A", "A", "A", "B", "B", "B", "C", "C", "D", "D"],
        ]

    def spin_the_reels(self, bet_amount):
        """
        Spins the reels and chooses a combination of 3
        """
        chosen_reel_list = ["_", "_", "_"]

        for i in range(3):
            chosen_reel = self.reels[i]
            chosen_symbol = random.choice(chosen_reel)
            chosen_reel_list[i] = chosen_symbol
            time.sleep(1)
            print(
                f"[{chosen_reel_list[0]}][{chosen_reel_list[1]}][{chosen_reel_list[2]}]"
            )

        print("")
        self.check_for_match(chosen_reel_list, bet_amount)
        print(f":> Balance: ${self.balance}\n")

    def check_for_match(self, reel_list, bet_amount):
        """
        Evaluates the chosen combo
        """
        if reel_list[0] == reel_list[1] == reel_list[2]:
            print(":> 3 Match!!!")
            reward = bet_amount * (self.symbol_value.get(reel_list[0]))
            self.balance += reward
            print(f":> You got ${reward} as reward!!!")

        elif (
            reel_list[0] == reel_list[1]
            or reel_list[1] == reel_list[2]
            or reel_list[2] == reel_list[0]
        ):
            print(":> 2 Match!!!")
            self.balance += bet_amount
            print(":> You got your money back.")

        else:
            print(":> No Match:(")
            print(":> You lost your money!")


def main():
    print("\n---SLOT MACHINE---")
    print("'q' - quit. 'bal' - balance")
    while True:
        balance = input("Enter the amount to deposit: ").strip().lower()

        if balance.isdigit():
            balance = int(balance)
            slot_machine = SlotMachine(balance)
            break
        elif balance == "q":
            print("Thanks for playing!")
            quit()
        else:
            print("Enter a valid input! Try again.")

    while True:
        bet_amount = (
            input(":> Enter the amount to bet on each reel. (min $10): ")
            .strip()
            .lower()
        )

        if bet_amount.isdigit():
            bet_amount = int(bet_amount) * 3
        elif bet_amount == "q":
            print("Thanks for playing!")
            quit()
        elif bet_amount == "bal":
            print(f":> Balance: ${balance}")
            continue
        else:
            print("Invalid input! Try again.")
            continue

        if bet_amount > balance:
            print(f":> You don't have ${bet_amount} in your balance! Try again.")
        else:
            slot_machine.balance -= bet_amount
            print(f"You are betting ${bet_amount}\n")
            slot_machine.spin_the_reels(bet_amount)


if __name__ == "__main__":
    main()
