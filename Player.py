import numpy as np
import time
class AIPlayer:
    def __init__(self, player_number):
        self.player_number = player_number
        self.type = 'ai'
        self.player_string = 'Player {}:ai'.format(player_number)

    def get_alpha_beta_move(self, board):
        """
        Given the current state of the board, return the next move based on
        the alpha-beta pruning algorithm

        This will play against either itself or a human player

        INPUTS:
        board - a numpy array containing the state of the board using the
                following encoding:
                - the board maintains its same two dimensions
                    - row 0 is the top of the board and so is
                      the last row filled
                - spaces that are unoccupied are marked as 0
                - spaces that are occupied by player 1 have a 1 in them
                - spaces that are occupied by player 2 have a 2 in them

        RETURNS:
        The 0 based index of the column that represents the next move
        """
    
        def nextEmpty(arr):
            nxt = []
            for col in range(7):
                Ro = -1
                Co = -1
                for row in range(5,-1,-1):
                    if arr[row][col]==0:
                        Ro = row
                        Co = col
                        nxt.append([Ro,Co])
                        break
            return nxt
        def MinValue(board,depth,alpha,beta):
            var = float('inf')
            nxtutility = 0
            bestmove = -1
            nxtmoves = nextEmpty(board)
            # print("MinMoves")
            # print(nxtmoves)
            if depth==4:
                for move in nxtmoves:
                    newboard = np.copy(board)
                    newboard[move[0]][move[1]] = 2
                    nxtutility = self.evaluation_function(newboard)
                    if nxtutility<var:
                        var = nxtutility
                        bestmove = move[1]
                    beta = min(beta,var)
                    if beta<=alpha:
                        break
                return [bestmove,var]
            depth+=1
            for move in nxtmoves:
                newboard = np.copy(board)
                newboard[move[0]][move[1]] = 2
                nxtutility = MaxValue(newboard,depth,alpha,beta)[1]
                if nxtutility<var:
                    var = nxtutility
                    bestmove = move[1]
                    beta = min(beta,var)
                if beta<=alpha:
                    return [bestmove,var]
            return [bestmove,var]
        def MaxValue(board,depth,alpha,beta):
            var = float('-inf')
            nxtutility = 0
            bestmove = -1
            nxtmoves = nextEmpty(board)
            if depth==4:
                for move in nxtmoves:
                    newboard = np.copy(board)
                    newboard[move[0]][move[1]] = 1
                    nxtutility = self.evaluation_function(newboard)
                    if nxtutility>var:
                        var = nxtutility
                        bestmove = move[1]
                    alpha = max(alpha,var)
                    if beta<=alpha:
                        break
                return [bestmove,var]
            depth+=1
            for move in nxtmoves:
                newboard = np.copy(board)
                newboard[move[0]][move[1]] = 1
                nxtutility = MinValue(newboard,depth,alpha,beta)[1]
                if nxtutility>var:
                        var = nxtutility
                        bestmove = move[1]
                        alpha = max(alpha,var)
                if alpha>=beta:
                    return [bestmove,var]
            return [bestmove,var]
        if self.player_number ==1:
            return MaxValue(board,1,-100000000000000000,1000000000000000000)[0]
        
        else:
            return MinValue(board,1,-100000000000000000,1000000000000000000)[0]
    
    def get_expectimax_move(self, board):
        """
        Given the current state of the board, return the next move based on
        the expectimax algorithm.

        This will play against the random player, who chooses any valid move
        with equal probability

        INPUTS:
        board - a numpy array containing the state of the board using the
                following encoding:
                - the board maintains its same two dimensions
                    - row 0 is the top of the board and so is
                      the last row filled
                - spaces that are unoccupied are marked as 0
                - spaces that are occupied by player 1 have a 1 in them
                - spaces that are occupied by player 2 have a 2 in them

        RETURNS:
        The 0 based index of the column that represents the next move
        """
        def nextEmpty(arr):
            nxt = []
            for col in range(7):
                Ro = -1
                Co = -1
                for row in range(5,-1,-1):
                    if arr[row][col]==0:
                        Ro = row
                        Co = col
                        nxt.append([Ro,Co])
                        break
            return nxt
        
        if self.player_number==1:
            def Rand(board,depth):
                nxtmvs = nextEmpty(board)
                totalutil = 0
                noofmoves = len(nxtmvs)
                depth+=1
                for move in nxtmvs:
                    newboard = np.copy(board)
                    newboard[move[0]][move[1]]=1
                    totalutil+=Max(newboard,depth)[0]
                return totalutil/noofmoves


            def Max(board,depth):
                bestmove = -1
                maxutil = 0
                nxtutil = 0
                nxtmvs = nextEmpty(board)
                depth+=1
                for move in nxtmvs:
                    newboard = np.copy(board)
                    newboard[move[0]][move[1]]=1
                    if depth==4:
                        nxtutil=self.evaluation_function(newboard)
                    else:
                        nxtutil = Rand(newboard,depth)
                    if nxtutil>maxutil:
                        maxutil=nxtutil
                        bestmove=move[1]
                return [maxutil,bestmove]
            return Max(board,1)[1]
        else:
            def Rand(board,depth):
                nxtmvs = nextEmpty(board)
                totalutil = 0
                noofmoves = len(nxtmvs)
                depth+=1
                for move in nxtmvs:
                    newboard = np.copy(board)
                    newboard[move[0]][move[1]]=1
                    totalutil+=Min(newboard,depth)[0]
                return totalutil/noofmoves


            def Min(board,depth):
                bestmove = -1
                minutil = 100000
                nxtutil = 0
                nxtmvs = nextEmpty(board)
                depth+=1
                for move in nxtmvs:
                    newboard = np.copy(board)
                    newboard[move[0]][move[1]]=1
                    if depth==4:
                        nxtutil=self.evaluation_function(newboard)
                    else:
                        nxtutil = Rand(newboard,depth)
                    if nxtutil<minutil:
                        minutil=nxtutil
                        bestmove=move[1]
                return [minutil,bestmove]
            return Min(board,1)[1]



    def evaluation_function(self, board):
        """
        Given the current stat of the board, return the scalar value that 
        represents the evaluation function for the current player
       
        INPUTS:
        board - a numpy array containing the state of the board using the
                following encoding:
                - the board maintains its same two dimensions
                    - row 0 is the top of the board and so is
                      the last row filled
                - spaces that are unoccupied are marked as 0
                - spaces that are occupied by player 1 have a 1 in them
                - spaces that are occupied by player 2 have a 2 in them

        RETURNS:
        The utility value for the current board
        """
        score = 0
        def evaluate_window(window):
            score = 0
            player1_count = np.count_nonzero(window == 1)
            player2_count = np.count_nonzero(window == 2)

            if player1_count == 4:
                score += 100
            elif player1_count == 3 and player2_count == 0:
                score += 5
            elif player1_count == 2 and player2_count == 0:
                score += 2
            elif player1_count == 1 and player2_count == 0:
                score += 1

            if player2_count == 4:
                score -= 100
            elif player2_count == 3 and player1_count == 0:
                score -= 5
            elif player2_count == 2 and player1_count == 0:
                score -= 2
            elif player2_count == 1 and player1_count == 0:
                score -= 1

            return score
        # Check horizontal lines
        for row in range(6):
            for col in range(4):
                window = board[row, col:col+4]
                score += evaluate_window(window)

        # Check vertical lines
        for col in range(7):
            for row in range(3):
                window = board[row:row+4, col]
                score += evaluate_window(window)

        # Check positively sloped diagonals
        for row in range(3):
            for col in range(4):
                window = board[row:row+4, col:col+4].diagonal()
                score += evaluate_window(window)

        # Check negatively sloped diagonals
        for row in range(3):
            for col in range(3, 7):
                window = np.flip(board[row:row+4, col-3:col+1], axis=1).diagonal()
                score += evaluate_window(window)

        return score

    

        
            

