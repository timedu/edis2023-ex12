
# Reference: <https://fullstackopen.com/osa8/graph_ql_palvelin>
# (Node.js version there)

from ariadne import QueryType # pyright: ignore
from examples.persons.data import persons

query = QueryType()

@query.field("person_count")
def person_count(*_):
    return len(persons)

@query.field("all_persons")
def all_persons(*_):
    return persons

@query.field("find_person")
def find_person(*_, name):
    return next((person for person in persons if person.get('name') == name), None)
