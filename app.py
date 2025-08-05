import streamlit as st
import joblib
import pandas as pd

data = joblib.load("recommandation2.sav")
similarity = data['similarity']
movies = data['movies']

st.set_page_config(
    page_title="🎬 Movie Recommender",
    page_icon="🎥",
    layout="centered"
)

st.markdown("""
    <style>
        .main-title {
            font-size: 48px;
            text-align: center;
            font-weight: bold;
            color: #333;
            margin-bottom: 10px;
        }
        .subtitle {
            text-align: center;
            font-size: 18px;
            color: #666;
            margin-bottom: 30px;
        }
        .recommend-box {
            background-color: #ffffff;
            border-radius: 10px;
            padding: 20px;
            margin-top: 20px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.05);
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='main-title'>🎬 Movie Recommender</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Select a movie and get top 5 similar movie recommendations!</div>", unsafe_allow_html=True)

movie_list = movies['title'].values
selected_movie = st.selectbox("📽️ Select a Movie", movie_list)

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = similarity[index]
    recommended = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    return [movies.iloc[i[0]].title for i in recommended]

if st.button("🎯 Recommend"):
    recommendations = recommend(selected_movie)
    st.markdown("<div class='recommend-box'>", unsafe_allow_html=True)
    st.subheader("📢 Recommended Movies:")
    for i, movie in enumerate(recommendations, 1):
        st.markdown(f"**{i}.** {movie}")
    st.markdown("</div>", unsafe_allow_html=True)
