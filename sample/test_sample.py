from parameterized import parameterized
import unittest

class TestMovieService(unittest.TestCase):
    # A sample movie store for testing purposes
    movie_store = [
        {'title': 'Movie 1', 'year': '2022', 'language': 'Kannada'},
        {'title': 'Movie 2', 'year': '2023', 'language': 'Kazakh'},
        {'title': 'Movie 3', 'year': '2024', 'language': 'Khmer'}
    ]

    @parameterized.expand([
        (None, None),  # Should raise an exception
        ('2022', 'Kannada'),  # Should return movies from 2022 in Kannada
        ('2023', 'Kazakh'),  # Should return movies from 2023 in Kazakh
        ('2024', 'Khmer'),  # Should return movies from 2024 in Khmer
    ])
    def test_invalid_input(self, year, language):
        service = MovieService(self.movie_store)
        
        # Test for invalid input (both year and language are None)
        if not year and not language:
            with self.assertRaises(Exception):
                service.movie_service_handler(year, language)
        else:
            # For valid inputs, it should not raise an exception
            try:
                result = service.movie_service_handler(year, language)
                self.assertIsNotNone(result)  # Ensure the result is not None
            except Exception as e:
                self.fail(f"movie_service_handler raised an exception {e}")
