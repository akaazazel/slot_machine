import random
import time


def main_game(bet_amount):
    # symbols = ["A", "B", "C", "D"]
    symbolValue = {"A": 2, "B": 3, "C": 5, "D": 10}

    reels = [
        ["A", "A", "A", "B", "B", "B", "C", "C", "D", "D"],
        ["A", "A", "A", "B", "B", "C", "C", "C", "D", "D"],
        ["A", "A", "A", "B", "B", "B", "C", "C", "D", "D"],
    ]

    for i in range(3):
        chosenReel = reels[i]
        chosenSymbol = random.choice(chosenReel)

        if i == 0:
            reel1 = chosenSymbol
        elif i == 1:
            reel2 = chosenSymbol
        elif i == 2:
            reel3 = chosenSymbol

        time.sleep(1)
        print(f":> {chosenSymbol}")

    matchValue = matchChecker(reel1, reel2, reel3, symbolValue, bet_amount)
    print(f":> Balance: ${balance}\n")


def matchChecker(reel1, reel2, reel3, symbolValue, bet_amount):
    global balance

    print("")
    time.sleep(0.5)

    if reel1 == reel2 == reel3:
        print(":> 3 Match!!!")

        multiplier = symbolValue.get(reel1)
        reward = bet_amount * multiplier
        balance += reward

        print(f":> You got ${reward} as reward!!!")

    elif reel1 == reel2 or reel2 == reel3 or reel3 == reel1:
        print(":> 2 Match!!!")
        balance += bet_amount
        print(":> You got your money back.")

    else:
        print(":> No Match:(")
        print(":> You lost your money!")


def main():
    global balance

    print("\n---SLOT MACHINE---")
    print("'q' - quit. 'bal' - balance")
    balance = input(":> Enter the amount to deposit: ").strip().lower()

    if balance == "q":
        return 0
    else:
        balance = int(balance)

    while True:
        bet_amount = (
            input(":> Enter the amount to bet on each reel. (min $10): ")
            .strip()
            .lower()
        )

        if bet_amount.isdigit() == True:
            bet_amount = int(bet_amount) * 3

        elif bet_amount == "q":
            return 0

        elif bet_amount == "bal":
            print(f":> Balance: ${balance}")
            continue

        if bet_amount > balance:
            print(f":> You don't have ${bet_amount} in your balance! Try again.")
        else:
            balance -= bet_amount
            print(f"You are betting ${bet_amount}\n")
            main_game(bet_amount)


balance = 0
main()
