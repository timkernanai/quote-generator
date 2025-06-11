import random
#Test SSH push
quotes = [
    "Believe you can and you're halfway there.",
    "The only way to do great work is to love what you do.",
    "You are stronger than you think.",
    "Keep going; everything you need will come to you at the perfect time.",
    "Small steps every day lead to big results."
    "You've got this; keep pushing forward!"
]

def get_random_quote():
    return random.choice(quotes)

def main():
    while True:
        print("Your motivational quote of the day:")
        print(get_random_quote())
        again = input("Want another quote? (yes/no): ").lower()
        if again != "yes":
            break

if __name__ == "__main__":
    main()