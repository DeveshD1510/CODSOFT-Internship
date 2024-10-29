import tkinter as tk
import random

# Initialize scores
user_score = 0
computer_score = 0

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    global user_score, computer_score
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        user_score += 1
        return "You win!"
    else:
        computer_score += 1
        return "Computer wins!"

# Function to play the game
def play_game(user_choice):
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    result = determine_winner(user_choice, computer_choice)

    result_label.config(text=f"You chose: {user_choice}\nComputer chose: {computer_choice}\n{result}")
    update_scores()

# Function to reset the game
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    result_label.config(text="Choose rock, paper, or scissors!")
    update_scores()

# Function to update the score display
def update_scores():
    score_label.config(text=f"Your Score: {user_score} | Computer Score: {computer_score}")

# Setting up the main window
root = tk.Tk()
root.title("Rock, Paper, Scissors")
root.configure(bg="lightblue")
root.geometry("700x500")  # Set the window size

# Instructions
instructions_label = tk.Label(root, text="Choose your move!", font=("Bookman Old Style", 18), bg="lightblue")
instructions_label.pack(pady=10)

# Rules of the game
rules_text = (
    "Rules:\n"
    "1. Rock beats Scissors.\n"
    "2. Scissors beats Paper.\n"
    "3. Paper beats Rock.\n"
    "4. Choose Rock, Paper, or Scissors to play.\n"
)
rules_label = tk.Label(root, text=rules_text, font=("Bookman Old Style", 16), bg="orange", justify=tk.LEFT)
rules_label.pack(pady=10)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 14), bg="lightblue")
result_label.pack(pady=10)

# Score label
score_label = tk.Label(root, text="Your Score: 0 | Computer Score: 0", font=("Arial", 16), bg="lightblue")
score_label.pack(pady=10)

# Buttons for user choices
button_frame = tk.Frame(root, bg="lightblue")
button_frame.pack(pady=20)

rock_button = tk.Button(button_frame, text="Rock", command=lambda: play_game('rock'), font=("Arial", 14), bg="salmon")
paper_button = tk.Button(button_frame, text="Paper", command=lambda: play_game('paper'), font=("Arial", 14), bg="lightyellow")
scissors_button = tk.Button(button_frame, text="Scissors", command=lambda: play_game('scissors'), font=("Arial", 14), bg="lime")

rock_button.pack(side=tk.LEFT, padx=10)
paper_button.pack(side=tk.LEFT, padx=10)
scissors_button.pack(side=tk.LEFT, padx=10)

# Reset button
reset_button = tk.Button(root, text="Reset", command=reset_game, font=("Arial", 14), bg="lightgray")
reset_button.pack(pady=20)

# Run the application
root.mainloop()
