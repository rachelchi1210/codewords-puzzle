import streamlit as st
from codewords_puzzle_gen import generate_codewords_puzzle  # Import the puzzle generator function

st.title("KDP A-Z Codeword Maker")

grid_size = st.number_input("Grid Size (10-20):", min_value=10, max_value=20, value=10)
word_input = st.text_area("Enter words (comma separated):")

if 'show_solution' not in st.session_state:
    st.session_state['show_solution'] = False

if word_input:
    word_list = [word.strip().upper() for word in word_input.split(",") if word.strip()]
    coded_grid, solution_grid = generate_codewords_puzzle(word_list, grid_size)

    # Define columns FIRST
    col1, col2 = st.columns([1, 2])

    with col1:
        st.subheader("Enter Your Words")
        st.write(word_list)

    with col2:
        st.subheader("Generated Puzzle")
        puzzle_html = """
        <style>
            td.black { background-color: black; width: 30px; height: 30px; }
            td { text-align: center; font-size: 20px; padding: 15px; }
        </style>
        <table border='1' style='border-collapse: collapse; width:100%; text-align:center;'>
        """

        for row in coded_grid:
            puzzle_html += "<tr>"
            for cell in row:
                if cell == '█':  # Ensure black cells are filled
                    puzzle_html += "<td class='black'></td>"
                else:
                    puzzle_html += f"<td>{cell}</td>"
            puzzle_html += "</tr>"

        puzzle_html += "</table>"
        st.markdown(puzzle_html, unsafe_allow_html=True)

# Buttons to toggle visibility
col1, col2 = st.columns(2)
with col1:
    if st.button("Show Solution"):
        st.session_state['show_solution'] = True
        st.rerun()
with col2:
    if st.button("Hide Solution"):
        st.session_state['show_solution'] = False
        st.rerun()
