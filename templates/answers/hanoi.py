# Object oriented solution


class Towers:
    def __init__(self, disks):
        self.disks = disks
        self.moves = [[[x for x in range(disks, 0, -1)], [], []]]
     
        

    def move(self, last_moves: list[list], start: int, end: int):
        # [[1], [2], [3]]
        first, second, third = last_moves[0][:], last_moves[1][:], \
                                last_moves[2][:]
        new_moves = [first, second, third]
        x = new_moves[start].pop()
        new_moves[end].append(x)
        self.moves.append(new_moves)
        return self.moves

    def solve(self, start=None, end=None, temp=None, n=None):
        if n is None:
            n = self.disks
        if start is None and end is None and temp is None:
            start, temp, end = 0, 1, 2
        if n == 1:
            self.move(self.moves[-1], start, end)
            return self.moves
        else:
            self.solve(start, temp, end, n - 1)
            self.move(self.moves[-1], start, end)
            self.solve(temp, end, start, n - 1)
            return self.moves
       


### Array Solution


def move(moves, start, end) -> list:
    last_move = moves[-1]
    first, second, last = [x for x in last_move[0]], \
                        [y for y in last_move[1]], [z for z in last_move[2]] 
    new_move = [first, second, last]
    moving_disk = new_move[start].pop()
    new_move[end].append(moving_disk)
    return new_move

def solve_hanoi(disks: int, moves=None, start=None, end=None, temp=None):
    if moves is None:
        moves = [[[x for x in range(disks, 0, -1)], [], []]]
    if start is None and end is None and temp is None:
        start, end, temp = 0, 2, 1
    if disks == 1:
        moves.append(move(moves, start, end))
        return moves
        
    else:
        moves = solve(disks - 1, moves, start, temp, end)
        moves.append(move(moves, start, end))
        moves = solve(disks - 1, moves, temp, end, start)
        return moves



        
        