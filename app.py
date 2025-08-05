import streamlit as st
import joblib
import numpy as np

model = joblib.load("recommandation.sav")

st.set_page_config(
    page_title="Movie Recommendation App 🎬",
    layout="wide",
    page_icon="🎥"
)
st.markdown("""
    <style>
        .main {
            background-color: #f0f2f6;
            padding: 2rem;
        }
        .title {
            font-size: 3rem;
            font-weight: bold;
            color: #4a4a4a;
        }
        .subtitle {
            font-size: 1.2rem;
            color: #666;
        }
        .recommendation {
            font-size: 1.1rem;
            color: #333;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main">', unsafe_allow_html=True)
st.markdown('<p class="title">Movie Recommendation System</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Enter a movie you like, and we\'ll recommend similar ones for you!</p>', unsafe_allow_html=True)

movie_input = st.text_input("Type a movie name")

def recommend(movie):
    try:
        movie_index = model['new_df'][model['new_df']['title'] == movie].index[0]
        distances = model['similarity'][movie_index]
        movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
        return [model['new_df'].iloc[i[0]].title for i in movies_list]
    except:
        return []

if st.button("Get Recommendations 🎯"):
    if movie_input.strip() == "":
        st.warning("Please enter a movie name.")
    else:
        recommendations = recommend(movie_input)
        if recommendations:
            st.success("Here are your recommendations:")
            for i, rec in enumerate(recommendations, 1):
                st.markdown(f"<p class='recommendation'>{i}. {rec}</p>", unsafe_allow_html=True)
        else:
            st.error("Movie not found. Please try another.")

st.markdown('</div>', unsafe_allow_html=True)
