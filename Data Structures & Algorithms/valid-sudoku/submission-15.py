class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        i = 0
        full_map = {"row":{}, "col":{}, "box":{}}
        while i < len(board):
            for x in range(len(board[i])):
                if board[i][x] != ".":
                    # add to row_map
                    if i not in full_map["row"]:
                        full_map["row"][i] = [board[i][x]]
                    elif board[i][x] in full_map["row"][i]:
                        return False
                    else:
                        full_map["row"][i].append(board[i][x])

                    # add to col_map
                    if x not in full_map["col"]:
                        full_map["col"][x] = [board[i][x]]
                    elif board[i][x] in full_map["col"][x]:
                        return False
                    else:
                        full_map["col"][x].append(board[i][x])

                    # add_to_box_map
                    box = (i // 3) * 3 + (x // 3)

                    if box not in full_map["box"]:
                        full_map["box"][box] = [board[i][x]]
                    elif board[i][x] in full_map["box"][box]:
                        return False
                    else:
                        full_map["box"][box].append(board[i][x])

            i += 1
        return True