class RandomPlayer:
    def __init__(self, player_number):
        self.player_number = player_number
        self.type = 'random'
        self.player_string = 'Player {}:random'.format(player_number)

    def get_move(self, board):
        """
        Given the current board state select a random column from the available
        valid moves.

        INPUTS:
        board - a numpy array containing the state of the board using the
                following encoding:
                - the board maintains its same two dimensions
                    - row 0 is the top of the board and so is
                      the last row filled
                - spaces that are unoccupied are marked as 0
                - spaces that are occupied by player 1 have a 1 in them
                - spaces that are occupied by player 2 have a 2 in them

        RETURNS:
        The 0 based index of the column that represents the next move
        """
        valid_cols = []
        for col in range(board.shape[1]):
            if 0 in board[:,col]:
                valid_cols.append(col)

        return np.random.choice(valid_cols)


class HumanPlayer:
    def __init__(self, player_number):
        self.player_number = player_number
        self.type = 'human'
        self.player_string = 'Player {}:human'.format(player_number)

    def get_move(self, board):
        """
        Given the current board state returns the human input for next move

        INPUTS:
        board - a numpy array containing the state of the board using the
                following encoding:
                - the board maintains its same two dimensions
                    - row 0 is the top of the board and so is
                      the last row filled
                - spaces that are unoccupied are marked as 0
                - spaces that are occupied by player 1 have a 1 in them
                - spaces that are occupied by player 2 have a 2 in them

        RETURNS:
        The 0 based index of the column that represents the next move
        """

        valid_cols = []
        for i, col in enumerate(board.T):
            if 0 in col:
                valid_cols.append(i)

        move = int(input('Enter your move: '))

        while move not in valid_cols:
            print('Column full, choose from:{}'.format(valid_cols))
            move = int(input('Enter your move: '))

        return move

