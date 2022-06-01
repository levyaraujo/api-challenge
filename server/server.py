from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from flask_cors import CORS
from .csv_search import search

app = Flask(__name__)
api = Api(app)
CORS(app, resources={r"/*": {"origins": "*"}})


class SearchData(Resource):
    def get(self):
        key = request.args.get("key")
        result = search(key)
        return jsonify(result)


api.add_resource(SearchData, "/search")
