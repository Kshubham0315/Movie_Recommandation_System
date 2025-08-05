import streamlit as st
import joblib
import pandas as pd

model_data = joblib.load("recommandation2.sav")
new_df = model_data['new_df']
similarity = model_data['similarity']

st.set_page_config(
    page_title=" Movie Recommender",
    page_icon=" ",
    layout="centered"
)

st.markdown("""
    <style>
        body {
            background-color: #f4f4f4;
        }
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

st.markdown("<div class='main-title'> Movie Recommender</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Select a movie and get top 5 similar movie recommendations!</div>", unsafe_allow_html=True)

movie_list = new_df['title'].values
selected_movie = st.selectbox("Select a Movie", movie_list)

def recommend(movie):
    index = new_df[new_df['title'] == movie].index[0]
    distances = similarity[index]
    recommended_movies = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    return [new_df.iloc[i[0]].title for i in recommended_movies]

if st.button("Recommend"):
    recommendations = recommend(selected_movie)
    st.markdown("<div class='recommend-box'>", unsafe_allow_html=True)
    st.subheader("Recommended Movies:")
    for i, movie in enumerate(recommendations, 1):
        st.markdown(f"**{i}.** {movie}")
    st.markdown("</div>", unsafe_allow_html=True)
