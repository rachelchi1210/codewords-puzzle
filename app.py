import streamlit as st
from codewords_puzzle_gen import generate_codewords_puzzle
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import pandas as pd

st.title("KDP A-Z Codeword Maker")

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

# Generate puzzle when button is clicked
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
        puzzle_html = """
        <style>
            table { border-collapse: collapse; }
            td { 
                border: 1px solid black; 
                width: 40px; 
                height: 40px; 
                text-align: center; 
                position: relative; 
                font-size: 20px;
            }
            td.black { background-color: black; }
            .sup { 
                font-size: 12px; 
                position: absolute; 
                top: 2px; 
                right: 5px; 
                color: grey; 
            }
            .hidden { color: transparent; }
        </style>
        <table>
        """

        for row in st.session_state['coded_grid']:
            puzzle_html += "<tr>"
            for cell in row:
                if cell == '#':
                    puzzle_html += "<td class='black'></td>"
                else:
                    letter = cell.split("<sup>")[0]
                    number = cell.split("<sup>")[1].replace("</sup>", "")
                    letter_class = "hidden" if not st.session_state['show_solution'] else ""
                    puzzle_html += f"<td><span class='sup'>{number}</span><span class='{letter_class}'>{letter}</span></td>"
            puzzle_html += "</tr>"

        puzzle_html += "</table>"
        st.markdown(puzzle_html, unsafe_allow_html=True)

        # Export puzzle as PNG
        def create_puzzle_image(grid):
            cell_size = 50
            img_width = len(grid[0]) * cell_size
            img_height = len(grid) * cell_size

            img = Image.new("RGB", (img_width, img_height), "white")
            draw = ImageDraw.Draw(img)

            font = ImageFont.load_default()

            for row_index, row in enumerate(grid):
                for col_index, cell in enumerate(row):
                    x0 = col_index * cell_size
                    y0 = row_index * cell_size
                    x1 = x0 + cell_size
                    y1 = y0 + cell_size
                    draw.rectangle([x0, y0, x1, y1], outline="black")
                    if cell != "#":
                        draw.text((x0 + 15, y0 + 10), cell, fill="black", font=font)

            return img

        img = create_puzzle_image(st.session_state['coded_grid'])
        buf = BytesIO()
        img.save(buf, format="PNG")
        st.download_button("Download as PNG", buf.getvalue(), file_name="puzzle.png", mime="image/png")

        # Export puzzle as PDF
        def create_pdf(grid):
            pdf_buffer = BytesIO()
            df = pd.DataFrame(grid)
            df.to_csv(pdf_buffer, index=False)
            pdf_buffer.seek(0)
            return pdf_buffer

        pdf_file = create_pdf(st.session_state['coded_grid'])
        st.download_button("Download as PDF", pdf_file, file_name="puzzle.pdf", mime="application/pdf")

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
