# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a PhD thesis dissertation using a modified TU Delft dissertation template (based on Moritz Beller's improved template). The thesis titled "Learning Event-Based Robot Vision" focuses on event-based optical flow and spiking neural networks (SNNs). It's compiled using pdfLaTeX with Libertine fonts and follows TU Delft's PhD dissertation formatting requirements.

## Build System

### Primary Build Commands

```bash
# Standard compilation sequence
pdflatex dissertation
bibtex dissertation
pdflatex dissertation
pdflatex dissertation

# Build propositions document
pdflatex propositions

# Clean temporary LaTeX files
python clean.py
```

### Build Process Details

- **Main compilation**: Uses `pdflatex` (not XeLaTeX) with native fonts
- **Bibliography**: Requires separate `bibtex dissertation` run between pdflatex passes
- **Multi-pass compilation**: Standard LaTeX workflow (pdflatex → bibtex → pdflatex → pdflatex) to resolve all references
- **Font system**: Uses Libertine fonts (libertine package) with T1 encoding, compatible with pdflatex

### Document Class Options

The dissertation class supports three modes (set in `dissertation.tex` line 1-3):
- Default: `\documentclass{dissertation}` - Screen version with hyperlinks
- Print: `\documentclass[print]{dissertation}` - Print version with binding offset
- Draft: `\documentclass[print,draft]{dissertation}` - Print with draft mode

**IMPORTANT**: Before sending to printer, change line 1 to use the `[print]` option.

## Repository Structure

```
thesis/
├── dissertation.tex          # Main document (includes all chapters)
├── propositions.tex          # Propositions document
├── dissertation.cls          # Custom TU Delft dissertation class
├── propositions.cls          # Custom propositions class
├── dissertation.bib          # All bibliography references
├── clean.py                  # Script to clean temporary LaTeX files
├── pdf2png.py                # Script to convert PDFs to PNG
├── fonts/                    # Font files (for XeLaTeX only, not used with pdflatex)
│   ├── libertinus/          # Serif, sans, and math fonts
│   └── inconsolata/         # Monospace font
├── 01_title/                # Title page
├── 02_summary/              # Summary/abstract
├── 03_acronyms/             # Acronyms list
├── 04_chapters/             # All thesis chapters
│   ├── Intro/               # Introduction chapter
│   ├── NeurIPS21/           # Chapter 2 (NeurIPS 2021 paper)
│   ├── SR23/                # Chapter 3 (Science Robotics 2023)
│   ├── CVPR25/              # Chapter 4 (CVPR 2025)
│   ├── NPJR25/              # Chapter 5 (Nature Portfolio 2025)
│   └── Conclusion/          # Conclusion chapter
├── 05_references/           # Bibliography section
├── 06_acks/                 # Acknowledgments
├── 07_cv/                   # Curriculum Vitae
└── 08_publications/         # Publications list
```

### Chapter Structure

Each chapter in `04_chapters/` contains:
- `main.tex` - Main chapter content
- `figures/` or similar - Chapter-specific figures and images

Chapters are named after their publication venues (NeurIPS21, SR23, CVPR25, NPJR25), indicating this is a paper-based dissertation.

## Architecture & Design

### Compilation Pipeline

1. **pdfLaTeX** is the primary compiler (with nativefonts mode)
2. **BibTeX** is used for bibliography processing between pdflatex passes
3. Multi-pass compilation resolves cross-references, citations, and TOC
4. The dissertation class (`dissertation.cls`) extends the standard `book` class and uses Libertine fonts via LaTeX packages

### Font System

- **Serif (main text)**: Libertine (via libertine package from CTAN)
- **Math**: Libertinus T1 Math (via libertinust1math package from CTAN)
- **T1 font encoding**: Ensures proper font handling with pdflatex
- Fonts are included via standard LaTeX packages, no system font installation required
- Note: The `fonts/` directory contains font files for XeLaTeX compilation, but these are NOT used when compiling with pdflatex

### Custom LaTeX Features

The dissertation.tex defines several custom reference commands:
- `\chapref{label}` - Chapter references
- `\secref{label}` - Section references
- `\figref{label}` - Figure references
- `\tabref{label}` - Table references
- Variants for multiple references: `\figreftwo`, `\figrefthree`, etc.

### Color and Print Considerations

- TU Delft blue (`tudelft-cyan`, `tudelft-orange`) used for highlights
- Hyperlinks are colored orange in screen version
- Print version includes binding offset and different formatting
- The template reduces color usage to minimize printing costs

## Utility Scripts

### clean.py
Recursively removes temporary LaTeX build artifacts:
- `.aux`, `.log`, `.out`, `.toc`, `.gz`, `.bbl`, `.blg`
- `.fdb_latexmk`, `.fls`, `.xdv`, `.dvi`
- `.tikz` directories

### pdf2png.py
Converts specific PDF figures to PNG at specified resolution:
```bash
python pdf2png.py <resolution>
```
Uses `pdftoppm` to convert figures. Edit the `ch1` and `ch2` lists in the script to specify which PDFs to convert.

## Important Build Considerations

1. **Compiler**: Uses pdfLaTeX with native fonts (libertine package), not XeLaTeX
2. **Multiple Passes**: Always run the full sequence (pdflatex → bibtex → pdflatex → pdflatex) for complete document
3. **Compilation Time**: Full builds can be slow due to large number of figures and multiple compilation passes
4. **Print vs Screen**: Remember to uncomment cover pages and change document class option for final print version
5. **Bibliography Management**: Uses natbib with numerical citations, sorted and compressed

## Common Workflows

### Adding a New Figure
1. Place the figure file in the appropriate chapter's subdirectory
2. Reference with full path: `\includegraphics{04_chapters/ChapterName/figures/filename.pdf}`
3. Use `\figref{fig:label}` for cross-references

### Modifying Chapter Content
1. Navigate to `04_chapters/<ChapterName>/main.tex`
2. Edit the LaTeX content
3. Rebuild with the pdflatex → bibtex → pdflatex → pdflatex sequence
4. Main dissertation includes chapters via `\include` commands in `dissertation.tex:94-99`

### Final Print Preparation
1. Change `dissertation.tex` line 1 to `\documentclass[print]{dissertation}`
2. Uncomment cover page includes (lines 78, 121-122 in dissertation.tex)
3. Run full compilation sequence (pdflatex → bibtex → pdflatex → pdflatex)
4. Optionally use Ghostscript to embed all fonts: `gs -dNOPAUSE -dBATCH -sDEVICE=pdfwrite -dPDFSETTINGS=/prepress -dEmbedAllFonts=true -sOutputFile=dissertation_print.pdf -f dissertation.pdf`

## Dependencies

Required LaTeX packages (auto-installed with full TeX distribution):
- pdfLaTeX compiler
- libertine, libertinust1math (fonts)
- fontenc, inputenc (font encoding)
- natbib (bibliography)
- hyperref (hyperlinks)
- tikz, xcolor (graphics)
- booktabs, caption, subcaption (tables and figures)
- acronym (acronym list)
- Many others defined in dissertation.cls

External tools:
- `bibtex` - Bibliography processing
- `gs` (Ghostscript) - Font embedding for print version (optional)
- `pdftoppm` - PDF to PNG conversion (optional, for pdf2png.py)
