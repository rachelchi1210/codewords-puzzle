with col2:
    st.subheader("Generated Puzzle")
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

    for row in coded_grid:
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
