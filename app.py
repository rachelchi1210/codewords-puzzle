import streamlit as st
from codewords_puzzle_gen import generate_codewords_puzzle  # Import puzzle generator function

st.title("KDP A-Z Codeword Maker")

# Input for grid size and words
grid_size = st.number_input("Grid Size (10-20):", min_value=10, max_value=20, value=10)
word_input = st.text_area("Enter words (comma separated):")

if word_input:
    word_list = [word.strip().upper() for word in word_input.split(",") if word.strip()]
    coded_grid, original_grid = generate_codewords_puzzle(word_list, grid_size)

    # Checkbox to toggle word visibility
    hide_words = st.checkbox("Hide Words")
    
    display_grid = [['■' if hide_words and cell != ' ' else cell for cell in row] for row in original_grid]

    # Layout for input on the left and puzzle on the right
    col1, col2 = st.columns([1, 2])

    with col1:
        st.subheader("Enter Your Words")
        st.write(word_list)

    with col2:
        st.subheader("Generated Puzzle")
        st.write("### Puzzle Grid")
        st.markdown("<style>table {border-collapse: collapse; width: 100%;}</style>", unsafe_allow_html=True)

        puzzle_html = "<table border='1' style='width:100%; text-align:center;'>"
        for row in display_grid:
            puzzle_html += "<tr>" + "".join(f"<td style='padding:10px;'>{cell}</td>" for cell in row) + "</tr>"
        puzzle_html += "</table>"

        st.markdown(puzzle_html, unsafe_allow_html=True)

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
