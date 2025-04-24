# nlp_app.py

import streamlit as st
# NLP Pkgs
from textblob import TextBlob
from nltk.stem.wordnet import WordNetLemmatizer
import re

# If you haven't downloaded the wordnet resource, uncomment the following two lines once:
#import nltk
#nltk.download("wordnet")

def clean_text(text):
    """Clean and lemmatize input text."""
    # Keeping only Text and digits
    text = re.sub(r"[^A-Za-z0-9]", " ", text)
    # Removes Whitespaces
    text = re.sub(r"\'s", " ", text)
    # Removing Links if any
    text = re.sub(r"http\S+", " link ", text)
    # Removes Numbers
    text = re.sub(r"\b\d+(?:\.\d+)?\s+", "", text)
    # Splitting Text
    words = text.split()
    # Lemmatizer
    lemmatizer = WordNetLemmatizer()
    lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
    return " ".join(lemmatized_words)

# 1) GUI part
st.title("Sentiment Analysis NLP Application")  
st.subheader("Please enter a text, click Analyze to view the sentiment (positive/negative/neutral)")
user_input = st.text_area("Input Text", height=200)

# 2) When the button is clicked, clean, predict, and display
if st.button("Analyze"):
    cleaned = clean_text(user_input)
    blob = TextBlob(cleaned)
    result = blob.sentiment.polarity

    if result > 0:
        custom_emoji = ":blush:"
        st.success("Happy : {}".format(custom_emoji))
    elif result < 0:
        custom_emoji = ":disappointed:"
        st.warning("Sad : {}".format(custom_emoji))
    else:
        custom_emoji = ":confused:"
        st.info("Confused : {}".format(custom_emoji))

    st.success("Polarity Score is: {}".format(result))
