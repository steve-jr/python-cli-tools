import os
import sys
from pypdf import PdfWriter


def merge_pdfs(paths, output):
    merger = PdfWriter()

    for path in paths:
        absolute_path = os.path.abspath(path)

        # Check if the path is a file
        if os.path.isfile(absolute_path):
            merger.append(absolute_path)
        else:
            print(f"Error: {path} is not a file.")
            sys.exit(1)

    merger.write(output)
    merger.close()


if __name__ == '__main__':

    if len(sys.argv) < 4:
        print("Usage: python merge_pdfs.py output.pdf input1.pdf input2.pdf ...")
        sys.exit(1)

    output_path = sys.argv[1]
    input_paths = sys.argv[2:]

    # Check if the output path is a directory
    if os.path.isdir(output_path):
        output_path += '/output.pdf'

    merge_pdfs(input_paths, output_path)

    print(f'Merged {len(input_paths)} documents into {output_path}')
