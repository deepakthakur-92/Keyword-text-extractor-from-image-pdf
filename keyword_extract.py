import spacy
import re
# load the englishlanguage model
nlp = spacy.load("en_core_web_sm")

def extract_keywords(text):
    # process the text with spacy
    doc=nlp(text)

    #extract keywords based on relavant criteria(e.g., noun phrases)
    keywords = [chunk.text for chunk in doc.noun_chunks]

    return keywords