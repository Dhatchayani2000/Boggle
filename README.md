# Boggle Board Word Search

This Python function determines whether a given string is a valid guess on a Boggle board, following the rules of Boggle. It uses depth-first search (DFS) to explore all possible paths on the board.

## Usage

```python
from boggle import find_word

# Create your Boggle board as a 2D list
boggle_board = [
    ["E","A","R","A"],
    ["N","L","E","C"],
    ["I","A","I","S"],
    ["B","Y","O","R"]
]

# Define the word you want to search for
word = "C"

# Call the find_word function to check if the word is valid
result = find_word(boggle_board, word)

# Print the result
print(result)  # True or False
