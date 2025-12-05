# PhD Thesis: Learning Event-Based Robot Vision

This repository contains the PhD thesis dissertation of Jesse J. Hagenaars, titled "Learning Event-Based Robot Vision", defended at TU Delft.

## Building the Dissertation

This dissertation is compiled using pdfLaTeX. To build the PDF:

```bash
# Standard compilation sequence
pdflatex dissertation
bibtex dissertation
pdflatex dissertation
pdflatex dissertation
```

For the propositions document:

```bash
pdflatex propositions
```

To clean temporary LaTeX build files:

```bash
python clean.py
```

### Document Options

The dissertation class supports two main modes (configured in `dissertation.tex` line 1):

- **Screen version** (default): `\documentclass{dissertation}`
  - Optimized for on-screen reading with hyperlinks
  - No binding offset adjustment

- **Print version**: `\documentclass[print]{dissertation}`
  - Optimized for physical printing with binding offset
  - Use this when preparing the final print version

**Important**: Before sending to the printer, change to the `[print]` option and uncomment the cover page includes in `dissertation.tex`.

### Print-Ready PDF

To create a print-ready PDF with all fonts embedded (required by most publishers):

```bash
gs -dNOPAUSE -dBATCH -sDEVICE=pdfwrite -dPDFSETTINGS=/prepress -dEmbedAllFonts=true -sOutputFile=dissertation_print.pdf -f dissertation.pdf
```

## Structure

The dissertation follows a paper-based structure:

```
04_chapters/
├── Intro/          - Introduction
├── NeurIPS21/      - Self-Supervised Learning of Event-Based Optical Flow with SNNs (NeurIPS 2021)
├── SR23/           - Event-Based Vision Meets Deep Learning on Autonomous Racing (Science Robotics 2023)
├── CVPR25/         - Chapter from CVPR 2025
├── NPJR25/         - Chapter from Nature Portfolio 2025
└── Conclusion/     - Conclusion
```

Each chapter contains:
- `main.tex` - Main chapter content
- `figures/` - Chapter-specific figures and images

## Template Attribution

This dissertation uses a modified version of Moritz Beller's [improved TU Delft PhD thesis template](https://github.com/Inventitech/phd-thesis-template), which itself is based on the [official TU Delft dissertation template](https://www.tudelft.nl/en/tu-delft-corporate-design/downloads/).

### Key Template Features

The template includes several improvements over the original TU Delft house style:

- Improved page layout with proper binding offset for physical printing
- Libertine fonts for better on- and off-screen readability
- Reduced color usage to minimize printing costs
- Consistent page numbering and header styles
- Pre-configured LaTeX packages in compatible order
- Custom commands for figures, citations, and cross-references
- Support for both screen and print versions

### Original Template Credits

- **Original TU Delft template**: TU Delft (2013/07/08 v1.0)
- **Improved template**: Moritz Beller (2018/11/13 v2.0)
  - Based on commit `ff9d073` from July 2nd, 2015
  - See [Moritz Beller's thesis](https://repository.tudelft.nl/islandora/object/uuid:b2946104-2092-42bb-a1ee-3b085d110466) for an example

## Requirements

### LaTeX Distribution

A full TeX Live or MiKTeX installation is required. Key packages include:

- `libertine`, `libertinust1math` - Fonts
- `natbib` - Bibliography management
- `hyperref` - Hyperlinks and cross-references
- `tikz`, `xcolor` - Graphics
- `booktabs`, `caption`, `subcaption` - Tables and figures
- Many others (see `dissertation.cls` for full list)

### Linux (Debian/Ubuntu)

```bash
sudo apt-get install texlive texlive-fonts-extra texlive-latex-extra texlive-science
```

### macOS

Install [MacTeX](https://www.tug.org/mactex/) or BasicTeX with required packages.

### Windows

Install [MiKTeX](https://miktex.org/), which will automatically install required packages on first compilation.

## Utility Scripts

### clean.py

Removes temporary LaTeX build files (`.aux`, `.log`, `.out`, `.bbl`, etc.) recursively from all subdirectories.

### pdf2png.py

Converts specified PDF figures to PNG at a given resolution:

```bash
python pdf2png.py 300  # 300 DPI
```

Edit the script to specify which figures to convert.

## License and Usage

The dissertation content is © Jesse J. Hagenaars. The LaTeX template is based on Moritz Beller's improved template, which builds upon the original TU Delft template.

If you use this template, please:
1. Keep attribution to the original template authors
2. Consider notifying Moritz Beller (moritzbeller -AT- gmx -DOT- de) of your usage
