from keyword_extract import extract_keywords
import re
import spacy

nlp = spacy.load("en_core_web_sm")

# function to extract entities(name, location, skills)

def extract_entities(text):
    doc = nlp(text)
    entities = {
        'name':[],
        'location':[],
        'skills':[],
        'keywords':[]

    }

    for ent in doc.ents:
        if ent.label_ == "PERSON":
            entities["name"].append(ent.text)
        elif ent.label_ == "GPE":
            entities["location"].append(ent.text)
        elif ent.label_ == "SKILLS":
            entities["skils"].append(ent.text)

    return entities

# function to extract phone numbers using regular expression
def extract_phone_number(text):
    phone_numbers = re.findall(r'\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b', text)
    return phone_numbers

# function to extract email addresses using regular expression
def extract_emails(text):
    emails = re.findall(r'\S+@\S+', text)
    return emails

# function to extract information (skills, location, keywords)
def extract_information(text):
    extracted_entites = {
        'name': [],
        'location': [],
        'skills': [],
        'keywords': []
    }

    doc = nlp(text)

    # extract skills using specific rules or patterns
    skill_list = ['python', 'Machine Learning', 'Data Analysis', 'SQL', 'Latex']
    for token in doc:
        if token.text in skill_list:
            extracted_entites["skills"].append(token.text)

    # extract locationentities(modify as per your requirements)
    for ent in doc.ents:
        if ent.label_ == "GPE":
            extracted_entites["location"].append(ent.text)

    # extract keywords using your preferred techniques (e.g., YAKE)
    extracted_entites["keywords"] = extract_keywords(text)

    return extracted_entites


