from boggleboard import Board
from bogglesolver import BoggleSolver
from pprint import pprint


def main():
    board = Board(4)
    solver = BoggleSolver("/Users/austin/boggle_solver/boggle_solver/dictionaries/safedict_full.txt")
    solutions = solver.solve_board(board)
    print(board)
    pprint(solutions)


if __name__ == "__main__":
    main()