# Pong Game

## Full Description

The Pong Game project is a recreation of the classic arcade game, Pong, using Python's Turtle graphics module. The game is designed for two players, each controlling a paddle on opposite sides of the screen. The objective is to hit the ball past the opponent's paddle to score points, while preventing the ball from passing your own paddle. The game includes scoring, ball speed control, and realistic bouncing mechanics off the paddles and screen boundaries.

**Features:**
- **Two-Player Gameplay:** Players use the keyboard to control the paddles. Player 1 uses the "Up" and "Down" arrow keys, while Player 2 uses the "W" and "S" keys.
- **Ball Movement and Collision:** The ball moves continuously, bouncing off the top and bottom boundaries. It also bounces off the paddles when struck, changing direction.
- **Scoring System:** Points are awarded when the ball passes the opponent's paddle. The score is displayed on the screen.
- **Paddle and Ball Dynamics:** The ball's speed increases with each bounce, adding a level of difficulty as the game progresses.

**Note**: This project was inspired by Angela Yu's course on Udemy.

## Getting Started

### Prerequisites

- Python 3.x installed on your system.
- The Turtle graphics module (usually included with Python installations).

### How to Play

1. Clone or download the repository to your local machine.
2. Ensure you have the `paddle.py`, `score.py`, `ball.py`, and `boundary.py` modules in the same directory.
3. Run the script using Python:

   ```bash
   python pong_game.py
   ```

4. Control your paddle using the following keys:
   - Player 1: "W" to move up, "S" to move down.
   - Player 2: "Up" arrow to move up, "Down" arrow to move down.

5. The game will start automatically, with the ball moving towards one of the paddles. Hit the ball back and forth with your opponent, aiming to score by getting the ball past their paddle.

6. The game continues indefinitely, with the score displayed on the screen.

### Customization

You can customize the Pong Game by:
- **Adjusting Paddle and Ball Speeds:** Modify the speed of the paddles or the ball in their respective classes to change the difficulty level.
- **Changing the Screen Size:** Alter the screen dimensions by adjusting the `screen.setup(width=800,height=600)` parameters.
- **Adding Features:** Implement new features like power-ups, multiple balls, or AI-controlled paddles for single-player mode.
