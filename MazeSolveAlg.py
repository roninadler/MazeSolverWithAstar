from MazeCell import *

def astar_alg(maze, start, end):
    open = []
    closed = []

    start_cell = MazeCell(start, None)
    end_cell = MazeCell(end, None)

    open.append(start_cell)

    while len(open) > 0:
        open.sort()  # Sort the open list to get the cell with the lowest cost first
        current_cell = open.pop(0)  # Cell with lowest cost

        if current_cell == end_cell:
            return reconstruct_path(start_cell,current_cell)

        closed.append(current_cell)  # Add curr cell to closed list

        neighbors = current_cell.get_neighbors()

        for neighbor in neighbors:
            (x,y) = neighbor
            if x >= 5 or y>=5 or x < 0 or y < 0:
                continue
            cell_value = maze[x][y]
            if cell_value == 1:
                continue

            neighbor = MazeCell(neighbor, current_cell)

            if neighbor in closed:
                continue

            neighbor.calculate_costs(end_cell)

            if add_neighbor_to_open(open, neighbor):
                open.append(neighbor)

    return None


def add_neighbor_to_open(open, neighbor):
    for cell in open:
        #if neighbor.compareCellsPosition(cell) and neighbor.f >= cell.f:
        if neighbor == cell and neighbor.f >= cell.f:
            return False
    return True

def reconstruct_path(start_cell, current_cell):
    path = []
    while current_cell != start_cell:
        path.append(current_cell.position)
        current_cell = current_cell.prevCell
    return path[::-1]