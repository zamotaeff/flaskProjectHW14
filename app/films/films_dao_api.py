import os
import sqlite3


PATH = os.path.dirname(os.path.realpath(__file__)) + "/"


class FilmsDaoApi:

    def to_dict(self, data):
        keys_value = ['title', 'country', 'release_year', 'genre', 'description']
        new_dict = dict(zip(keys_value, data))

        return new_dict

    def db_cursor_execute(self, search_query):
        """
        Open a connection to the database and make a request
        :param search_query:
        :return: list
        """
        with sqlite3.connect(PATH + '../netflix.db') as con:
            cur = con.cursor()

            result = cur.execute(search_query).fetchall()

            return result

    def search(self, title):
        """
        Search for movies by name
        :param title:
        :return: list
        """

        search_query = (f"SELECT `title`, `country`, `release_year`, `listed_in`, `description` "
                        f"FROM netflix "
                        f"WHERE `title` LIKE '%{title}%' "
                        f"ORDER BY `release_year` DESC "
                        f"LIMIT 1")

        result = self.db_cursor_execute(search_query)

        return result

    def search_by_date_range(self, date_at, date_to):
        """
        Search for movies by time period
        :param date_at:
        :param date_to:
        :return: list
        """

        search_query = (f"SELECT `title`, `release_year` "
                        f"FROM netflix "
                        f"WHERE `release_year` BETWEEN {date_at} AND {date_to} "
                        f"ORDER BY `release_year` DESC "
                        f"LIMIT 100")
        result = self.db_cursor_execute(search_query)

        result = [dict(zip(['title', 'release_year'], i)) for i in result]

        return result

    def search_by_rating(self, rating_value):
        """
        Search for movies by rating
        :param rating_value:
        :return: list
        """

        rating_values = {
            'children': 'G',
            'family': ('G', 'PG', 'PG-13'),
            'adult': ('R', 'NC-17')
        }

        rating = rating_values.get(rating_value)

        search_query = (f"SELECT `title`, `rating`, `description` "
                        f"FROM netflix "
                        f"WHERE `rating` IN {rating} "
                        f"LIMIT 100")
        result = self.db_cursor_execute(search_query)

        result = [dict(zip(['title', 'rating', 'description'], i)) for i in result]

        return result

    def search_by_genre(self, genre_value):
        """
        Search for movies by genre
        :param genre_value:
        :return: list
        """

        search_query = (f"SELECT `title`, `description` "
                        f"FROM netflix "
                        f"WHERE `listed_in` LIKE '%{genre_value.title()}%' "
                        f"LIMIT 100")
        result = self.db_cursor_execute(search_query)
        result = [dict(zip(['title', 'description'], i)) for i in result]

        return result

    def search_by_artist(self, artist_one, artist_two):
        """
        Search for movies by artist
        :param artist_one: artist first and second name
        :param artist_two: artist first and second name
        :return: list
        """

        search_query = (f"SELECT `cast` "
                        f"FROM netflix "
                        f"WHERE `cast` LIKE '%{artist_one}%' AND `cast` LIKE '%{artist_two}%'")
        result = []

        names_dict = {}
        for item in self.db_cursor_execute(search_query):

            names = set(item) - set([artist_one, artist_two])

            for name in names:
                names_dict[str(name).strip()] += names_dict.get(str(name).strip(), 0) + 1

        for key, value in names_dict.items():
            if value >= 2:
                result.append(key)

    def search_by_type_year_genre(self, film_type, year, genre):
        """
        Search for movies by type, year release and genre
        :param type:
        :param year:
        :param genre:
        :return: list
        """

        search_query = (f"SELECT `title`, `description` "
                        f"FROM netflix "
                        f"WHERE `type`='{film_type}' AND `release_year`={year} "
                        f"AND `listed_in` LIKE '%{genre}%' "
                        f"LIMIT 100")
        result = self.db_cursor_execute(search_query)
        result = [dict(zip(['title', 'description', ], i)) for i in result]

        return result
