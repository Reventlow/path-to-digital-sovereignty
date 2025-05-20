#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
convert.py - Converts Markdown files to a LaTeX-compiled PDF document
This script takes all the Markdown files from the parent directory and 
compiles them into a single PDF using LaTeX.
"""

import os
import subprocess
import shutil
from pathlib import Path
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('LatexConverter')

# File order and structure
FILE_ORDER = [
    '../README.md',
    '../faser-i-beredskabsplanen.md',
    '../fase-1-observation-og-forberedende-overvågning.md',
    '../fase-2-planlægningsfase.md',
    '../fase-3-blød-overgang.md',
    '../fase-4-akut-overgang.md',
    '../fase-5-systemfejl-og-nødprocedurer.md',
    '../faseovergang-og-eskalationskriterier.md',
    '../LICENSE.md'
]

# LaTeX output filenames
OUTPUT_DIR = 'output'
TEX_FILE = os.path.join(OUTPUT_DIR, 'beredskabsplan.tex')
PDF_FILE = os.path.join(OUTPUT_DIR, 'beredskabsplan.pdf')
TEMP_DIR = os.path.join(OUTPUT_DIR, 'temp')

# LaTeX template with Danish language support
LATEX_TEMPLATE = 'template.tex'

def ensure_directories():
    """Create output directories if they don't exist"""
    Path(OUTPUT_DIR).mkdir(exist_ok=True)
    Path(TEMP_DIR).mkdir(exist_ok=True)
    logger.info(f"Created output directories: {OUTPUT_DIR}, {TEMP_DIR}")

def remove_navigation_text(text):
    """
    Remove navigation text links from a markdown string.

    The function looks for patterns like:
    | [« Oversigt](faser-i-beredskabsplanen.md) | [Næste: Fase 2 »](fase-2-planlægningsfase.md) |
    |:------------------------------------------|----------------------------------------------:|

    Args:
        text (str): The input text to filter

    Returns:
        str: Text with navigation elements removed
    """
    import re

    # Pattern for navigation table with links
    # This pattern matches markdown table rows containing navigation links
    nav_pattern = r'\|\s*\[.*?\]\(.*?\)\s*\|\s*\[.*?\]\(.*?\)\s*\|\s*\n\|[\s:\-]*\|[\s:\-]*\|'

    # Remove the navigation text
    filtered_text = re.sub(nav_pattern, '', text)

    return filtered_text

def convert_markdown_to_latex(markdown_content, output_file=None):
    """Convert markdown to LaTeX using Pandoc

    Args:
        markdown_content (str): The markdown content to convert
        output_file (str, optional): Path to save the output LaTeX file.
            If None, returns the LaTeX content as a string.

    Returns:
        Union[bool, str]: If output_file is provided, returns True on success.
            Otherwise returns the LaTeX content as a string.
    """
    # Remove navigation headers and footers
    markdown_content = remove_navigation_text(markdown_content)
    
    # Write content to a temporary file
    with open('temp_input.md', 'w', encoding='utf-8') as f:
        f.write(markdown_content)

    try:
        # Run pandoc to convert
        cmd = [
            'pandoc',
            '-f',
            'markdown',
            '-t',
            'latex',
            'temp_input.md',
            '--top-level-division=chapter'
        ]

        if output_file:
            cmd.extend(['-o', output_file])
            subprocess.run(cmd, check=True)
            result = True
        else:
            result = subprocess.run(cmd, check=True, capture_output=True, text=True)
            result = result.stdout
    finally:
        # Clean up temporary file
        if os.path.exists('temp_input.md'):
            os.remove('temp_input.md')

    return result

