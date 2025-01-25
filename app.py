import streamlit as st
from codewords_puzzle_gen import generate_codewords_puzzle  # Import your function

st.title("Codewords Puzzle Generator")

# User input
word_list = st.text_area("Enter words (comma separated)").split(",")
grid_size = st.number_input("Grid size", min_value=5, max_value=15, value=8)

if st.button("Generate Puzzle"):
    coded_grid, hints, _, _ = generate_codewords_puzzle(word_list, grid_size)

    st.subheader("Coded Grid:")
    for row in coded_grid:
        st.text(" ".join(row))

    st.subheader("Hints:")
    for letter, number in hints.items():
        st.text(f"{letter} = {number}")
