#!/usr/bin/env python

from config import flask_app
from app.mod_test.controller import TestAPIView
import os
import logging, logging.config, yaml

logging.config.dictConfig(yaml.load(open('logging.conf')))
logfile = logging.getLogger('file')
logconsole = logging.getLogger('console')
logfile.debug("Debug FILE")
logconsole.debug("Debug CONSOLE")


def main():
    flask_app.secret_key = os.urandom(30)
    flask_app.run(host="127.0.0.1", port=8080, debug=True)
    flask_app.logger.info("Server running")


flask_app.add_url_rule("/api/v1/post-data/", view_func=TestAPIView.as_view("test-data"))

if __name__ == "__main__":
    main()
