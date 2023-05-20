from PyPDF2 import PdfMerger
import os

def merge_pdfs(input_dir, output_path):
    merger = PdfMerger()

    # Retrieve all PDF files in the input directory
    pdf_files = [file for file in os.listdir(input_dir) if file.endswith(".pdf")]
    pdf_files.sort()  # Sort the files alphabetically

    # Merge each PDF file into the merger object
    for pdf_file in pdf_files:
        file_path = os.path.join(input_dir, pdf_file)
        merger.append(file_path)

    # Write the merged PDF to the output path
    merger.write(output_path)
    merger.close()

    print(f"Merged PDFs saved to: {output_path}")

# Directory paths
input_directory = "ppt_files"
output_path = "merged.pdf"

# Call the merge_pdfs function
merge_pdfs(input_directory, output_path)
