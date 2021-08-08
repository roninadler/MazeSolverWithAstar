class MazeCell:
    # Initialize the class
    def __init__(self, position:(), prevCell:()):
        self.position = position
        self.prevCell = prevCell

        # Distance to start node
        self.g = 0

        # Distance to goal node
        self.h = 0

        # Total cost
        self.f = 0

    def __lt__(self, other):
        return self.position < other.position
    def __eq__(self, other):
        return self.position == other.position

    def __repr__(self):
        return ('({0},{1})'.format(self.position, self.f))

    def sortCellsByTotalDistances(self, other) -> bool:
        return self.f < other.f

    def getCellFormattedDetails(self) -> str:
        return '({0},{1})'.format(self.position, self.f)

    def calculate_costs(self, end_cell):
        self.g = self.prevCell.g + 1
        self.h = self.Manhattan_distance(end_cell)
        self.f = self.g + self.h

    def Manhattan_distance(self, end_cell):
        (x1, y1) = self.position
        (x2, y2) = end_cell.position
        return abs(x1 - x2) + abs(y1 - y2)

    def get_neighbors(self):
        (x, y) = self.position
        return [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]