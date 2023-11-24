
from flask import Flask, request, jsonify
from ariadne import gql, make_executable_schema, graphql_sync # pyright: ignore
from ariadne import load_schema_from_path # pyright: ignore
from os import environ
from supp.config import todo, set_config

server = Flask(__name__)
set_config()

# --
# make executable gql schema based on typedefs and resorvers
#

type_defs = load_schema_from_path(environ['SCHEMA_PATH'])
exe_schema = make_executable_schema(type_defs, todo['resolvers'])

# --
# response gql queries
# 

@server.route("/", methods=["POST"])
def run_query():

   query = request.get_json()
   success, result = graphql_sync(exe_schema, query, context_value={"request": request})
   status_code = 200 if success else 400
   return jsonify(result), status_code

# --
# start server
#

# server.run(host='0.0.0.0', port=4000, debug=True)
server.run(host='0.0.0.0', port=4000)

