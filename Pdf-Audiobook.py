import pyttsx3
import PyPDF2

def pdf_to_audio(pdf_path, output_path):
    # Initialize the text to speech engine
    engine = pyttsx3.init()

    # Open the PDF file
    pdf_file = open(pdf_path, 'rb')

    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfReader("C:/Users/kudali vasuki/OneDrive/Desktop/python/CSP.pdf")

    # Get total number of pages in the PDF
    num_pages = len(pdf_reader.pages)

    # Read and convert each page to audio
    for page_number in range(num_pages):
        page = pdf_reader.pages[page_number]
        text = page.extract_text()
        
        # Add text to speech engine
        engine.say(text)

    # Save the audio to file
    engine.save_to_file(text, output_path)

    # Run the engine
    engine.runAndWait()

    # Close the PDF file
    pdf_file.close()

# Example usage
pdf_path = 'CSP.pdf'  # Replace with your PDF file path
output_path = 'output.mp3' # Replace with desired output file path
pdf_to_audio("C:/Users/kudali vasuki/OneDrive/Desktop/python/CSP.pdf", output_path)