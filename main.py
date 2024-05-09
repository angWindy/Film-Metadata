import numpy as np
import pandas as pd
from flask import Flask, render_template, request
import requests

# API TMDB
ACCESS_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0NTRmNDRhNWNmYjUzZGRhYTc1YjkyZmQ5YTUwYWIwNCIsInN1YiI6IjY2MjBjMTBhOTY2MWZjMDE0YmZmYjQwMCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.9efQcoH6zuKqgNEHiFBxMFK_Oep5Nx-3cQfshrVFh3E"
API_KEY = "454f44a5cfb53ddaa75b92fd9a50ab04"


def get_movie_id(movie_name):
    base_url = "https://api.themoviedb.org/3"
    search_endpoint = "/search/movie"
    params = {"api_key": API_KEY, "query": movie_name}
    response = requests.get(base_url + search_endpoint, params=params)
    if response.status_code == 200:
        data = response.json()
        if data["results"]:
            return data["results"][0]["id"]
        else:
            return None
    else:
        return None


def rcmd(movie_name):  # return list[]
    movie_id = get_movie_id(movie_name)
    if movie_id == None:
        return "Sorry! The movie you requested is not in our database. Please check the spelling or try with some other movies"

    url = f"https://api.themoviedb.org/3/movie/{movie_id}/recommendations?language=en-US&page=1"

    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {ACCESS_TOKEN}",
    }

    response = requests.get(url, headers=headers)

    data = response.json()  # Chuyển đổi phản hồi thành đối tượng JSON
    suggestions = []  # Danh sách để lưu trữ các tên phim

    for item in data["results"]:
        title = item["title"]  # Trích xuất tên phim từ mỗi mục trong kết quả
        suggestions.append(title)

    return suggestions[0:10]  # In ra danh sách các tên phim


# converting list of string to list (eg. "["abc","def"]" to ["abc","def"])
def convert_to_list(my_list):
    my_list = my_list.split('","')
    my_list[0] = my_list[0].replace('["', "")
    my_list[-1] = my_list[-1].replace('"]', "")
    return my_list


def get_suggestions():
    data = pd.read_csv("Data/main_data.csv")
    return list(data["movie_title"].str.capitalize())


app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    suggestions = get_suggestions()
    return render_template("home.html", suggestions=suggestions)


@app.route("/similarity", methods=["POST"])
def similarity():
    movie_name = request.form["name"]
    rc = rcmd(movie_name)
    if type(rc) == type("string"):
        return rc
    else:
        m_str = "---".join(rc)
        return m_str


@app.route("/recommend", methods=["POST"])
def recommend():
    # getting data from AJAX request
    title = request.form["title"]
    cast_ids = request.form["cast_ids"]
    cast_names = request.form["cast_names"]
    cast_chars = request.form["cast_chars"]
    cast_bdays = request.form["cast_bdays"]
    cast_bios = request.form["cast_bios"]
    cast_places = request.form["cast_places"]
    cast_profiles = request.form["cast_profiles"]
    imdb_id = request.form["imdb_id"]
    poster = request.form["poster"]
    genres = request.form["genres"]
    overview = request.form["overview"]
    vote_average = request.form["rating"]
    vote_count = request.form["vote_count"]
    release_date = request.form["release_date"]
    runtime = request.form["runtime"]
    status = request.form["status"]
    rec_movies = request.form["rec_movies"]
    rec_posters = request.form["rec_posters"]

    # get movie suggestions for auto complete
    suggestions = get_suggestions()

    # call the convert_to_list function for every string that needs to be converted to list
    rec_movies = convert_to_list(rec_movies)
    rec_posters = convert_to_list(rec_posters)
    cast_names = convert_to_list(cast_names)
    cast_chars = convert_to_list(cast_chars)
    cast_profiles = convert_to_list(cast_profiles)
    cast_bdays = convert_to_list(cast_bdays)
    cast_bios = convert_to_list(cast_bios)
    cast_places = convert_to_list(cast_places)

    # convert string to list (eg. "[1,2,3]" to [1,2,3])
    cast_ids = cast_ids.split(",")
    cast_ids[0] = cast_ids[0].replace("[", "")
    cast_ids[-1] = cast_ids[-1].replace("]", "")

    # rendering the string to python string
    for i in range(len(cast_bios)):
        cast_bios[i] = cast_bios[i].replace(r"\n", "\n").replace(r"\"", '"')

    # combining multiple lists as a dictionary which can be passed to the html file so that it can be processed easily and the order of information will be preserved
    movie_cards = {rec_posters[i]: rec_movies[i] for i in range(len(rec_posters))}

    casts = {
        cast_names[i]: [cast_ids[i], cast_chars[i], cast_profiles[i]]
        for i in range(len(cast_profiles))
    }

    cast_details = {
        cast_names[i]: [
            cast_ids[i],
            cast_profiles[i],
            cast_bdays[i],
            cast_places[i],
            cast_bios[i],
        ]
        for i in range(len(cast_places))
    }

    # # web scraping to get user reviews from IMDB site
    # sauce = urllib.request.urlopen(
    #     "https://www.imdb.com/title/{}/reviews?ref_=tt_ov_rt".format(imdb_id)
    # ).read()
    # soup = bs.BeautifulSoup(sauce, "lxml")
    # soup_result = soup.find_all("div", {"class": "text show-more__control"})

    # reviews_list = []  # list of reviews
    # reviews_status = []  # list of comments (good or bad)
    # for reviews in soup_result:
    #     if reviews.string:
    #         reviews_list.append(reviews.string)
    #         # passing the review to our model
    #         movie_review_list = np.array([reviews.string])
    #         movie_vector = vectorizer.transform(movie_review_list)
    #         pred = clf.predict(movie_vector)
    #         reviews_status.append("Good" if pred else "Bad")

    # # combining reviews and comments into a dictionary
    # movie_reviews = {
    #     reviews_list[i]: reviews_status[i] for i in range(len(reviews_list))
    # }

    # passing all the data to the html file
    return render_template(
        "recommend.html",
        title=title,
        poster=poster,
        overview=overview,
        vote_average=vote_average,
        vote_count=vote_count,
        release_date=release_date,
        runtime=runtime,
        status=status,
        genres=genres,
        movie_cards=movie_cards,
        # reviews=movie_reviews,
        casts=casts,
        cast_details=cast_details,
    )


if __name__ == "__main__":
    app.run(debug=True)
