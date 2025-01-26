import random
import string

def generate_codewords_puzzle(word_list, grid_size):
    # Initialize empty grid with placeholders
    grid = [['#' for _ in range(grid_size)] for _ in range(grid_size)]

    def can_place_word(word, row, col, direction):
        """Check if a word can be placed at the given row and col in the given direction."""
        if direction == "H":
            if col + len(word) > grid_size:
                return False
            for i in range(len(word)):
                if grid[row][col + i] != '#' and grid[row][col + i] != word[i]:
                    return False
        elif direction == "V":
            if row + len(word) > grid_size:
                return False
            for i in range(len(word)):
                if grid[row + i][col] != '#' and grid[row + i][col] != word[i]:
                    return False
        elif direction == "D":  # Diagonal placement
            if row + len(word) > grid_size or col + len(word) > grid_size:
                return False
            for i in range(len(word)):
                if grid[row + i][col + i] != '#' and grid[row + i][col + i] != word[i]:
                    return False
        return True

    def place_word(word):
        """Try placing a word in random positions and directions."""
        directions = ["H", "V", "D"]
        random.shuffle(directions)
        positions = [(r, c) for r in range(grid_size) for c in range(grid_size)]
        random.shuffle(positions)

        for row, col in positions:
            for direction in directions:
                if can_place_word(word, row, col, direction):
                    for i in range(len(word)):
                        if direction == "H":
                            grid[row][col + i] = word[i]
                        elif direction == "V":
                            grid[row + i][col] = word[i]
                        elif direction == "D":
                            grid[row + i][col + i] = word[i]
                    return True
        return False

    # Place words from longest to shortest for better fitting
    word_list.sort(key=len, reverse=True)
    placed_words = []

    for word in word_list:
        if place_word(word):
            placed_words.append(word)

    # Check if all words have been placed
    if len(placed_words) < len(word_list):
        print(f"Warning: Could not place all words. Placed {len(placed_words)} out of {len(word_list)}")

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
