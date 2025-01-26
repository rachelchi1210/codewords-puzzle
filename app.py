import streamlit as st
from codewords_puzzle_gen import generate_codewords_puzzle
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import base64
from PIL import Image, ImageDraw, ImageFont

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

        # Export to PNG
        def export_to_png():
            img = Image.new('RGB', (grid_size * 50, grid_size * 50), color='white')
            draw = ImageDraw.Draw(img)
            font = ImageFont.load_default()
            for r, row in enumerate(st.session_state['coded_grid']):
                for c, cell in enumerate(row):
                    text = cell.replace("<sup>", "").replace("</sup>", "")
                    draw.text((c * 50 + 15, r * 50 + 15), text, font=font, fill='black')
            img.save("puzzle.png")
            return "puzzle.png"

        if st.button("Download as PNG"):
            png_path = export_to_png()
            with open(png_path, "rb") as file:
                btn = st.download_button(
                    label="Download PNG",
                    data=file,
                    file_name="puzzle.png",
                    mime="image/png"
                )

        # Export to PDF
        def export_to_pdf():
            buffer = BytesIO()
            c = canvas.Canvas(buffer, pagesize=letter)
            for r, row in enumerate(st.session_state['coded_grid']):
                for c_idx, cell in enumerate(row):
                    text = cell.replace("<sup>", "").replace("</sup>", "")
                    c.drawString(c_idx * 50 + 50, 750 - r * 50, text)
            c.save()
            buffer.seek(0)
            return buffer

        pdf_buffer = export_to_pdf()
        st.download_button(
            "Download as PDF", pdf_buffer, file_name="puzzle.pdf", mime="application/pdf"
        )

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
