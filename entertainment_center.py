import media
import fresh_tomatoes

def main():
    '''Creates six Movie objects, initialising these objects with title, storyline,
    poster image link, video trailer link and IMBD rating.'''
    harry_potter=media.Movie("Harry Potter",
                             "Movie about a magic school",
                             "https://upload.wikimedia.org/wikipedia/en/a/a0/Harry_Potter_and_the_Prisoner_of_Azkaban.jpg",
                             "7.8",
                             "https://www.youtube.com/watch?v=lAxgztbYDbs")
    unbroken=media.Movie("Unbroken",
                         "Movie about a courageous soldier",
                         "https://upload.wikimedia.org/wikipedia/en/7/76/Unbroken_poster.jpg",
                         "7.2",
                         "https://www.youtube.com/watch?v=XrjJbl7kRrI&t=57s")
    twilight=media.Movie("Twilight",
                         "Love story of a vampire and a human girl",
                         "https://upload.wikimedia.org/wikipedia/en/b/b6/Twilight_%282008_film%29_poster.jpg",
                         "5.2",
                         "https://www.youtube.com/watch?v=uxjNDE2fMjI")
    pirates_of_caribbean=media.Movie("Pirates of Caribbean",
                                     "Fantasy pirates movie",
                                     "https://upload.wikimedia.org/wikipedia/en/5/5a/Pirates_AWE_Poster.jpg",
                                     "7.1",
                                     "https://www.youtube.com/watch?v=HKSZtp_OGHY")
    midnight_in_paris=media.Movie("Midnight In Paris",
                                  "A movie about time travel",
                                  "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                                  "7.7",
                                  "https://www.youtube.com/watch?v=FAfR8omt-CY")
    the_avengers=media.Movie("The Avengers",
                             "Superheroes fights together to save the world",
                             "https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg",
                             "8.1",
                             "https://www.youtube.com/watch?v=eOrNdBpGMv8")

    movies=[harry_potter,unbroken,twilight,pirates_of_caribbean,midnight_in_paris,the_avengers]
    #fresh_tomatoes module has a function called open_movies_page which takes a list or array of movies and generate an html page
    #containing titles,box art imagery, ratings and trailers of those movies.
    fresh_tomatoes.open_movies_page(movies)
if __name__=='__main__':
    main()
