import random
import string

def generate_codewords_puzzle(word_list, grid_size):
    # Initialize empty grid
    grid = [['#' for _ in range(grid_size)] for _ in range(grid_size)]

    def can_place_word(word, row, col, direction):
        """Check if a word can be placed at the specified row and col."""
        if direction == "H":
            if col + len(word) > grid_size:
                return False
            for i in range(len(word)):
                if grid[row][col + i] != '#':
                    return False
        elif direction == "V":
            if row + len(word) > grid_size:
                return False
            for i in range(len(word)):
                if grid[row + i][col] != '#':
                    return False
        return True

    def place_word(word):
        """Try placing a word randomly in the grid."""
        directions = ["H", "V"]
        random.shuffle(directions)
        attempts = 500  # Increased attempts to improve word placement
        while attempts > 0:
            direction = random.choice(directions)
            row = random.randint(0, grid_size - 1)
            col = random.randint(0, grid_size - 1)
            if can_place_word(word, row, col, direction):
                for i in range(len(word)):
                    if direction == "H":
                        grid[row][col + i] = word[i]
                    else:
                        grid[row + i][col] = word[i]
                return True
            attempts -= 1
        return False

    placed_words = []
    for word in word_list:
        if place_word(word):
            placed_words.append(word)

    # Check if any words were placed
    if not placed_words:
        return None  # Return None if no words could be placed

    # Generate a random number-letter mapping
    alphabet = list(string.ascii_uppercase)
    numbers = list(range(1, 27))
    random.shuffle(numbers)
    letter_to_number = dict(zip(alphabet, numbers))

    coded_grid = []
    solution_grid = []

    for row in grid:
        coded_row = []
        solution_row = []
        for cell in row:
            if cell == '#':
                coded_row.append('#')
                solution_row.append('#')
            else:
                coded_row.append(f"{cell}<sup>{letter_to_number[cell]}</sup>")
                solution_row.append(cell)
        coded_grid.append(coded_row)
        solution_grid.append(solution_row)

    return coded_grid, solution_grid, letter_to_number, placed_words
