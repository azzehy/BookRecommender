import pickle
import streamlit as st
import numpy as np
from PIL import Image
import requests
from io import BytesIO
# images to be improved
# Set Page Config
st.set_page_config(page_title="📚 Book Recommender", layout="wide")

# Dark Mode Styling
st.markdown(
    """
    <style>
    /* Global background */
    .stApp {
        background-color: #121212;
        color: #FFFFFF;
    }
    
    /* Header Styling */
    .stHeader {
        text-align: center;
        color: #4CAF50;
        font-size: 2em;
        font-weight: bold;
    }

    /* Button Styling */
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
        border-radius: 8px;
    }

    /* Select Box Styling */
    .stSelectbox label {
        font-weight: bold;
        color: #BBBBBB;
    }

    /* Image Styling */
    .stImage img {
        border-radius: 10px;
        border: 2px solid #4CAF50;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar
st.sidebar.title("📖 AI Book Recommender")
st.sidebar.markdown("👋 Discover books tailored to your taste! Just pick a book, and let AI do the magic! ✨")

# Page Header
st.markdown("<h1 class='stHeader'>📚 AI-Powered Book Recommender</h1>", unsafe_allow_html=True)
st.write("✨ **Discover books tailored to your taste using Machine Learning!**")

# Load Model & Data
try:
    model = pickle.load(open('artifacts/model.pkl', 'rb'))
    book_names = pickle.load(open('artifacts/book_names.pkl', 'rb'))
    ratingsGeneralInfo = pickle.load(open('artifacts/ratingsGeneralInfo.pkl', 'rb'))
    book_pivot = pickle.load(open('artifacts/book_pivot.pkl', 'rb'))
except FileNotFoundError:
    st.error("⚠️ Required data files not found! Please check the 'artifacts/' directory.")


# Book Recommendation Function
def recommend_book(book_name):
    try:
        book_id = np.where(book_pivot.index == book_name)[0][0]
        distances, suggestions = model.kneighbors(book_pivot.iloc[book_id, :].values.reshape(1, -1), n_neighbors=6)

        recommended_books = []
        poster_urls = []
        
        for book_id in suggestions[0]:
            book_title = book_pivot.index[book_id]
            idx = ratingsGeneralInfo[ratingsGeneralInfo['title'] == book_title].index
            recommended_books.append(book_title)

            if len(idx) > 0:
                poster_urls.append(ratingsGeneralInfo.loc[idx[0], 'image_url'])
            else:
                poster_urls.append("https://via.placeholder.com/140x210.png?text=No+Image")

        return recommended_books, poster_urls
    except IndexError:
        st.error("⚠️ Book not found in database. Try another one!")
        return [], []

# User Input: Select a Book
selected_book = st.selectbox("📖 Choose a Book:", book_names)

# Show Recommendations
if st.button("🎯 Show Recommendations"):
    recommended_books, poster_urls = recommend_book(selected_book)

    if recommended_books:
        cols = st.columns(5)  # Display in 5 columns
        for i in range(1, 6):  # Ignore the first book (itself)
            with cols[i-1]:
                st.image(poster_urls[i], use_container_width=True, caption=f"📖 {recommended_books[i]}", output_format="JPG")

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #BBBBBB;'>🚀 Developed with ❤️ using Streamlit & Machine Learning</h4>", unsafe_allow_html=True)
