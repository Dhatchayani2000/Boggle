def find_word(board, word):
    def dfs(i, j, k):
        # Check if (i, j) is within bounds and the current cell matches the word character
        if 0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] == word[k]:
            # Base case: If the entire word is found, return True
            if k == len(word) - 1:
                return True
            
            # Mark the current cell as visited
            original_char, board[i][j] = board[i][j], "#"
            
            # Explore neighboring cells recursively
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == 0 and dy == 0:
                        continue
                    if dfs(i + dx, j + dy, k + 1):
                        return True
            
            # Restore the original character and backtrack
            board[i][j] = original_char
        
        return False
    
    # Iterate through the board to start the search from each cell
    for i in range(len(board)):
        for j in range(len(board[0])):
            if dfs(i, j, 0):
                return True
    
    return False

# Example usage:
testBoard = [
    ["E","A","R","A"],
    ["N","L","E","C"],
    ["I","A","I","S"],
    ["B","Y","O","R"]
]

print(find_word(testBoard, "C"))  # True
print(find_word(testBoard, "EAR"))  # True
print(find_word(testBoard, "EARS"))  # False
print(find_word(testBoard, "BAILER"))  # True
print(find_word(testBoard, "RSCAREIOYBAILNEA"))  # True
print(find_word(testBoard, "CEREAL"))  # False
print(find_word(testBoard, "ROBES"))  # False
