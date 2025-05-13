# LaTeX Converter for Emergency Preparedness Plan

This directory contains the LaTeX converter that compiles all the Markdown documents from the main repository into a comprehensive, professional PDF document.

## Contents
- `convert.py` - The main Python script that converts Markdown to LaTeX and generates the PDF
- `template.tex` - The LaTeX template file used for styling the document
- `requirements.txt` - Python dependencies needed to run the converter

## How to Use

1. Make sure you have Python 3.6+ and LaTeX installed on your system
2. Install dependencies: `pip install -r requirements.txt`
3. Run the converter: `python convert.py`
4. The compiled PDF will be created as `beredskabsplan.pdf`

## Dependencies

- Python 3.6+
- LaTeX (TeX Live or MiKTeX)
- Pandoc (for better Markdown to LaTeX conversion)