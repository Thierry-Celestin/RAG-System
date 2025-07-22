import re

def clean_text(raw_text):
    text = re.sub(r'\n+', '\n', raw_text)
    text = re.sub(r'\s+', ' ', text)
    text = text.strip()
    return text

if __name__ == "__main__":
    sample_text = "Your deductible is $500. \n\n\n Coverage starts..."
    print(clean_text(sample_text))
