class MovieService:
    
    def __init__(self, movie_store=None):
        self.movie_store = movie_store
    

    def set_movies_language(self, language=None):
        movie_list = []
        for movie in self.movie_store:
            if movie.get('language') == language:
                movie_list.append(movie)
        return movie_list
    

    def get_movie_by_year(self, year=None):
        movie_list = []
        for movie in self.movie_store:
            if movie.get('year') == year:
                movie_list.append(movie)
        return movie_list
    
    def movie_service_handler(self, year=None, language=None):
        if not year and not language:
            raise Exception("At least one of 'year' or 'language' must be provided.")
        
        if year:
            return self.get_movie_by_year(year)
        
        if language:
            return self.set_movies_language(language)
