import os
from pprint import pprint

from flask import Blueprint, jsonify

from app.films.films_dao_api import FilmsDaoApi

PATH = os.path.dirname(os.path.realpath(__file__)) + "/"

films_api_dao = FilmsDaoApi()

films_api_blueptint = Blueprint('films_api_blueprint',
                                __name__,
                                url_prefix='/api/v1')


@films_api_blueptint.route('/movie/<title>/')
def page_api_search_by_title(title):
    """
    Endpoit for search film by title
    :param title:
    :return: json response
    """

    return jsonify(films_api_dao.search(title))


@films_api_blueptint.route('/movie/<year_at>/to/<year_to>/')
def page_api_search_by_date(year_at, year_to):
    """
    Endpoit for search film by years range
    :param year_at:
    :param year_to:
    :return: json response
    """
    return jsonify(films_api_dao.search_by_date_range(year_at, year_to))


@films_api_blueptint.route('/rating/<rating_value>/')
def page_api_search_by_rating(rating_value):
    """
    Endpoit for search film by rating
    :param rating_value:
    :return: json response
    """
    return jsonify(films_api_dao.search_by_rating(rating_value))


@films_api_blueptint.route('/genre/<genre_value>/')
def page_api_search_by_genre(genre_value):
    """
    Endpoit for search film by genre
    :param genre_value:
    :return: json response
    """
    pprint(films_api_dao.search_by_artist('Ben Lamb', 'Rose McIver'))

    return jsonify(films_api_dao.search_by_genre(genre_value))
