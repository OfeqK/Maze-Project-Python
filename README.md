# Maze-Project-Python
This Python project uses the pygame library to generate a maze in real-time. It allows users to select a start and end point for the maze and then dynamically solves it in real-time.

**Prerequisites**:
Before you get started, make sure you have the following prerequisites:
Python (3.x recommended)
pygame library

**Installation**:
Clone or download this repository to your local machine.
Navigate to the project directory.
Install the required libraries from the requirements.txt file using pip:
pip install -r requirements.txt

**Usage**:
After installing the required libraries, you can run the project by executing the main Python script.
Follow the on-screen instructions to interact with the maze generation and solving process.

**Author**:
This project was created by Ofeq Koren from Israel.

**Maze Generation**:
The maze in this project is generated using an iterative implementation of the Backtracking (Depth-First Search) algorithm. Here's a brief overview of the maze generation process:
Choose the initial cell, mark it as visited, and push it to the stack.
While the stack is not empty:
  Pop a cell from the stack and make it the current cell.
  If the current cell has any neighbors that have not been visited:
    Push the current cell to the stack.
    Choose one of the unvisited neighbors.
    Remove the wall between the current cell and the chosen cell.
    Mark the chosen cell as visited and push it to the stack.

This process continues until all cells have been visited, resulting in the creation of a maze.

**License**:
This project is not currently licensed.
