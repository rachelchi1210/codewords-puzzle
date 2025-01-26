import streamlit as st
from codewords_puzzle_gen import generate_codewords_puzzle

def create_grid_display(grid, show_letters):
    return [['■' if cell == ' ' else (cell if show_letters else '?') for cell in row] for row in grid]

st.title("KDP A-Z Codeword Maker")

grid_size = st.number_input("Grid Size (10-20):", min_value=10, max_value=20, value=10)
word_input = st.text_area("Enter words (comma separated):")

if 'show_letters' not in st.session_state:
    st.session_state['show_letters'] = False

if word_input:
    word_list = [word.strip().upper() for word in word_input.split(",") if word.strip()]
    coded_grid, original_grid = generate_codewords_puzzle(word_list, grid_size)
    display_grid = create_grid_display(original_grid, st.session_state['show_letters'])

    col1, col2 = st.columns([1, 2])

    with col1:
        st.subheader("Word List")
        st.write(word_list)
    
    with col2:
        st.subheader("Puzzle Grid")
        puzzle_html = "<table border='1' style='width:100%; text-align:center;'>"
        for row in display_grid:
            puzzle_html += "<tr>" + "".join(f"<td style='padding:10px;'>{cell}</td>" for cell in row) + "</tr>"
        puzzle_html += "</table>"
        st.markdown(puzzle_html, unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    if st.button("Show Letters"):
        st.session_state['show_letters'] = True
        st.rerun()
with col2:
    if st.button("Hide Letters"):
        st.session_state['show_letters'] = False
        st.rerun()
