import random
import string

def generate_codewords_puzzle(word_list, grid_size):
    # Initialize empty grid with placeholders
    grid = [['#' for _ in range(grid_size)] for _ in range(grid_size)]

    def can_place_word(word, row, col, direction):
        """Check if a word can be placed at the given row and col in the given direction."""
        if direction == "H":  # Horizontal Left to Right
            if col + len(word) > grid_size:
                return False
            for i in range(len(word)):
                if grid[row][col + i] != '#' and grid[row][col + i] != word[i]:
                    return False
        elif direction == "HR":  # Horizontal Right to Left
            if col - len(word) < -1:
                return False
            for i in range(len(word)):
                if grid[row][col - i] != '#' and grid[row][col - i] != word[i]:
                    return False
        elif direction == "V":  # Vertical Top to Bottom
            if row + len(word) > grid_size:
                return False
            for i in range(len(word)):
                if grid[row + i][col] != '#' and grid[row + i][col] != word[i]:
                    return False
        elif direction == "VR":  # Vertical Bottom to Top
            if row - len(word) < -1:
                return False
            for i in range(len(word)):
                if grid[row - i][col] != '#' and grid[row - i][col] != word[i]:
                    return False
        elif direction == "D":  # Diagonal Top-Left to Bottom-Right
            if row + len(word) > grid_size or col + len(word) > grid_size:
                return False
            for i in range(len(word)):
                if grid[row + i][col + i] != '#' and grid[row + i][col + i] != word[i]:
                    return False
        elif direction == "DR":  # Diagonal Bottom-Right to Top-Left
            if row - len(word) < -1 or col - len(word) < -1:
                return False
            for i in range(len(word)):
                if grid[row - i][col - i] != '#' and grid[row - i][col - i] != word[i]:
                    return False
        elif direction == "RD":  # Reverse Diagonal Top-Right to Bottom-Left
            if row + len(word) > grid_size or col - len(word) < -1:
                return False
            for i in range(len(word)):
                if grid[row + i][col - i] != '#' and grid[row + i][col - i] != word[i]:
                    return False
        elif direction == "RDR":  # Reverse Diagonal Bottom-Left to Top-Right
            if row - len(word) < -1 or col + len(word) > grid_size:
                return False
            for i in range(len(word)):
                if grid[row - i][col + i] != '#' and grid[row - i][col + i] != word[i]:
                    return False
        return True

    def place_word(word):
        """Try placing a word in random positions and directions."""
        directions = ["H", "HR", "V", "VR", "D", "DR", "RD", "RDR"]
        random.shuffle(directions)
        positions = [(r, c) for r in range(grid_size) for c in range(grid_size)]
        random.shuffle(positions)

        for row, col in positions:
            for direction in directions:
                if can_place_word(word, row, col, direction):
                    for i in range(len(word)):
                        if direction == "H":
                            grid[row][col + i] = word[i]
                        elif direction == "HR":
                            grid[row][col - i] = word[i]
                        elif direction == "V":
                            grid[row + i][col] = word[i]
                        elif direction == "VR":
                            grid[row - i][col] = word[i]
                        elif direction == "D":
                            grid[row + i][col + i] = word[i]
                        elif direction == "DR":
                            grid[row - i][col - i] = word[i]
                        elif direction == "RD":
                            grid[row + i][col - i] = word[i]
                        elif direction == "RDR":
                            grid[row - i][col + i] = word[i]
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
