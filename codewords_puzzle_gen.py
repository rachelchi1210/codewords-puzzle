import random
import string

def generate_codewords_puzzle(word_list, grid_size):
    grid = [['#' for _ in range(grid_size)] for _ in range(grid_size)]

    def can_place_word(word, row, col, direction):
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
        directions = ["H", "V"]
        random.shuffle(directions)  # Try horizontal and vertical in random order
        attempts = 500  # Increase attempts to ensure better placement
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

    # Generate a random number-letter mapping
    alphabet = list(string.ascii_uppercase)
    numbers = list(range(1, 27))
    random.shuffle(numbers)
    letter_to_number = dict(zip(alphabet, numbers))

