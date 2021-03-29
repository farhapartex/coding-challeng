from flask.views import View, MethodView
from flask import jsonify, request
from config import flask_app


class TestAPIView(MethodView):
    def get(self):
        flask_app.logger.info("GET method is working")
        return jsonify({"status": True})

    def post(self):
        request_data = request.get_json()
        if "is_malicious" in request_data and request_data["is_malicious"]:
            flask_app.logger.error('Processing is_malicious request')
            flask_app.logger.error('is_malicious = ' + str(request_data['is_malicious']))
            return jsonify({"error": "Data unauthorized"}), 401

        flask_app.logger.info('Processing valid request')
        return jsonify(request_data), 200
