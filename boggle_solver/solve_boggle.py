from boggleboard import Board
from bogglesolver import BoggleSolver
from pprint import pprint


def main():
    board = Board(5)
    solver = BoggleSolver("/Users/austin/boggle_solver/boggle_solver/examples/safedict_full.txt")
    solutions = solver.solve_board(board)
    print(board)
    pprint(solutions)


if __name__ == "__main__":
    main()