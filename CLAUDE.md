# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a LaTeX PhD dissertation on event-based robot vision. The dissertation combines research on event cameras, spiking neural networks, and autonomous flight, containing four major research chapters from published papers (NeurIPS 2021, Science Robotics 2023, CVPR 2025, npj Robotics 2025).

## Build Commands

```bash
# Standard compilation (run all 4 steps for clean build)
pdflatex dissertation
bibtex dissertation
pdflatex dissertation
pdflatex dissertation

# Compile propositions document
pdflatex propositions

# Clean temporary LaTeX files
python clean.py

# Convert PDF figures to PNG (specify DPI)
python pdf2png.py 300

# Generate print-ready PDF with embedded fonts
gs -dNOPAUSE -dBATCH -sDEVICE=pdfwrite -dPDFSETTINGS=/prepress -dEmbedAllFonts=true -sOutputFile=dissertation_print.pdf -f dissertation.pdf
```

## Document Modes

Set in `dissertation.tex` line 1:
- Screen version (default): `\documentclass{dissertation}` - optimized for on-screen reading
- Print version: `\documentclass[print]{dissertation}` - includes binding offset

## Repository Structure

- `dissertation.tex` - Main document entry point
- `dissertation.cls` - Document class defining layout/formatting
- `dissertation.bib` - Bibliography database (600+ references)
- `04_chapters/` - Main content chapters:
  - `Intro/`, `NeurIPS21/`, `SR23/` - Monolithic `main.tex` files
  - `CVPR25/`, `NPJR25/` - Modular structure with `sec/` subdirectories
- `fonts/` - Libertine and Inconsolata fonts
- `propositions.tex` / `propositions.cls` - Separate propositions document
