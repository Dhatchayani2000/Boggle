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
print(result)  # True or False ```

Replace boggle_board and word with your own values. The function returns True if the word is found, and False otherwise.

##Example

# Test cases
print(find_word(boggle_board, "C"))  # True
print(find_word(boggle_board, "EAR"))  # True
print(find_word(boggle_board, "EARS"))  # False
print(find_word(boggle_board, "BAILER"))  # True
print(find_word(boggle_board, "RSCAREIOYBAILNEA"))  # True
print(find_word(boggle_board, "CEREAL"))  # False
print(find_word(boggle_board, "ROBES"))  # False

