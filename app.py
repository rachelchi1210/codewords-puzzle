import streamlit as st
from codewords_puzzle_gen import generate_codewords_puzzle
from io import BytesIO
import pandas as pd
import matplotlib.pyplot as plt

st.title("Codeword Maker")

# Session state initialization
if 'puzzle_generated' not in st.session_state:
    st.session_state['puzzle_generated'] = False
if 'coded_grid' not in st.session_state:
    st.session_state['coded_grid'] = None
if 'solution_grid' not in st.session_state:
    st.session_state['solution_grid'] = None
if 'letter_to_number' not in st.session_state:
    st.session_state['letter_to_number'] = None
if 'placed_words' not in st.session_state:
    st.session_state['placed_words'] = []
if 'show_solution' not in st.session_state:
    st.session_state['show_solution'] = False
if 'current_grid_size' not in st.session_state:
    st.session_state['current_grid_size'] = 10
if 'current_word_input' not in st.session_state:
    st.session_state['current_word_input'] = ""

# Input for grid size and words
grid_size = st.number_input("Grid Size (6-30):", min_value=6, max_value=30, value=st.session_state['current_grid_size'])
word_input = st.text_area("Enter words (comma separated):", value=st.session_state['current_word_input'])

# Buttons for generating puzzle
if st.button("Generate Puzzle"):
    word_list = [word.strip().upper() for word in word_input.split(",") if word.strip()]
    coded_grid, solution_grid, letter_to_number, placed_words = generate_codewords_puzzle(word_list, grid_size)
    st.session_state['coded_grid'] = coded_grid
    st.session_state['solution_grid'] = solution_grid
    st.session_state['letter_to_number'] = letter_to_number
    st.session_state['placed_words'] = placed_words
    st.session_state['puzzle_generated'] = True
    st.session_state['current_grid_size'] = grid_size
    st.session_state['current_word_input'] = word_input

col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("Placed Words")
    st.write(st.session_state['placed_words'])

with col2:
    st.subheader("Generated Puzzle")
    if st.session_state['coded_grid']:
        fig, ax = plt.subplots()
        ax.axis('off')
        table_data = st.session_state['coded_grid']
        table = ax.table(cellText=table_data, loc='center', cellLoc='center')
        plt.savefig("puzzle.png")
        st.pyplot(fig)

        # Export to PNG button
        buf = BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        st.download_button("Download as PNG", buf, file_name="puzzle.png", mime="image/png")

        # Export to PDF button
        pdf_buffer = BytesIO()
        df = pd.DataFrame(table_data)
        df.to_csv(pdf_buffer, index=False)
        pdf_buffer.seek(0)
        st.download_button("Download as PDF", pdf_buffer, file_name="puzzle.pdf", mime="application/pdf")

# Buttons for toggling solution visibility
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Show Solution"):
        st.session_state['show_solution'] = True
        st.rerun()
with col2:
    if st.button("Hide Solution"):
        st.session_state['show_solution'] = False
        st.rerun()
with col3:
    if st.button("Reset"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()
