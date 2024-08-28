import random
import time

def choice():
    while True:
        choice = input("\nDo you want to play a new round? (Yes or No): ").lower()
        if choice == "yes":
            return True
        elif choice == "no":
            print("\tExiting the program...")
            time.sleep(2)
            print("\t Exit.")
            return False
        else:
            print("Invalid input. Please enter 'Yes' or 'No'.")

def main():
    file_path = "result.txt"
    with open(file_path, 'w') as file:
        print("You are in the Kingdom of Dragons. In front of you, you see five caves. In one \n"
              "cave, the dragon is friendly and will share his treasure with you. The other \n"
              "dragons is hungry and will eat you on sight!")
        file.write("You are in the Kingdom of Dragons. In front of you, you see five caves. In one \n"
              "cave, the dragon is friendly and will share his treasure with you. The other \n"
              "dragons is hungry and will eat you on sight!")
        while True:
            friendly_dragon = random.randint(1, 5)
            try:
                cave = int(input("\nCave 1,2,3,4 or 5 : "))
                if 1 <= cave <= 5:
                    print("\n\tYou approach the cave...")
                    file.write("\n")
                    file.write(f"\n You approach the cave...{cave}")
                    time.sleep(2)
                    print("\tIt is dark and spooky...")
                    file.write("\n It is dark and spooky...")
                    time.sleep(2)
                    print("\tA large dragon jumps out in front of you! He opens his jaws and...")
                    time.sleep(2)
                    if cave == friendly_dragon:
                        print("\tGives you his treasure!")
                        file.write("\n Gives you his treasure!")
                    else:
                        print("\tGobbles you down in one bite!")
                        file.write("\n Gobbles you down in one bite!")
                    if not choice():
                        break
                else:
                    print("Invalid input. Please choose cave 1 or 2.")
            except ValueError:
                print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
