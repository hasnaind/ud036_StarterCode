import webbrowser

class Movie():
    '''This class provides a way to store information about movies'''
    def __init__(self,movie_title,movie_storyline,poster_image,imbd_ratings,trailer_url):
        self.title=movie_title
        self.storyline=movie_storyline
        self.poster_image_url=poster_image
        self.imbd_ratings=imbd_ratings
        self.trailer_youtube_url=trailer_url
    def show_trailer(self):
        #This function open a youtube page for the movie trailer
        webbrowser.open(self.trailer_youtube_url)
