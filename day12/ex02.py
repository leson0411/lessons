def print_show_info(movies):
    print(f"{movies['title']} ({movies['initial_release']}) - {movies['seasons']} seasons")


movies = {
    "title": "Breaking Bad",
    "seasons": 5,
    "initial_release": 2008
}

print_show_info(movies)
