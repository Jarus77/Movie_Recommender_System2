# Movie Recommendation System

This is a simple movie recommendation system built using Streamlit. The system recommends movies based on user input and displays them along with their posters. Below is an explanation of the code and how to use it.

## Features
- Select a movie from the dropdown menu.
- Click the "Recommend" button to get a list of recommended movies.
- Recommended movies will be displayed along with their posters.
- Uses movie data stored in a pickle file and a precomputed similarity matrix that is computed under movie.ipynb .

## How to Use
1. Clone this GitHub repository to your local machine.
2. Ensure you have the necessary dependencies installed. You can install them using `pip install streamlit pillow requests`.
3. Place the `movies.pkl` (pickle file containing movie data) and `similarity.pkl` (pickle file containing similarity matrix) in the same directory as your script.
4. Run the script using `streamlit run movie.py`.

## Code Explanation

### Imports
- `streamlit`: A Python library for creating web apps.
- `pickle`: Used to load movie data and similarity matrix from pickle files.
- `requests`: For making HTTP requests to a movie API.
- `PIL`: Python Imaging Library for handling images.
- `Image` and `BytesIO` are used to display movie posters.

### Data Loading
- Load movie data from `movies.pkl` and store it in a DataFrame.
- Create a list of movie titles.

### Streamlit Setup
- Set the header for the web app as "Movie Recommendation System."
- Create a dropdown menu with movie titles for user selection.
- Load the similarity matrix from `similarity.pkl`.

### Functions
- `get_movie_poster(movie_title)`: This function retrieves the poster URL for a given movie title using the TMDb API. It returns the URL or `None` if no poster is found.
- `recommend_movie(movie)`: This function recommends movies based on the selected movie. It finds the most similar movies using the precomputed similarity matrix.

### Recommendation Display
- When the "Recommend" button is clicked, it calculates and displays the recommended movies.
- Movies are displayed in a grid with two rows and three columns.
- For each recommended movie, the script attempts to fetch and display its poster.
- If a poster is not available, it displays a message indicating so.

## Note
- You need to replace `'d84abdce4b7b8a069bdb83d14a36aff7'` with your own TMDb API key in the `get_movie_poster` function.
- Make sure you have a stable internet connection to fetch movie posters from the TMDb API.



Happy movie recommending! 🍿
