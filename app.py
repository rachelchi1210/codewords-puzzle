with col2:
    st.subheader("Generated Puzzle")
    puzzle_html = """
    <style>
        td { border: 1px solid black; width: 30px; height: 30px; text-align: center; font-size: 20px; position: relative; }
        td.black { background-color: black; }
        .sup { font-size: 12px; position: absolute; top: 2px; right: 5px; color: grey; }
    </style>
    <table border='1' style='border-collapse: collapse;'>
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

