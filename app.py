import streamlit as st
import pickle
with open('recommandation2.sav', 'rb') as f:
    new_df = pickle.load(f)
with open('recommandation.sav', 'rb') as f:
    similarity = pickle.load(f)
def recommend(movie):
    movie_index = new_df[new_df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    return [new_df.iloc[i[0]].title for i in movie_list]
st.set_page_config(page_title="Movie Recommender", layout="centered")
st.title("Movie Recommendation System")
selected_movie = st.selectbox("Choose a movie", new_df['title'].values)
if st.button("Get Recommendations"):
    recommendations = recommend(selected_movie)
    st.subheader("Top 5 Recommended Movies:")
    for i, movie in enumerate(recommendations, 1):
        st.write(f"{i}. {movie}")
