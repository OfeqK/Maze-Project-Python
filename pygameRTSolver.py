from cell import Cell
import pygame

pygame.init()

"""
Iterative Implementation of Backtracking (DFS) To Generate The Maze
  1. Choose the initial cell, mark it as visited and push it to the stack
  2. While the stack is not empty
  1. Pop a cell from the stack and make it a current cell
  2. If the current cell has any neighbours which have not been visited:
      1. Push the current cell to the stack
      2. Choose one of the unvisited neighbours
      3. Remove the wall between the current cell and the chosen cell
      4. Mark the chosen cell as visited and push it to the stack
"""


def remove_walls(current, next_c):
    dx = current.x - next_c.x
    if dx == 1:  # the current cell is to the right of the next cell
        current.walls["left"] = False
        next_c.walls["right"] = False
    if dx == -1:  # the current cell is to the left of the next cell
        current.walls["right"] = False
        next_c.walls["left"] = False

    dy = current.y - next_c.y
    if dy == 1:  # the current cell is below the next cell
        current.walls["top"] = False
        next_c.walls["bottom"] = False
    if dy == -1:  # the current cell is above the next cell
        current.walls["bottom"] = False
        next_c.walls["top"] = False


white = pygame.Color(255, 255, 255)
black = pygame.Color(0, 0, 0)
light_blue = pygame.Color(0, 255, 255)
turquoise = pygame.Color(0, 82, 84)
red = pygame.Color(255, 0, 0)

TILE = 40  # each pixel will be 100px so that it is easier to see
cols, rows = 20, 20  # we have a 20x20 maze
W_WIDTH, W_HEIGHT = cols * TILE, rows * TILE

wn = pygame.display.set_mode((W_WIDTH, W_HEIGHT))
pygame.display.set_caption("Maze Solver!")
clock = pygame.time.Clock()

# the maze setup
grid_cells = [Cell(col, row, TILE, (cols, rows)) for row in range(rows) for col in range(cols)]
current_cell = grid_cells[0]  # top left
stack = []
generating_maze = True

while generating_maze:
    wn.fill(light_blue)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    # draw all cells to the screen
    for cell in grid_cells:
        cell.draw(wn)
    current_cell.visited = True
    current_cell.draw_current_cell(wn)

    next_cell = current_cell.check_neighbors(grid_cells)  # choosing a random neighbor from the list of neighbors
    if next_cell:  # a random neighbor was chosen
        next_cell.visited = True
        stack.append(current_cell)  # if we get to a dead end we can pop back to the previous current cell
        remove_walls(current_cell, next_cell)
        current_cell = next_cell
    elif stack:  # dead end reached and there is a cell to pop back to
        current_cell = stack.pop()
    else:
        generating_maze = False

    pygame.display.flip()  # updating the screen
    clock.tick(120)  # 30 fps

# finding starting and ending cell for the solver
print("Finished generating the maze!")
solving_maze = True
start_chosen, end_chosen = False, False
start_printed, end_printed = False, False
start_cell, end_cell = (0, 0), (cols - 1, rows - 1)  # default start and end cell

# setting up the maze solver
stack = []  # cell, path
visited_cells = []
found_end = False
final_path = []

while solving_maze:
    wn.fill(light_blue)

    if not start_printed:
        print("Choose a starting cell!")
        start_printed = True
    elif not end_printed and start_chosen:
        print("Choose an ending cell!")
        end_printed = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if not start_chosen:
                start_cell = list(pos)
                start_cell[0], start_cell[1] = start_cell[0] // TILE, start_cell[
                    1] // TILE  # making sure we are at the correct cell
                print(f"Start: {start_cell}")
                start_chosen = True
                start_index = start_cell[0] + start_cell[1] * rows
                current_cell = grid_cells[start_index]
                stack.append((current_cell, [current_cell]))  # cell, path
            elif not end_chosen:
                end_cell = list(pos)
                end_cell[0], end_cell[1] = end_cell[0] // TILE, end_cell[
                    1] // TILE  # making sure we are at the correct cell
                print(f"End: {end_cell}")
                end_chosen = True

    # TODO: finish clearing the maze of other paths that are irrelevant to the final path
    for cell in grid_cells:
        cell.draw(wn)
        # check if the cell is in the final path
        if cell in final_path:
            cell.visited = False
        else:
            cell.visited = True

    # start and end were chosen so we can start solving the maze:
    if end_chosen and not found_end and stack:
        current_cell, path = stack.pop()
        final_path = path
        current_cell.visited = False  # reversing it back to the light blue color
        x, y = current_cell.draw_current_cell(wn)
        if x // TILE == end_cell[0] and y // TILE == end_cell[1]:
            print("Finished solving the maze!")
            found_end = True

        visited_cells.append(current_cell)
        valid_neighbors = current_cell.choose_neighbor(grid_cells, visited_cells)
        if not valid_neighbors:  # dead end
            continue

        for neigh in valid_neighbors:
            stack.append((neigh, path + [neigh]))

    pygame.display.flip()  # updating the screen
    clock.tick(30)  # 30 fps
