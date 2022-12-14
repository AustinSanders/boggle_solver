from pygtrie import CharTrie

class BoggleSolver():
    """ A Boggle solver based on a prefix trie.
    
    Attributes
    ----------
    dictionary : pygtrie.CharTrie
        A user-defined dictionary used as the basis for the solver
    """
    def __init__(self, filepath):
        self.dictionary = CharTrie()
        self.load(filepath)


    def load(self, filepath):
        """ Load a user-defined dictionary and parse into prefix trie

        Parameters
        ----------
        filepath : str
            A filepath containing a line-delimited list of words to be found by the solver

        Returns
        -------
        None
        """
        with(open(filepath) as f):
            for line in f.readlines():
                self.dictionary[line.strip()] = 1


    def solve_board(self, board, min_length=3):
        """ Find all words defined in self.dictionary that appear on the board

        Searches the board for all words available in the dictionary.  Searches up, down,
        left, right, and diagonal, and words are not required to be in a linear path,
        i.e. a word may be found by traversing in sequence right, down, down, right, down.

        Parameters
        ----------
        board : bogglesolver.Board
            A board object prepopulated with tiles.

        min_length : integer
            The minimum number of letters required to form a valid word.

        Returns
        -------
        dictionary:  
            {word: [[row1, col1][row2, col2][row3, col3]}
        """
        solutions = {}
        # Perform local search by iterating through possible starting points
        for ridx, row in enumerate(board.grid):
            for cidx, _ in enumerate(row):
                solutions.update(self.solve_tile(board, [[ridx, cidx]]))
        # Trim invalid (short) words from the dictionary
        solutions = {k:solutions[k] for k in solutions if len(k)>=min_length}
        return solutions


    def solve_tile(self, board, path, solutions={}):
        """ Find all words beginning at the specified tile

        Helper function for BoggleSolver.solve_board().  Recursively searches
        all reachable nodes for valid words.

        Parameters
        ----------
        board : boggleboard.Board
            The board on which the tile exists

        path : list of lists of ints
            list of lists of integer indices indicating current traversal

        solutions : dictionary of list of lists
            Solutions gathered over the course of this traversal

        Returns
        -------
        dict :
            A dictionary of form {word: [[row1, col1], [row2, col2], [row3, col3]]}
              which contains all solutions found in the current traversal.
              Indices indicate the traversal path at which the word can be found.
        """
        if not path:
            return solutions
        # Convert path of grid indices to string
        prefix = "".join([board.grid[x][y] for x, y in path])
        if not self.dictionary.has_subtrie(prefix):
            # If current prefix is not in the tree, no use in checking further
            return solutions
        if self.dictionary.has_key(prefix):
            # If current substring is a word, add to dict of solutions and keep looking
            solutions[prefix] = path
        for new_path in ([*path, [x,y]] for x, y in board.neighbors(path[-1]) if [x,y] not in path):
            solutions.update(self.solve_tile(board, new_path, solutions))
        return solutions
