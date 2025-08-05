import streamlit as st
import joblib

data = joblib.load("recommandation2.sav")

# Check what's inside the loaded file
st.write("Model data type:", type(data))

if isinstance(data, dict):
    st.write("Keys in model:", list(data.keys()))

    if 'similarity' in data and 'movies' in data:
        similarity = data['similarity']
        movies = data['movies']

        selected_movie = st.selectbox("Select a movie", movies['title'].values)

        def recommend(movie):
            index = movies[movies['title'] == movie].index[0]
            distances = similarity[index]
            recommended = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
            return [movies.iloc[i[0]].title for i in recommended]

        if st.button("Recommend"):
            for i in recommend(selected_movie):
                st.write(i)
    else:
        st.error("Model file does not contain 'similarity' or 'movies' keys.")
else:
    st.error("Model file is not in expected dictionary format.")
