"""
- Enter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie, and 'q' to quit:

-Add movies
-See movies
-Find a movie
-Stop running the program

Tasks:
[X]: Decide where to store movies
[X]: Whats is the format of a movie?
[x]: Show the user the main interface and get their input
[X]: Allow users to add movies
[X]: Show All their movies
[X]: Find a movie
[x]: Stop running the program when they type 'q'
"""

movies = []

"""
movie = {
    'name': ... (str),
    'director': ... (str),
    'year': ... (int)
}
"""

def menu():
    text = "Enter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie, and 'q' to quit:"
    user_input = input(text)
    choose_option(user_input, text)

def choose_option(user_input, text):
    while user_input != 'q':
        if user_input == 'a':
            add_movie()
        elif user_input == 'l':
            list_movies(movies)
        elif user_input == 'f':
            find_movie()
        else:
            send_unknown_message()
    
        user_input = input(text)

def add_movie():
    movie_name =     input("What is the name of the movie?: ")
    movie_director = input("What is the director of the movie?: ")
    movie_year =     input("Whats is the movie creation year?: ")
    
    movie_info = {
                  "name": movie_name, 
                  "director": movie_director, 
                  "year": movie_year
                  }

    movies.append(movie_info)

def find_movie():
    find_by = input("What property of the movie are you looking for? ")
    looking_for = input("What are you searching for? ")

    found_movies = find_by_attribute(movies, looking_for, lambda x: x[find_by])

    list_movies(found_movies)

def find_by_attribute(items ,expected, finder, found = []):
    for i in items:
        if finder(i) == expected:
            found.append(i)

        return found

def list_movies(movies_list):
    for movie in movies_list:
        show_movie_details(movie)

def show_movie_details(movie):
    print(f"Name: {movie['name']}")
    print(f"Director: {movie['director']}")
    print(f"Release year: {movie['year']}")

def send_unknown_message():
    print("Unknown command-please try again")

menu()
