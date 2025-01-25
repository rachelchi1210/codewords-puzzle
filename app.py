import streamlit as st
from codewords_puzzle_gen import generate_codewords_puzzle  # Import the puzzle generator function

st.title("Codewords Puzzle Generator")

# User input for words and grid size
word_input = st.text_area("Enter words (comma separated):")
grid_size = st.slider("Select grid size", 5, 15, 8)

if st.button("Generate Puzzle"):
    word_list = [word.strip().upper() for word in word_input.split(",") if word.strip()]
    if not word_list:
        st.error("Please enter at least one word.")
    else:
        coded_grid, hints, _, _ = generate_codewords_puzzle(word_list, grid_size)

        st.subheader("Coded Grid:")
        for row in coded_grid:
            st.text(" ".join(row))

        st.subheader("Hints:")
        for letter, number in hints.items():
            st.text(f"{letter} = {number}")

        st.subheader("Solution:")
        for row in _:
            st.text(" ".join(row))
