# 2048 Game (Python + Pygame)

A Python implementation of the classic 2048 game, featuring clean object-oriented logic and a Pygame-powered user interface. This version includes simple but complete game mechanics such as tile merging, movement, score tracking, and game-over detection.

---

## 🚀 How to Run

1. Install `pygame` if you haven’t already:

   ```bash
   pip3 install pygame
   python3 runner.py


---

## 🔥 Project Motivation
Improve my python skills and escape tutorial hell. More specifically, be comfortable in using classes and object-oriented programming and directly applying problem solving skills to my projects. 

I was also bored af. 

## 🛠️ Technologies Used

Python (Standard Library) -- Implementing core game logic

Pygame -- For building the UI and handling keyboard input
-- Note: the UI portion was vibe-coded using AI tools such as ChatGPT. The 2048 game logic itself was written from scratch as a learning exercise, with minimal AI/code generation help.

## 🧠 What I learned
This was my first fully self-directed Python project, and it taught me a lot:

	•	Object-Oriented Programming: Structuring the game’s logic into classes was key to keeping the code modular and clean.
	•	Debugging Strategies: Using a separate file (tester.py) to isolate and test individual functions helped break down bugs more effectively.
	•	Algorithmic Thinking: I used ideas from CS50AI — like deep copying and state simulation — to implement smart game-over logic inspired by minimax search.
	•	Problem Decomposition: Translating game mechanics into pseudocode before writing actual code was a major productivity boost.


## Screenshot 
<img width="787" height="1049" alt="Screenshot 2025-07-14 at 6 33 00 PM" src="https://github.com/user-attachments/assets/39a40ec9-ccf0-42c7-bf18-58bc98580423" />


## Credit
Created by Darren Kim
Inspired by CS50AI and the original 2048 classical game

## 📁 Project Structure

```
2048/
├── logic.py         # Game logic (board state, movement, merging)
├── runner.py        # Pygame interface for playing the game
├── tester.py        # Debugging + function testing
├── screenshot.png   # UI screenshot (for README)
└── README.md        # Project documentation
