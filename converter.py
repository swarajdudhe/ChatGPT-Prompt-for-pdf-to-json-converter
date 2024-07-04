import fitz  # PyMuPDF
import json

# Path to the PDF file
pdf_path = 'Swaraj Dudhe Resume.pdf'

# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    document = fitz.open(pdf_path)
    text = ""
    for page_num in range(len(document)):
        page = document.load_page(page_num)
        text += page.get_text("text") + "\n"
    return text

# Function to parse the text and convert it to a dictionary
def parse_resume_text(text):
    lines = text.split("\n")
    resume_data = {}
    current_section = None

    for line in lines:
        line = line.strip()
        if line:
            if line.lower() in ['projects', 'hard skill', 'education background', 'my contact', 'certifications', 'internships', 'languages', 'extra-curricular activities']:
                current_section = line.lower().replace(' ', '_')
                resume_data[current_section] = []
            elif current_section:
                resume_data[current_section].append(line)
            else:
                resume_data['header'] = resume_data.get('header', '') + line + ' '

    # Further parsing can be done based on the structure of your PDF
    return resume_data

# Extract text from the PDF
text = extract_text_from_pdf(pdf_path)

# Parse the text to create a resume dictionary
resume_data = parse_resume_text(text)

# Convert the dictionary to a JSON object
resume_json = json.dumps(resume_data, indent=4)

# Save the JSON object to a file
with open('converter_output.json', 'w') as json_file:
    json_file.write(resume_json)

print("PDF content has been converted to JSON and saved to 'resume.json'.")
