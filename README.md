# Battleship

## Overview
Battleship is a classic board game of strategy and luck, where two players engage in a duel to outmaneuver each other by sinking the opponent's fleet. This project is a Python-based implementation of the game, designed to be fully playable from the command line.

## Gameplay
The game consists of two 5x5 boards—one for the player and one for the machine. Each player positions their fleet of ships on their board, with each ship occupying at least one square. Players take turns announcing the coordinates of their attacks, aiming to hit the opponent's ships. The game continues until one player's fleet is entirely destroyed.

## Features
- **Board Setup:** Players manually position their ships, while the machine randomly places its fleet on a 5x5 grid.
- **Turn-Based Play:** Players input the coordinates of their attacks, and the game visually indicates whether the attack was a hit or a miss.
- **AI Opponent:** The machine randomly selects coordinates to attack on the player’s board after each turn.
- **Victory/Defeat Visuals:** The game provides visual feedback when all three ships of a player are destroyed, declaring a winner or loser.

## Objectives
1. **Board Construction:** Build a 5x5 grid for both the user and the machine. The user manually places their ships, while the machine’s ships are placed randomly.
2. **User Interface:** Display the player’s and machine’s boards, allowing the player to choose attack coordinates each turn. The game visually shows hits, misses, and attacked areas.
3. **AI Logic:** Implement a simple AI that randomly selects coordinates to attack on the player’s board after each player’s turn.
4. **Endgame Display:** Visually represent the victory or defeat when one player's fleet is entirely destroyed.

## Getting Started
To play the game, simply clone this repository and run the main Python script. Ensure you have Python 3.x installed on your machine.

`git clone https://github.com/yourusername/battleship.git`
`cd battleship`
`python3 battleship.py`


## Contributing
Feel free to fork this repository and submit pull requests with improvements, bug fixes, or new features. Contributions are welcome!

## License
This project is licensed under the MIT License - see the LICENSE file for details.
