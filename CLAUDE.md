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

# Generate print-ready PDF with embedded fonts.
# Both modes write to dissertation.pdf, so switch to print mode FIRST (see
# Document Modes) and rerun the 4-step build. Running this on a screen-mode
# build produces a file with no binding offset, no bleed and no crop marks.
gs -dNOPAUSE -dBATCH -sDEVICE=pdfwrite -dPDFSETTINGS=/prepress -dEmbedAllFonts=true -sOutputFile=dissertation_print.pdf -f dissertation.pdf
```

## Document Modes

Set in `dissertation.tex` line 1. Both modes write to `dissertation.pdf` and paginate
identically, because `\textwidth` and `\textheight` are pinned to the same values in
each; only the position of the text block on the sheet changes.

- Screen version (default): `\documentclass{dissertation}` - 170x240mm page, no bleed
  or crop marks, inner margin 17.0mm, outer 25.5mm.
- Print version: `\documentclass[print]{dissertation}` - 176x246mm sheet holding a
  170x240mm trim box (3mm bleed all round), crop marks on the outer edge and at top
  and bottom, 6mm binding offset giving inner 20.6mm and outer 21.9mm. Sized for
  Ipskamp Printing's 170x240mm thesis format and their 20mm margin recommendation.

Before sending to the printer: switch to `[print]`, uncomment the cover page includes
in `dissertation.tex`, rerun the 4-step build, then run the Ghostscript step. Verify
the result reports a 176x246mm page size; 170x240mm means the screen build was used.

## Repository Structure

- `dissertation.tex` - Main document entry point
- `dissertation.cls` - Document class defining layout/formatting
- `dissertation.bib` - Bibliography database (600+ references)
- `04_chapters/` - Main content chapters:
  - `Intro/`, `NeurIPS21/`, `SR23/` - Monolithic `main.tex` files
  - `CVPR25/`, `NPJR25/` - Modular structure with `sec/` subdirectories
- `fonts/` - Libertine and Inconsolata fonts
- `propositions.tex` / `propositions.cls` - Separate propositions document