def convert_md_to_tex():
    """Convert Markdown files to LaTeX content"""
    logger.info("Starting Markdown to LaTeX conversion")

    chapters = []

    # Read the template
    with open(LATEX_TEMPLATE, 'r', encoding='utf-8') as f:
        template = f.read()

    # Process each file in order
    for i, filepath in enumerate(FILE_ORDER):
        try:
            if not os.path.exists(filepath):
                logger.warning(f"File not found: {filepath} - skipping")
                continue

            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            if i == 0:
                import re
                content = re.sub(
                    r"^#\s+.*",
                    "# Introduktion",
                    content,
                    count=1,
                    flags=re.MULTILINE)

                content = re.sub(r"!\[.*?\]\(.*?\)", "", content)

                split_marker = "## 📚 Indholdsfortegnelse"
                if split_marker in content:
                    content = content.split(split_marker)[0].strip()

            latex_content = convert_markdown_to_latex(content)

            chapters.append(latex_content)
            logger.info(f"Processed {filepath}")

        except Exception as e:
            logger.error(f"Error processing {filepath}: {str(e)}")

    # Combine all chapters
    document_content = '\n\\newpage\n\n'.join(chapters)

    # Insert content into template
    latex_document = template.replace('{{CONTENT}}', document_content)

    # Write the combined LaTeX file
    with open(TEX_FILE, 'w', encoding='utf-8') as f:
        f.write(latex_document)

    logger.info(f"LaTeX document written to {TEX_FILE}")
    return TEX_FILE

def compile_latex_to_pdf(tex_file):
    """Compile the LaTeX file to PDF using pdflatex (more commonly available than xelatex)"""
    logger.info("Compiling LaTeX to PDF...")

    try:
        # First try pdflatex (more commonly available)
        latex_cmd = 'pdflatex'
        
        # Check if pdflatex is available
        try:
            subprocess.run(['which', latex_cmd], check=True, capture_output=True)
        except subprocess.CalledProcessError:
            # If pdflatex is not available, try xelatex
            latex_cmd = 'xelatex'
            try:
                subprocess.run(['which', latex_cmd], check=True, capture_output=True)
            except subprocess.CalledProcessError:
                # If neither is available, try lualatex
                latex_cmd = 'lualatex'
                try:
                    subprocess.run(['which', latex_cmd], check=True, capture_output=True)
                except subprocess.CalledProcessError:
                    logger.error("No LaTeX compiler (pdflatex, xelatex, or lualatex) found")
                    return False

        logger.info(f"Using {latex_cmd} compiler")

        # Run LaTeX compiler twice to resolve references
        for i in range(2):
            process = subprocess.run(
                [latex_cmd, '-interaction=nonstopmode', '-output-directory=' + OUTPUT_DIR, tex_file],
                capture_output=True,
                text=True,
                check=False
            )

            if process.returncode != 0:
                logger.error(f"LaTeX compilation error: {process.stderr}")
                with open(os.path.join(OUTPUT_DIR, 'compile_error.log'), 'w', encoding='utf-8') as f:
                    f.write(process.stderr)
                return False

        # Generate table of contents with hyperrefs
        subprocess.run(
            [latex_cmd, '-interaction=nonstopmode', '-output-directory=' + OUTPUT_DIR, tex_file],
            capture_output=True,
            check=False
        )

        logger.info(f"PDF successfully generated at {PDF_FILE}")
        return True

    except Exception as e:
        logger.error(f"Error during PDF compilation: {str(e)}")
        return False

def main():
    """Main function to convert Markdown to PDF"""
    logger.info("Starting conversion process")

    ensure_directories()
    tex_file = convert_md_to_tex()

    if compile_latex_to_pdf(tex_file):
        logger.info("Conversion completed successfully!")
    else:
        logger.error("PDF compilation failed")

    # Copy PDF to parent directory for easier access
    pdf_path = os.path.join(OUTPUT_DIR, 'beredskabsplan.pdf')
    if os.path.exists(pdf_path):
        shutil.copy2(pdf_path, '../beredskabsplan.pdf')
        logger.info("PDF copied to repository root")
    else:
        logger.error(f"PDF file not found at {pdf_path}")

if __name__ == "__main__":
    main()
