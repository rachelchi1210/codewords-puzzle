import streamlit as st
from codewords_puzzle_gen import get_random_words

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
if 'show_solution' not in st.session_state:
    st.session_state['show_solution'] = False
if 'current_grid_size' not in st.session_state:
    st.session_state['current_grid_size'] = 10
if 'current_word_input' not in st.session_state:
    st.session_state['current_word_input'] = ""
if 'word_count' not in st.session_state:
    st.session_state['word_count'] = 10

# Input for number of words and grid size
word_count = st.number_input("Number of Words:", min_value=1, max_value=100, value=st.session_state['word_count'])
grid_size = st.number_input("Grid Size (6-20):", min_value=6, max_value=20, value=st.session_state['current_grid_size'])

# Button to generate random words
if st.button("Generate Random Words"):
    try:
        # Get the exact number of words
        selected_count = int(word_count)

        # Fetch the required number of words
        selected_words = get_random_words(selected_count)

        # Store the exact number of words
        st.session_state['current_word_input'] = ", ".join(selected_words)

        # Debugging output
        st.write(f"Generated {len(selected_words)} words (debug)")
    except Exception as e:
        st.error(f"Error generating words: {str(e)}")

    st.rerun()

# Text area to display selected words
st.subheader("Enter words (comma separated):")
st.text_area("Enter words:", value=st.session_state['current_word_input'], height=100)

# Buttons for generating and resetting the puzzle
if st.button("Generate Puzzle"):
    st.session_state['puzzle_generated'] = True
    st.session_state['current_grid_size'] = grid_size

if st.button("Reset"):
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.rerun()

# Word List Display
st.subheader("Word List")
if 'current_word_input' in st.session_state and st.session_state['current_word_input']:
    st.write(st.session_state['current_word_input'])
    st.write(f"Word count (debug): {len(st.session_state['current_word_input'].split(', '))} words generated")

# Display puzzle with solution toggle buttons
if st.session_state['puzzle_generated']:
    col1, col2 = st.columns(2)

    with col1:
        if st.button("Show Solution"):
            st.session_state['show_solution'] = True
            st.rerun()
    with col2:
        if st.button("Hide Solution"):
            st.session_state['show_solution'] = False
            st.rerun()

    # Placeholder for grid visualization (mock-up)
    if st.session_state['show_solution']:
        st.write("Puzzle with solution shown here.")
    else:
        st.write("Puzzle without solution shown here.")

