import streamlit as st
from codewords_puzzle_gen import generate_codewords_puzzle  # Import puzzle generator function

st.title("Codeword Puzzle Generator")

# Input for grid size and words
grid_size = st.number_input("Grid Size (10-20):", min_value=10, max_value=20, value=10)
word_input = st.text_area("Enter words (comma separated):")

if word_input:
    word_list = [word.strip().upper() for word in word_input.split(",") if word.strip()]
    coded_grid, original_grid = generate_codewords_puzzle(word_list, grid_size)
    
    # Checkbox to toggle word visibility
    hide_words = st.checkbox("Hide Words")
    display_grid = [['■' if hide_words and cell != ' ' else cell for cell in row] for row in original_grid]

    st.subheader("Generated Puzzle")
    for row in display_grid:
        st.text(" ".join(row))

# Buttons to manually show/hide words
col1, col2 = st.columns(2)
with col1:
    if st.button("Show Words"):
        st.session_state['hide_words'] = False
        st.experimental_rerun()

with col2:
    if st.button("Hide Words"):
        st.session_state['hide_words'] = True
        st.experimental_rerun()

