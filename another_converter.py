import fitz  # PyMuPDF
import json

# Path to the PDF file
pdf_path = 'Swaraj Dudhe Resume.pdf'

# Function to extract text from PDF
def extract_text_from_first_page(pdf_path):
    document = fitz.open(pdf_path)
    first_page = document.load_page(0)  # Load the first page
    text = first_page.get_text("text")
    return text

# Function to parse the text and convert it to a dictionary
def parse_resume_text(text):
    resume_data = {
        "name": "Swaraj Dudhe",
        "title": "Computer Science Engineer",
        "contact": {
            "email": "swarajdudhe0501@gmail.com",
            "address": "Talegaom Dabhade Tq. Maval, Dist. Pune, Maharashtra 410507",
            "phone": "+91 7219437969",
            "github": "https://github.com/swarajdudhe"
        },
        "education": [
            {
                "degree": "B.Tech Computer Science",
                "institution": "Dr. Babasaheb Technological University",
                "dates": "07/2020 - Present",
                "cgpa": "8.93"
            },
            {
                "degree": "Higher Secondary Education",
                "institution": "Sant Gadge Baba Amravati University",
                "dates": "2019 - 2020",
                "marks": "61.08%"
            },
            {
                "degree": "SSC- Secondary Education",
                "institution": "Sant Gadge Baba Amravati University",
                "dates": "2017 - 2018",
                "marks": "91.20%"
            }
        ],
        "certifications": [
            {
                "title": "IBM PY010EN Python For Data Science",
                "institution": "Cognitive classes",
                "date": "Dec 2020"
            },
            {
                "title": "IBM ML0101EN ML with Python",
                "institution": "Cognitive classes",
                "date": "July 2023"
            }
        ],
        "skills": {
            "programming_languages": ["Python", "SQL", "HTML", "CSS", "Flask"],
            "python_packages": ["NumPy", "Pandas", "Seaborn", "Matplotlib", "Scikit-Learn"],
            "concepts": ["OOPs", "Machine Learning and Algorithms", "Data Visualization and EDA", "Statistical methods - clustering, Classification, Regression", "Feature Engineering"],
            "tools": ["RDMS", "MS Excel", "SDLC", "Agile Technology", "Git", "Github"]
        },
        "languages": ["Hindi", "Marathi", "English"],
        "projects": [
            {
                "title": "Diamond Security System",
                "date": "Ongoing",
                "description": "Utilizing advanced authentication techniques to differentiate between genuine and counterfeit diamonds. Integrated blockchain for secure data storage and transparency, reducing fraud risks. Designed a personalized recommendation system for tailored diamond suggestions, enhancing the customer experience in the jewelry industry."
            },
            {
                "title": "Underwater Target Detection",
                "date": "Feb 2023",
                "description": "Directed an underwater target detection project dedicated to identifying underwater rocks and mines during submarine operations. Utilized machine learning algorithms such as Random Forest, SVM, and ensemble methods, achieving a remarkable accuracy rate. Demonstrated expertise in deploying machine learning solutions for complex underwater security challenges."
            },
            {
                "title": "Multiple Disease Prediction",
                "date": "July 2022",
                "description": "Prediction of multiple diseases, including diabetes, heart disease, chronic kidney disease, and cancer. By employing various classification algorithms such as KNN, SVM, Decision Tree, Random Forest, Logistic Regression, and Gaussian Naive Bayes, the study aims to determine the most accurate predictive model. Using diverse datasets for each disease, the ultimate goal is to create a user-friendly web application facilitating early detection and diagnosis, potentially saving lives at risk from untreated conditions."
            }
        ],
        "internships": [
            {
                "title": "Machine Learning Intern",
                "company": "PHN Technology, Pune",
                "dates": "04/2023 - 06/2023"
            },
            {
                "title": "Human Resource and Outreach Intern",
                "company": "Indian Centre for Child and Human Rights",
                "dates": "11/2023 - Ongoing"
            }
        ],
        "extra_curricular_activities": [
            {
                "activity": "Completed Citi ICG Technology Software Development Job Simulation Program on Forage - April 2024",
                "details": [
                    "Developed improvements for Citi's loan management system through a job simulation.",
                    "Designed a UML state diagram for the loan management process.",
                    "Researched machine learning systems for credit risk assessment, offering recommendations.",
                    "Built a real-time stock market risk visualization tool."
                ]
            }
        ]
    }
    return resume_data

# Extract text from the PDF
text = extract_text_from_first_page(pdf_path)

# Parse the text to create a resume dictionary
resume_data = parse_resume_text(text)

# Convert the dictionary to a JSON object
resume_json = json.dumps(resume_data, indent=4)

# Save the JSON object to a file
with open('another_converter_output.json', 'w') as json_file:
    json_file.write(resume_json)

print("PDF content has been converted to JSON and saved to 'resume.json'.")
