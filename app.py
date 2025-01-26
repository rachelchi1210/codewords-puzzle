import streamlit as st
from codewords_puzzle_gen import generate_codewords_puzzle

st.title("KDP A-Z Codeword Maker")

# Input for grid size and words
grid_size = st.number_input("Grid Size (10-20):", min_value=10, max_value=20, value=10)
word_input = st.text_area("Enter words (comma separated):")

# Session state for showing solution
if 'show_solution' not in st.session_state:
    st.session_state['show_solution'] = False

if word_input:
    word_list = [word.strip().upper() for word in word_input.split(",") if word.strip()]
    coded_grid, solution_grid, letter_to_number = generate_codewords_puzzle(word_list, grid_size)

    col1, col2 = st.columns([1, 2])

    with col1:
        st.subheader("Word List")
        st.write(word_list)

    with col2:
        st.subheader("Generated Puzzle")
        puzzle_html = """
        <style>
            table { border-collapse: collapse; }
            td { border: 1px solid black; width: 30px; height: 30px; text-align: center; position: relative; }
            td.black { background-color: black; }
            .sup { font-size: 12px; position: absolute; top: 2px; right: 5px; color: grey; }
        </style>
        <table>
        """

        for row in coded_grid:
            puzzle_html += "<tr>"
            for cell in row:
                if cell == '#':
                    puzzle_html += "<td class='black'></td>"
                else:
                    letter, number = cell.split("<sup>")
                    number = number.replace("</sup>", "")
                    puzzle_html += f"<td>{letter}<span class='sup'>{number}</span></td>"
            puzzle_html += "</tr>"

        puzzle_html += "</table>"
        st.markdown(puzzle_html, unsafe_allow_html=True)

# Buttons for toggling solution
col1, col2 = st.columns(2)
with col1:
    if st.button("Show Solution"):
        st.session_state['show_solution'] = True
        st.rerun()
with col2:
    if st.button("Hide Solution"):
        st.session_state['show_solution'] = False
        st.rerun()
