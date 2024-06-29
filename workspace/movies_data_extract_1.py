import pandas as pd
import matplotlib.pyplot as plt

def netflix_analysis_part_1():
    # read csv file as DataFrame
    netflix_df = pd.read_csv("../resources/netflix_data.csv")

    columns = netflix_df.columns

    print(columns)

    # filter 'movie' type
    movie_types_df = netflix_df[netflix_df["type"] == "Movie"]

    # prints out selected columns and number of rows:
    print(movie_types_df[['type', 'title', 'duration']][20:25])

    # filter movies released in the 1990's
    movie_type_and_year_df = movie_types_df[(movie_types_df["release_year"] >= 1990) & (movie_types_df["release_year"] < 2000)]

    movies_count = movie_type_and_year_df["show_id"].count()

    print("number of movies released in the 1990s: " + str(movies_count))

    plt.hist(movie_type_and_year_df["duration"])
    plt.title('Durations of movies in the 1990s')
    plt.xlabel('Duration (minutes)')
    plt.ylabel('Number of Movies')
    plt.show()


if __name__ == '__main__':
    netflix_analysis_part_1()

