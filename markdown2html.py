#!/usr/bin/python3

"""Markdown to HTML"""

import sys
import os

def parse_heading(line):
    count = 0
    while line[count] == '#':
        count += 1
    return count

def parse_unordered_list(line):
    count = 0
    while line[count] == '-':
        count += 1
    return count

def convert_markdown_to_html(input_file, output_file):
    if not os.path.exists(input_file):
        sys.stderr.write(f"Missing {input_file}\n")
        sys.exit(1)

    with open(input_file, 'r') as md_file:
        markdown_lines = md_file.readlines()

    html_lines = []
    in_list = False

    for line in markdown_lines:
        line = line.strip()

        if line.startswith('#'):
            heading_level = parse_heading(line)
            html_line = f"<h{heading_level}>{line[heading_level+1:]}</h{heading_level}>"
            html_lines.append(html_line)

        elif line.startswith('-'):
            if not in_list:
                html_lines.append("<ul>")
                in_list = True
            list_level = parse_unordered_list(line)
            html_line = f"<li>{line[list_level+1:]}</li>"
            html_lines.append(html_line)
        else:
            if in_list:
                html_lines.append("</ul>")
                in_list = False
            html_lines.append(line)
    if in_list:
        html_lines.append("</ul>")

    with open(output_file, 'w') as html_file:
        html_file.write('\n'.join(html_lines))

if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    convert_markdown_to_html(input_file, output_file)
    sys.exit(0)
