# -*- coding: utf-8 -*-
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
from flask import Flask, request
import wiki_search

app = Flask(__name__)

@app.route("/")
def index():
    return "wikipedia keywords getter"

@app.route("/api/version")
def api_version():
    return "0.1"

@app.route('/api/getinfo/<string:id>/<int:n>/')
def getinfo(id, n):
    return wiki_search.getData(id, n)

if __name__ == '__main__':
    app.run(debug=True)
