import re

# Function to clean Arabic text
def clean_arabic_text(text):
    # Replace newlines with spaces (to keep text continuous)
    # text = text.replace("\n", " ").strip()

    # Normalize spaces: replace multiple spaces with a single space
    # text = re.sub(r'\s+', ' ', text)

    # Remove unwanted characters or symbols (misinterpreted OCR symbols, non-Arabic characters)
    # This regex keeps Arabic characters and spaces only
    text = re.sub(r'[^\x00-\x7F\u0600-\u06FF\s]+', '', text)

    return text

# Path to the input file (update as needed)
input_file_path = 'Gr.12-Term 1-history_Arabic.txt'
output_file_path = 'Gr.12-Term 1-history_Arabic_cleaned.txt'

# Open and read the input text file
with open(input_file_path, 'r', encoding='utf-8') as input_file:
    file_content = input_file.read()

# Clean the text
cleaned_text = clean_arabic_text(file_content)

# Write the cleaned text to a new file
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    output_file.write(cleaned_text)

print(f"Cleaned text has been saved to: {output_file_path}")

