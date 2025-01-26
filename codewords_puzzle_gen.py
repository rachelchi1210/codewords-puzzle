import streamlit as st
import random
import string

def generate_codewords_puzzle(word_list, grid_size):
    grid = [[' ' for _ in range(grid_size)] for _ in range(grid_size)]
    
    def place_word(word):
        direction = random.choice(['H', 'V'])
        max_row = grid_size if direction == 'H' else grid_size - len(word)
        max_col = grid_size - len(word) if direction == 'H' else grid_size
        
        for _ in range(100):
            row, col = random.randint(0, max_row - 1), random.randint(0, max_col - 1)
            positions = [(row, col + i) if direction == 'H' else (row + i, col) for i in range(len(word))]
            
            if all(grid[r][c] == ' ' for r, c in positions):
                for i, (r, c) in enumerate(positions):
                    grid[r][c] = word[i]
                return
    
    for word in word_list:
        place_word(word.upper())
    
    letters = list(set(c for row in grid for c in row if c != ' '))
    letter_to_number = {letter: str(i + 1) for i, letter in enumerate(letters)}
    
    coded_grid = [[letter_to_number.get(grid[r][c], '.') for c in range(grid_size)] for r in range(grid_size)]
    
    return coded_grid, grid

def display_grid(grid, hide_letters):
    return [['■' if hide_letters and cell != ' ' else cell for cell in row] for row in grid]

st.title("KDP A-Z Codeword Maker")

grid_size = st.number_input("Grid Size (10-20):", min_value=10, max_value=20, value=10)
word_input = st.text_area("Enter words (comma separated):")

if word_input:
    word_list = [word.strip().upper() for word in word_input.split(",") if word.strip()]
    coded_grid, original_grid = generate_codewords_puzzle(word_list, grid_size)
    
    hide_words = st.checkbox("Hide Words")
    display_puzzle = display_grid(original_grid, hide_words)
    
    st.subheader("Generated Puzzle")
    for row in display_puzzle:
        st.text(" ".join(row))

col1, col2 = st.columns(2)
with col1:
    if st.button("Show Words"):
        st.session_state['hide_words'] = False
        st.experimental_rerun()
with col2:
    if st.button("Hide Words"):
        st.session_state['hide_words'] = True
        st.experimental_rerun()

