with col2:
    st.subheader("Generated Puzzle")
    puzzle_html = "<style>td.black { background-color: black; width: 30px; height: 30px; }</style>"
    puzzle_html += "<table border='1' style='border-collapse: collapse; width:100%; text-align:center;'>"
    
    for row in display_grid:
        puzzle_html += "<tr>"
        for cell in row:
            if cell == '█':  # Replace solid black character with CSS class
                puzzle_html += "<td class='black'></td>"
            else:
                puzzle_html += f"<td style='padding:15px; font-size:20px;'>{cell}</td>"
        puzzle_html += "</tr>"
    
    puzzle_html += "</table>"
    st.markdown(puzzle_html, unsafe_allow_html=True)
