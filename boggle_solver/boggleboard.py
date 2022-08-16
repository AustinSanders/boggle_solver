import random
import string
from itertools import product

class Board():
    """ Basic representation of a Boggle board.

    Describes an n x n matrix populated with random (or predetermined) characters.
    """
    def __init__(self, size=4, grid=[]):
        self.size = size
        self.grid = grid or self.generate_grid()


    def __repr__(self):
        out = ""
        for i in self.grid:
            for j in i:
                out += j + " "
            out += "\n"
        return out


    @property
    def size(self):
        """ The size of the board represented as a square matrix of size x size."""
        return self._size


    @size.setter
    def size(self, val):
        if not hasattr(self, "_size"):
            self._size = val
        else:
            print("Dynamic reallocation of board size is not supported!\n"
                  "Please purchase a new board for $2.99.")


    @property
    def grid(self):
        """The n x n grid of tiles on the board."""
        return self._grid


    @grid.setter
    def grid(self, vals):
        if all([len(a) == self.size for a in vals]) and len(vals) == self.size:
            self._grid = vals
        else:
            print(f"Invalid grid supplied.  Please supply a {self.size}x{self.size} grid.")


    def generate_grid(self):
        """ Randomly generate characters to populate the board.

        Returns
        -------
        List of lists
            An n x n matrix of randomly generated, lower-case alpha characters

        """
        return [[random.choice(string.ascii_lowercase) for i in range(self.size)] for j in range(self.size)]


    def neighbors(self, tile):
        """ Returns neighboring tiles.
        
        Returns a list of lists (pairs) which constitutes tiles that are adjacent to the specified tile.
        Neighbors are guaranteed to be valid tiles and the return excludes the specified tile.

        Parameters
        ----------
        tile : 2-element iterable [int, int]
            The tile for which neighbors will be found.

        Examples
        --------
        >>> print(board.neighbors(0,1))
        [[0, 0], [0, 2], [1, 0], [1, 1], [1, 2]]

        Returns
        -------
        list of lists
            List of lists containing indices of neighboring tiles
        """
        row, col = tile
        neighbors = [[x,y] for x, y in product(range(row-1, row+2), range(col-1, col+2)) if [x,y] != tile and self.is_valid([x,y])]
        return neighbors

    
    def is_valid(self, tile):
        """ Returns True if tile is within the dimensions of the board, else False

        Parameters
        ----------
        tile : 2-element iterable [int, int]
            The tile for which the validity check will be performed.

        Returns
        -------
        bool : True if tile is valid else False
        """
        row, col = tile
        return 0 <= row < self.size and 0 <= col < self.size