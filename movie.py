import streamlit as st
import pickle
import requests
from PIL import Image
from io import BytesIO

df = pickle.load(open('movies.pkl', 'rb'))
movies_list = df['title'].values
st.header("Movie Recommendation System")
selected_movie = st.selectbox('choose movies', movies_list)
similarity = pickle.load(open('similarity.pkl', 'rb'))


def get_movie_poster(movie_title):
    api_key = 'd84abdce4b7b8a069bdb83d14a36aff7'
    base_url = 'https://api.themoviedb.org/3/search/movie'
    params = {'api_key': api_key, 'query': movie_title}

    responses = requests.get(base_url, params=params)
    data = responses.json()

    if data['results']:
        poster_path = data['results'][0]['poster_path']
        poster_urls = f"https://image.tmdb.org/t/p/w500{poster_path}"
        return poster_urls
    else:
        return None


def recommend_movie(movie):
    movies = movie.lower()
    rec_movies = []
    movie_index = df[df['title'].str.lower() == movies].index[0]
    distances = similarity[movie_index]
    sorted_array = sorted(enumerate(distances), key=lambda x: x[1], reverse=True)
    for item in sorted_array[1:7]:
        rec_movies.append(df.iloc[item[0], 7])
    return rec_movies


if st.button('Recommend'):
    num_rows = 2
    num_cols = 3
    recommendations = recommend_movie(selected_movie)
    st.subheader('Recommended Movies:')
    for row in range(num_rows):
        cols = st.columns(num_cols)
        for col_index, movie in enumerate(recommendations[row * num_cols:(row + 1) * num_cols]):
            cols[col_index].write(movie)
            poster_url = get_movie_poster(movie)  # Get the movie poster URL
            if poster_url:
                response = requests.get(poster_url)
                img = Image.open(BytesIO(response.content))
                cols[col_index].image(img, caption=movie, width=200)
            else:
                cols[col_index].write("Poster not available")


