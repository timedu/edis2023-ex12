
# Reference: <https://blog.logrocket.com/build-graphql-api-python-flask-ariadne/>

from ariadne import QueryType # pyright: ignore

query = QueryType()

@query.field("places")
def places(*_):
   return [
       {"name": "Paris", "description": "The city of lights", "country": "France"},
       {"name": "Rome", "description": "The city of pizza", "country": "Italy"},
       {
           "name": "London",
           "description": "The city of big buildings",
           "country": "United Kingdom",
       },
   ]
