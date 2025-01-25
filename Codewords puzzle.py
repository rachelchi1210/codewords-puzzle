import random
import string
import streamlit as st


def generate_codewords_puzzle(word_list, grid_size):
    # Step 1: Create empty grid
    grid = [[' ' for _ in range(grid_size)] for _ in range(grid_size)]
    used_positions = set()

    def place_word(word):
        direction = random.choice(['H', 'V'])  # H for horizontal, V for vertical
        max_row = grid_size if direction == 'H' else grid_size - len(word)
        max_col = grid_size - len(word) if direction == 'H' else grid_size

        for _ in range(100):  # Try multiple positions
            row, col = random.randint(0, max_row - 1), random.randint(0, max_col - 1)
            positions = [(row, col + i) if direction == 'H' else (row + i, col) for i in range(len(word))]

            if all(grid[r][c] == ' ' for r, c in positions):
                for i, (r, c) in enumerate(positions):
                    grid[r][c] = word[i]
                    used_positions.add((r, c))
                return True
        return False

    # Step 2: Fill the grid with words
    for word in word_list:
        place_word(word.upper())

    # Step 3: Assign numbers to letters
    letters = list(set(c for row in grid for c in row if c != ' '))
    letter_to_number = {letter: str(i + 1) for i, letter in enumerate(letters)}

    # Step 4: Create the coded grid
    coded_grid = [[letter_to_number[grid[r][c]] if grid[r][c] != ' ' else '.' for c in range(grid_size)] for r in
                  range(grid_size)]

    # Step 5: Provide hints
    hints = random.sample(letters, max(1, len(letters) // 4))  # Provide hints for 25% of the letters
    hints_dict = {letter: letter_to_number[letter] for letter in hints}

    return coded_grid, hints_dict, letter_to_number, grid


# Streamlit interface
st.title("Codewords Puzzle Generator")

word_input = st.text_area("Enter words (comma separated)")
word_list = [word.strip().upper() for word in word_input.split(',') if word.strip()]
grid_size = st.slider("Select grid size", 5, 15, 8)

if st.button("Generate Puzzle"):
    coded_grid, hints, letter_to_number, original_grid = generate_codewords_puzzle(word_list, grid_size)

    st.subheader("Coded Grid:")
    for row in coded_grid:
        st.text(' '.join(row))

    st.subheader("Hints:")
    for letter, number in hints.items():
        st.text(f"{letter} = {number}")

    st.subheader("Solution:")
    for row in original_grid:
        st.text(' '.join(row))
