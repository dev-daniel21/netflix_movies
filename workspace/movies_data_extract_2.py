import pandas as pd
import matplotlib.pyplot as plt


def netflix_analysis_part_2():
    # read csv file as DataFrame
    netflix_df = pd.read_csv("../resources/netflix_data.csv")

    action_movies = netflix_df[(netflix_df["type"] == "Movie") & (netflix_df["genre"] == "Action")]

    action_movie_2000s = action_movies[(action_movies["release_year"] > 2000) & (action_movies["release_year"] < 2010)]

    action_movie_count = (action_movie_2000s["show_id"]).count()

    print(action_movie_count)

    plt.hist(action_movies["duration"])
    plt.title('Durations of action movies')
    plt.xlabel('Duration (minutes)')
    plt.ylabel('Number of Movies')
    plt.show()


if __name__ == '__main__':
    netflix_analysis_part_2()