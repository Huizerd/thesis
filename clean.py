import os

# go through all subdirectories and files in this folder and clean temporary latex files
def clean():
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".aux") or file.endswith(".log") or file.endswith(".out") or file.endswith(".toc") or file.endswith(".gz") or file.endswith(".bbl") or file.endswith(".blg") or file.endswith(".fdb_latexmk") or file.endswith(".fls") or file.endswith(".xdv") or file.endswith(".dvi"):
                os.remove(os.path.join(root, file))
        for dir in dirs:
            if dir.endswith(".tikz"):
                os.rmdir(os.path.join(root, dir))

# main function
if __name__ == "__main__":
    clean()
    