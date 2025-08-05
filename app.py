import streamlit as st
import pickle

# Load model
with open('recommandation2.sav', 'rb') as file:
    model = pickle.load(file)

# Load movie list (if not part of model)
# Agar model ke andar movie list nahi toh use is tarah alag load karna padega
# with open('movies.pkl', 'rb') as f:
#     movie_list = pickle.load(f)

# Dummy movie list (replace with actual one)
movie_list = ['Avatar', 'Inception', 'The Dark Knight', 'Interstellar', 'Titanic']

# Streamlit UI
st.title("🎬 Movie Recommendation System")

selected_movie = st.selectbox("Choose a movie", movie_list)

if st.button("Get Recommendations"):
    try:
        recommendations = model.recommend(selected_movie)
        st.subheader("Top 5 Similar Movies:")
        for i, movie in enumerate(recommendations):
            st.write(f"{i+1}. {movie}")
    except Exception as e:
        st.error(f"Error: {e}")
