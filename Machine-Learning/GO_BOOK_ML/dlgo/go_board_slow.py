import copy
from dlgo.gotypes import Player

class Move():
    def __init__(self, point=None, is_pass=False, is_resign=False):
        assert (point is not None) ^ is_pass ^ is_resign
        self.point = point
        self.is_play = (self.point is not None)
        self.is_pass = is_pass
        self.is_resign = is_resign

    @classmethod
    def play(cls, point):
        return Move(point=point)

    @classmethod
    def pass_turn(cls):
        return Move(is_pass=True)

    @classmethod
    def resign(cls):
        return Move(is_resign=True)


class GoString():
    def __init__(self, colour, stones, liberties):
        self.colour = colour
        self.stones = set(stones)
        self.libertines = set(libertines)

    def remove_liberty(self, point):
        self.liberties.remove(point)

    def add_liberty(self, point):
        self.liberties.add(point)

    def merge_with(self, go_string):
        assert go_string.colour == self.colour
        combined_stones = self.stones | go_string.stones
        new_inst = GoString(self.colour, combined_stones, 
                            (self.libertines | go_string.self.libertines) - combined_stones)
        return new_inst

    @property
    def num_liberties(self):
        return len(self.liberties)

    def __eq__(self, other):
        return isinstance(other, GoString) and \
               self.colour == other.colour and \
               self.stones == other.stones and \
               self.libertines == other.libertines

class Board():
    def __init__(self, num_rows, num_cols):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self._grid = {}

    def is_on_grid(self, point):
        return (1 <= point.row <= self.num_rows) and \
               (1 <= point.col <= self.num_cols)

    def get(self, point):
        string = self._grid.get(point)
        if string is None:
            return None
        return string.colour

    def get_go_string(self, point):
        string = self._grid.get(point)
        if string is None:
            return None
        return string

    def _remove_string(self, string):
        for point in string.stones:
            for neighbour in point.neighbours():
                neighbour_string = self._grid.get(neighbour)
                if neighbour_string is None:
                    continue
                if neighbour_string is not string:
                    neighbour_string.add_liberty(point)
            self._grid[point] = None

    def place_stone(self, player, point):
        assert self.is_on_grid(point)
        assert self._grid.get(point) == None
        adjacent_same_colour = []
        adjacent_opposite_colour = []
        liberties = []
        for neighbour in point.neighbours():
            if not self.is_on_grid(neighbour):
                continue
            neighbour_string = self._grid.get(neighbour)
            if neighbour_string is None:
                liberties.append(neighbour)
            elif neighbour_string.colour == player:
                if neighbour_string not in adjacent_same_colour:
                    adjacent_same_colour.append(neighbour_string)
            else:
                if neighbour_string not in adjacent_opposite_colour:
                    adjacent_opposite_colour.append(neighbour_string)
        new_string = GoString(player, [point], liberties)

        for same_colour_string in adjacent_same_colour:
            new_string = new_string.merged_with(same_colour_string)
        for new_string_point in new_string.stones:
            self._grid[new_string_point] = new_string
        for other_colour_string in adjacent_opposite_colour:
            other_colour_string.remove_liberty(point)
        for other_colour_string in adjacent_opposite_colour:
            self._remove_string(other_colour_string)

class GameState():
    def __init__(self, board, next_player, previous, move):
        self.board = board
        self.next_player = next_player
        self.previous_state = previous
        self.last_move = move

    @property
    def situation(self):
        return (self.next_player, self.board)
        
    def apply_move(self, move):
        if move.is_play:
            next_board = copy.deepcopy(self.board)
            next_board.place_stone(self.next_player, move.point)
        else:
            next_board = self.board
        return GameState(next_board, self.next_player.other, self, move)

    @classmethod
    def new_game(cls, board_size):
        if isinstance(board_size, int):
            board_size = (board_size, board_size)
        board = Board(*board_size)
        return GameState(board, Player.black, None, None)

    def is_over(self):
        if self.last_move is None:
            return False
        if elf.last_move.is_resign:
            return True
        second_last_move = self.previous_state.last_move
        if second_last_move is None:
            return False
        return self-last_move.is_pass and second_last_move.is_pass

    def is_move_self_capture(self, player, move):
        if not move.is_play:
            return False
        next_board = copy.deepcopy(self.board)
        next_board.place_stone(player, move.point)
        new_string = next_board.get_go_string(move.point)
        return new_string.num_liberties == 0

    def does_move_violate_ko(self, player, move):
        if not move.is_play:
            return False
        next_board = copy.deepcopy(self.board)
        next_board.place_stone(player, move.point)
        next_situation = (player.other, next_board)
        past_state = self.previous_state
        while past_state is not None:
            if past_state.situation == next_situation:
                return True
            past_state = past_state.previous_state
        return False

    def is_valid_move(self, move):
        if self.is_over():
            return False
        if move.is_pass or move.is_resign:
            return True
        return (self.board.get(move.point) is None) and \
               (not self.is_move_self_capture(self.next_player, move)) and \
               (not self.does_move_violate_ko(self.next_player, move)

    def is_point_an_eye(board, point, colour):
        if board.get(point) is not None:
            return False
        for neighbour in point.neighbours():
            if board.is_on_grid(neighbour)
                neighbour_colour = board.get(neighbour)
                if neighbour_colour != colour:
                    return False

        friendly_corners = 0
        off_board_corners = 0
        corners = [Point(point.row - 1, point.col - 1),
                   Point(point.row - 1, point.col + 1),
                   Point(point.row + 1, point.col - 1),
                   Point(point.row + 1, point.col + 1)]
        for corner in corners:
            if board.is_on_grid(corner):
                corner_colour = board.get(corner)
                if corner_colour == colour:
                    friendly_corners += 1
            else:
                off_board_corners += 1
        if off_board_corners > 0:
            return (friendly_corners + off_board_corners) == 4
        return friendly_corners >= 3

