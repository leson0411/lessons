movies = [("queen of tears", "Korean", 2023, 5000)]
movie_name = input("Enter the movie name: ")
director = input("Enter the director name: ")
year = input("Enter the release year: ")
budget = input("Enter the budget: ")

another_movie = (movie_name, director, year, budget)
print(f"{another_movie[0]}, {another_movie[2]}")

movies.append(another_movie)
print(f"{movies[0]}\n{movies[1]}")

# movies.remove(movies[0])
# del movies[0]
movies.pop(0)
print(movies)
