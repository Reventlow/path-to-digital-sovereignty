#!/bin/bash
# Installation script for LaTeX converter dependencies

echo "Setting up LaTeX converter environment..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Python 3 is required but not installed. Please install Python 3 first."
    exit 1
fi

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "pip3 is required but not installed. Please install pip3 first."
    exit 1
fi

# Check if LaTeX is installed
if ! command -v xelatex &> /dev/null; then
    echo "XeLaTeX is required but not installed."
    echo "On Ubuntu/Debian: sudo apt-get install texlive-xetex texlive-fonts-recommended texlive-lang-european"
    echo "On macOS with Homebrew: brew install --cask mactex"
    echo "On Windows: Install MiKTeX or TeX Live"
    exit 1
fi

# Check if Pandoc is installed
if ! command -v pandoc &> /dev/null; then
    echo "Pandoc is required but not installed."
    echo "On Ubuntu/Debian: sudo apt-get install pandoc"
    echo "On macOS with Homebrew: brew install pandoc"
    echo "On Windows: Install from https://pandoc.org/installing.html"
    exit 1
fi

# Install Python dependencies
echo "Installing Python dependencies..."
pip3 install -r requirements.txt

echo "Setup complete! You can now run ./convert.py to generate the PDF."