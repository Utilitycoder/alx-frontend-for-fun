#!/usr/bin/python3

"""Markdown to HTML"""

import sys
import os

def parse_heading(line):
    count = 0
    while line[count] == '#':
        count += 1
    return count

def convert_markdown_to_html(input_file, output_file):
    if not os.path.exists(input_file):
        sys.stderr.write(f"Missing {input_file}\n")
        sys.exit(1)

    with open(input_file, 'r') as md_file:
        markdown_lines = md_file.readlines()

    html_lines = []
    for line in markdown_lines:
        line = line.strip()
        if line.startswith('#'):
            heading_level = parse_heading(line)
            html_line = f"<h{heading_level}>{line[heading_level+1:]}</h{heading_level}>"
            html_lines.append(html_line)
        else:
            html_lines.append(line)

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
