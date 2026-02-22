# Cat Adventure 🐱

A 2D top-down obstacle course game built with Pygame where a cat must navigate obstacles, collect items, and reach its home before time runs out!

## Features

*   **Cat Character:** Controllable via Arrow Keys or WASD.
*   **Enemies (Dogs):** Move around the screen and bounce off the edges. Touching them results in a "Game Over".
*   **Hazards (Puddles):** Static obstacles on the screen. Touching them results in a "Game Over".
*   **Collectibles (Treats):** Can be picked up to increase your score by 100 points each.
*   **Goal (Cat Tree):** Reaching the cat tree triggers the "Level Complete" screen.
*   **Timer System:** You have 30 seconds to reach the cat tree before time runs out!

## Requirements

*   Python 3.x
*   Pygame (>= 2.6.0)

## Installation

1.  Make sure you have Python installed.
2.  Install the required dependencies using pip:
    ```bash
    pip install -r requirements.txt
    ```

## How to Play

Run the game from your terminal:

```bash
python main.py
```

*   Press **SPACE** on the "Start" screen to begin playing.
*   Use the **Arrow Keys** or **WASD** to move the cat.
*   Collect the little fish-shaped treats for points.
*   Avoid the dogs and the blue puddles!
*   Get to the big cat tree on the right side of the screen before the timer runs out. 
*   When the game ends (either by winning or losing), you can press **SPACE** to restart a new randomized level.
