
from ariadne import QueryType # pyright: ignore
import requests
from data.genres24 import genres

json_server = 'http://json-server:4000/films';


query = QueryType()

@query.field("all_genres")
def all_genres(*_):
    
    # -- replace with actual code
    return [
        'Genre name 1',
        'Genre name 2'
    ]
    # --


@query.field("find_films")
def find_films(*_, genre):

    # -- replace with actual code
    return [
        {
            'genre': 'Genre name',
            'name': 'Movie name',
            'directed_by': 'Director Name',
            'initial_release_date': '2022-12-01',
            'id': 100
        },
        {
            'name': 'Movie name',
            'genre': 'Genre name',
            'directed_by': 'Director Name',
            'initial_release_date': '2022-12-01',
            'id': 200
        }
    ]
    # --


@query.field("count_films")
def count_films(*_, genre=None):

    # -- replace with actual code
    return 99
    # --
