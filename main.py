import streamlit as st
import nltk
from nltk.tokenize import TreebankWordTokenizer
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
import string
from textblob import TextBlob  # ✅ Added for spelling correction

# -------------------------------
# Download NLTK resources (only once)
# -------------------------------
nltk.download("punkt")
nltk.download("stopwords")
nltk.download("wordnet")

# -------------------------------
# Initialize tools
# -------------------------------
stop_words = set(stopwords.words("english"))
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

# -------------------------------
# Streamlit App Configuration
# -------------------------------
st.set_page_config(page_title="🔤 NLP Playground", layout="centered")
st.title("🔤 NLP Text Preprocessing Playground")
st.write("Enter a sentence to clean, correct, tokenize, stem, and lemmatize.")

# -------------------------------
# Input
# -------------------------------
text_input = st.text_area("✏ Enter your sentence:", height=150)

# -------------------------------
# Process Button
# -------------------------------
if st.button("🧪 Process"):
    if not text_input.strip():
        st.warning("Please enter some text.")
    else:
        # Step 1: Lowercase and remove punctuation
        cleaned = text_input.lower().translate(str.maketrans("", "", string.punctuation))
        st.markdown(f"🧹 Cleaned Text: `{cleaned}`")

        # Step 2: Spelling Correction (TextBlob)
        corrected_text = str(TextBlob(cleaned).correct())
        st.markdown(f"📝 Spelling Corrected: `{corrected_text}`")

        # Step 3: Tokenization
        tokenizer = TreebankWordTokenizer()
        tokens = tokenizer.tokenize(corrected_text)
        st.markdown(f"🔠 Tokens: `{tokens}`")

        # Step 4: Remove Stopwords
        filtered = [word for word in tokens if word not in stop_words]
        st.markdown(f"⛔ Without Stopwords: `{filtered}`")

        # Step 5: Stemming
        stemmed = [stemmer.stem(word) for word in filtered]
        st.markdown(f"🌱 Stemmed Words: `{stemmed}`")

        # Step 6: Lemmatization
        lemmatized = [lemmatizer.lemmatize(word) for word in filtered]
        st.markdown(f"🍋 Lemmatized Words: `{lemmatized}`")
