import pygame
import random

white = pygame.Color(255, 255, 255)
black = pygame.Color(0, 0, 0)
light_blue = pygame.Color(0, 255, 255)
turquoise = pygame.Color(0, 82, 84)
red = pygame.Color(255, 0, 0)


class Cell:
    def __init__(self, x, y, tile, res):
        self.x, self.y = x, y  # coordinates of the cell
        self.walls = {"top": True, "right": True, "bottom": True, "left": True}  # the sides that are active
        self.visited = False
        self.tile = tile
        self.rows, self.cols = res  # res of the screen

    def draw_current_cell(self, wn):
        x, y = self.x * self.tile, self.y * self.tile

        pygame.draw.rect(wn, turquoise,
                         (x + 2, y + 2, self.tile - 2, self.tile - 2))  # drawing the cell without touching the edges
        return x, y

    def draw(self, wn):
        x, y = self.x * self.tile, self.y * self.tile
        if self.visited:
            pygame.draw.rect(wn, white, (x, y, self.tile, self.tile))

        if self.walls["top"]:
            pygame.draw.line(wn, black, (x, y), (x + self.tile, y), 2)
        if self.walls["right"]:
            pygame.draw.line(wn, black, (x + self.tile, y), (x + self.tile, y + self.tile), 2)
        if self.walls["bottom"]:
            pygame.draw.line(wn, black, (x, y + self.tile), (x + self.tile, y + self.tile), 2)
        if self.walls["left"]:
            pygame.draw.line(wn, black, (x, y), (x, y + self.tile), 2)

    def check_cell(self, x, y, grid_cells):
        find_index = lambda i, j: i + j * self.cols  # finding the index of the neighbors in a one dimensional array.
        if x < 0 or x > self.cols - 1 or y < 0 or y > self.rows - 1:  # index out of range
            return False
        return grid_cells[find_index(x, y)]

    def check_neighbors(self, grid_cells):  # for the maze generation part
        neighbors = []
        top = self.check_cell(self.x, self.y - 1, grid_cells)
        right = self.check_cell(self.x + 1, self.y, grid_cells)
        bottom = self.check_cell(self.x, self.y + 1, grid_cells)
        left = self.check_cell(self.x - 1, self.y, grid_cells)

        if top and not top.visited:  # top is a valid cell that has not been visited
            neighbors.append(top)
        if right and not right.visited:  # right is a valid cell that has not been visited
            neighbors.append(right)
        if bottom and not bottom.visited:  # bottom is a valid cell that has not been visited
            neighbors.append(bottom)
        if left and not left.visited:  # left is a valid cell that has not been visited
            neighbors.append(left)

        if neighbors:  # return a random neighbor if it exists. Else, return false
            return random.choice(neighbors)
        else:
            return False

    def choose_neighbor(self, grid_cells, visited_cells):  # for the maze solving part
        neighbors = []
        top = self.check_cell(self.x, self.y - 1, grid_cells)  # returns the cell on the top
        right = self.check_cell(self.x + 1, self.y, grid_cells)
        bottom = self.check_cell(self.x, self.y + 1, grid_cells)
        left = self.check_cell(self.x - 1, self.y, grid_cells)

        if top and top not in visited_cells:  # top is a valid cell that has not been visited and the wall between them is not the same
            if not self.walls["top"] and not top.walls["bottom"]:  # there is a path between the cells
                neighbors.append(top)
        if right and right not in visited_cells:  # right is a valid cell that has not been visited
            if not self.walls["right"] and not right.walls["left"]:
                neighbors.append(right)
        if bottom and bottom not in visited_cells:  # bottom is a valid cell that has not been visited
            if not self.walls["bottom"] and not bottom.walls["top"]:
                neighbors.append(bottom)
        if left and left not in visited_cells:  # left is a valid cell that has not been visited
            if not self.walls["left"] and not left.walls["right"]:
                neighbors.append(left)

        if neighbors:  # return a random neighbor if it exists. Else, return false
            return neighbors
        else:
            return False
