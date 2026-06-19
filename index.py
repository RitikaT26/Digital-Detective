```python
def main():
    print("=" * 50)
    print("DIGITAL DETECTIVE")
    print("The Missing Laptop Mystery")
    print("=" * 50)

    clues = []
    score = 0

    while True:
        print("\nWhat would you like to do?")
        print("1. Inspect the office")
        print("2. Interview Alice")
        print("3. Interview Bob")
        print("4. Check security logs")
        print("5. View collected clues")
        print("6. Make accusation")
        print("7. Quit")

        choice = input("Enter choice: ")

        if choice == "1":
            if "USB Drive" not in clues:
                print("\nYou find a USB drive under a desk.")
                clues.append("USB Drive")
                score += 10
            else:
                print("\nYou already inspected the office.")

        elif choice == "2":
            if "Alice Alibi" not in clues:
                print("\nAlice says she was in a meeting from 2 PM to 3 PM.")
                clues.append("Alice Alibi")
                score += 10
            else:
                print("\nYou already interviewed Alice.")

        elif choice == "3":
            if "Bob Nervous" not in clues:
                print("\nBob seems nervous and avoids eye contact.")
                clues.append("Bob Nervous")
                score += 10
            else:
                print("\nYou already interviewed Bob.")

        elif choice == "4":
            if "Security Log" not in clues:
                print("\nSecurity footage shows Bob entering the office at 2:15 PM.")
                clues.append("Security Log")
                score += 20
            else:
                print("\nYou already checked the logs.")

        elif choice == "5":
            show_clues(clues)

        elif choice == "6":
            solve_case(clues, score)
            break

        elif choice == "7":
            print("\nCase closed. Goodbye!")
            break

        else:
            print("\nInvalid choice.")


def show_clues(clues):
    print("\nCollected Clues:")

    if len(clues) == 0:
        print("No clues collected yet.")
        return

    for clue in clues:
        print("-", clue)


def solve_case(clues, score):
    print("\nWho stole the laptop?")
    print("1. Alice")
    print("2. Bob")

    suspect = input("Enter your accusation: ")

    if suspect == "2":
        print("\nCASE SOLVED!")
        print("Bob stole the laptop.")
        print("Your detective score:", score + 50)

    else:
        print("\nWrong accusation!")
        print("The real thief was Bob.")
        print("Your detective score:", score)


if __name__ == "__main__":
    main()
```
