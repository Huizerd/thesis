# write a script that uses pdftoppm to convert pdf files in a list to png files using a specified resolution
# usage: python pdf2png.py <resolution>

import os
import sys
import subprocess

# get the resolution from the command line
resolution = sys.argv[1]

# get the list of pdf files in the current directory
ch1 = [
    # "04_chapters/NeurIPS21/figures/intro.pdf",
    # "04_chapters/NeurIPS21/figures/activity_aee.pdf",
    # "04_chapters/NeurIPS21/figures/activity_flow.pdf"
]
ch2 = [
    # "04_chapters/SR23/pdf/fig1-pipeline.pdf",
    # "04_chapters/SR23/pdf/fig2-vision.pdf",
    # "04_chapters/SR23/pdf/control_fig_3d.pdf",
    # "04_chapters/SR23/pdf/fig7-merging.pdf",
    # "04_chapters/SR23/pdf/fig_vision_results.pdf",
    # "04_chapters/SR23/pdf/fig5-simnetpi-results.pdf",
    # "04_chapters/SR23/pdf/fig6-pispecial-results.pdf",
    # "04_chapters/SR23/pdf/fig9-snnspecial-results.pdf",
    # "04_chapters/SR23/pdf/fig8-snntexture-results.pdf"
]

# merge lists
pdfs = ch1 + ch2

# convert each pdf file to a png file at the specified resolution
for pdf in pdfs:
    # get the pdf file name
    pdf_name = os.path.basename(pdf)
    print(pdf_name)
    # get the png file name
    png_name = pdf_name.replace(".pdf", "")
    # convert the pdf to png
    subprocess.call(
        ["pdftoppm", "-png", "-r", resolution, pdf, png_name]
    )
    subprocess.call(
        ["mv", png_name + "-1.png", png_name + ".png"]
    )
    # move them to the same folder as the pdf
    subprocess.call(["mv", png_name + ".png", os.path.dirname(pdf)])
