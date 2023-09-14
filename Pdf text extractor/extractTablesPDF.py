pdf_path = "path_to_your_pdf"

import PyPDF2

def extract_text_from_pdf(pdf_path):
    try:
        # Open the PDF file in binary mode
        with open(pdf_path, 'rb') as pdf_file:
            # Create a PDF reader object
            pdf_reader = PyPDF2.PdfReader(pdf_file)

            # Initialize an empty string to store the extracted text
            extracted_text = ""

            # Iterate through each page in the PDF
            for page_num in range(len(pdf_reader.pages)):
                # Extract the text from the current page
                page = pdf_reader.pages[page_num]
                extracted_text += page.extract_text()

            return extracted_text
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Usage example
extracted_text = extract_text_from_pdf(pdf_path)

if extracted_text:
    print(extracted_text)
else:
    print("No text extracted from the PDF.")
