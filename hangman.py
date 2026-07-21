import random

# List of predefined words
words = ["python", "football", "dream", "engineer", "apple"]

# Select a random word
word = random.choice(words)

# Create blank spaces
display = ["_"] * len(word)

# Variables
guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

# Welcome Message
print("=" * 45)
print("🎮 HANGMAN GAME 🎮")
print("=" * 45)
print("Think. Guess. Win.")
print("A secret word is waiting for you.")
print("Enter one letter at a time.")
print("Can you solve it before using all 6 chances?")
print("=" * 45)

# Game Loop
while wrong_guesses < max_wrong_guesses and "_" in display:

    print("\nWord:", " ".join(display))
    print("Guessed Letters:", " ".join(guessed_letters))
    print(f"Remaining Chances: {max_wrong_guesses - wrong_guesses}")

    guess = input("Enter a letter: ").lower()

    # Check valid input
    if len(guess) != 1 or not guess.isalpha():
        print("⚠ Please enter only one alphabet letter.")
        continue

    # Check repeated letter
    if guess in guessed_letters:
        print("⚠ You already guessed this letter.")
        continue

    guessed_letters.append(guess)

    # Correct Guess
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
        print("✅ Correct Guess!")

    # Wrong Guess
    else:
        wrong_guesses += 1
        print("❌ Wrong Guess!")

# Result
print("\n" + "=" * 40)

if "_" not in display:
    print("🎉 Congratulations!")
    print("You guessed the word:", word)
    print("🏆 You Win!")
else:
    print("💀 Game Over!")
    print("The correct word was:", word)

print("=" * 40)
print("Thank you for playing Hangman!")