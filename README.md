AI Pathfinder: Uninformed Search Visualization
📌 Project Overview
AI Pathfinder is a Python-based graphical application that visualizes Uninformed Search Algorithms in a grid-based environment. The agent navigates from a Start Point (S) to a Target Point (T) while avoiding obstacles (walls).

The application provides real-time animation and clearly distinguishes between Frontier Nodes (currently in the queue/stack) and Explored Nodes (visited nodes), offering a strong educational demonstration of algorithm behavior and efficiency.

🚀 Features

Interactive GUI: Draw walls, place Start/Target nodes, and reset the grid.

6 Search Algorithms Implemented:

Breadth-First Search (BFS)

Depth-First Search (DFS)

Uniform-Cost Search (UCS)

Depth-Limited Search (DLS)

Iterative Deepening DFS (IDDFS)

Bidirectional Search

Real-Time Visualization: Observe how each algorithm explores the grid step-by-step.

Strict Movement Constraint: Clockwise order
Up → Right → Bottom → Bottom-Right → Left → Top-Left

🛠️ Installation & Setup
Prerequisites

Python 3.x

Pygame library

1️⃣ Clone the Repository
git clone https://github.com/YourUsername/AI_A1_22F_XXXX.git
cd AI_A1_22F_XXXX

2️⃣ Install Dependencies
pip install pygame

3️⃣ Run the Application
python main.py

🎮 Controls & Usage
Input	Action
Left Click	Place Start (Orange), Target (Turquoise), or Walls (Black)
Right Click	Erase (Reset cell to White)
Key 1	Run BFS
Key 2	Run DFS
Key 3	Run UCS
Key 4	Run DLS (Limit = 10)
Key 5	Run IDDFS
Key 6	Run Bidirectional Search
Key C	Clear Grid
🎨 Color Legend

Orange: Start Node

Turquoise: Target Node

Black: Wall / Obstacle

Green: Frontier Nodes

Red: Explored Nodes

Purple: Final Path

📂 Project Structure

main.py – GUI loop and user interaction

grid.py – Node class and grid handling

algorithms.py – All six search algorithms

settings.py – Colors, screen size, movement constraints

⚠️ Assignment Constraints

Strict clockwise movement order starting from Up

Only two diagonals allowed: Bottom-Right and Top-Left

Visualization must differentiate Frontier and Explored nodes

👨‍💻 Author Information

Author: Abdullah Farooq & Zainab Iftikhar
Student ID: 23F-0503 & 23F-0762
Course: Artificial Intelligence
