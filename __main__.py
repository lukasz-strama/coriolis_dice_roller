from dice_logic import roll_dice, count_successes, calculate_probability
from image_generator import create_dice_image

def update_file_timestamp():
    """Touch the main file to update the file system timestamp (e.g., for reload triggers)."""
    try:
        with open('__main__.py', 'r'):
            pass
    except FileNotFoundError:
        pass

def main():
    print("=== Coriolis Dice Roller ===")
    print("Enter number of dice to roll (or 'quit' to exit)")

    while True:
        try:
            user_input = input("\nNumber of dice: ").strip().lower()

            if user_input == 'quit':
                print("Thanks for playing!")
                break

            num_dice = int(user_input)
            if num_dice < 1:
                print("Please enter a positive number of dice.")
                continue

            results = roll_dice(num_dice)
            successes = count_successes(results)
            dice_display = " ".join(f"[{die}]" for die in results)

            print(f"\n{dice_display}")
            print(f"{successes} success{'es' if successes != 1 else ''}!" if successes else "Failure!")

            probability = calculate_probability(num_dice, successes)
            print(f"{probability:.1f}% chance for this outcome")

            create_dice_image(results, successes, probability)
            update_file_timestamp()

        except ValueError:
            print("Please enter a valid number or 'quit' to exit.")
        except KeyboardInterrupt:
            print("\nThanks for playing!")
            break

if __name__ == "__main__":
    main()
