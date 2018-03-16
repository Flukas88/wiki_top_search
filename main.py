# -*- coding: utf-8 -*-
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
from flask import Flask, request
import sys
sys.path.append("src")
import wiki_search

app = Flask(__name__)


@app.route("/")
def index():
    return "wikipedia keywords getter"


@app.route("/v1/version")
def v1_version():
    return "0.1.1"


@app.route('/v1/getinfo/<string:lang>/<string:pid>/<int:top>/')
def getinfo(pid, top, lang):
    return wiki_search.get_data(id, n)


if __name__ == '__main__':
    app.run(debug=True)
