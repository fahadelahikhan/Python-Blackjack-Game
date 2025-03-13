# Python Blackjack Game 🃏

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

A Python implementation of the classic card game Blackjack.

## 📜 About
This project implements the popular casino game Blackjack, where players compete against the dealer to get as close to 21 points as possible without going over. It's an excellent example of object-oriented programming principles and game logic implementation in Python.

## ✨ Features
- Classic Blackjack rules with easy-to-understand interface
- Automatic card dealing and scoring calculation
- Player choice to hit or stand
- Computer opponent with basic AI for dealer decisions
- Multiple game session support
- Clear win/lose/draw conditions

## 🚀 Quick Start

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/fahadelahikhan/Python-Blackjack-Game.git
   cd Python-Blackjack-Game
   ```

2. Run the game:
   ```bash
   python blackjack_game.py
   ```

### Basic Usage
```python
# Start a new game
from blackjack_game import start_game

# The game will automatically deal initial cards
# and display the current state

# Player's turn - choose to hit or stand
# Type 'y' to get another card, type 'n' to pass

# The computer (dealer) will automatically play its turn
# based on predefined logic

# Final results will be displayed with scores
```

### Example Game Session
```python
# Initial deal
print(f"Your cards: [Ace, King]")
print(f"Computer's first card: Queen")

# Player chooses to hit
choice = 'y'
new_card = ran_card()  # Suppose it's a 5
print(f"Your final hand: [Ace, King, 5]")

# Computer's turn
computer_choice = random.randint(0, 1)  # Suppose it chooses to hit
new_computer_card = ran_card()  # Suppose it's a 10
print(f"Computer's final hand: [Queen, 10]")

# Determine winner
if sum(player_cards_value) > sum(computer_cards_value):
    print("You win!")
else:
    print("Computer wins!")
```

## 📖 How It Works
The game follows standard Blackjack rules:
- Cards have values: numbered cards = face value, face cards = 10, Ace = 11 (or 1 if it would cause bust)
- Players and dealer receive two cards each
- Players can choose to hit (receive another card) or stand (end their turn)
- Dealer must hit until their total is at least 17
- The winner is the one closest to 21 without exceeding it

## ⚖️ License
Distributed under the MIT License. See [LICENSE](LICENSE) for details.

---

> **Note**: This implementation is for educational and entertainment purposes. Always remember that gambling should be done responsibly and within legal boundaries.
