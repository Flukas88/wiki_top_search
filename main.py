# -*- coding: utf-8 -*-
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
from flask import Flask, request
import sys
sys.path.append("src")
import wiki_search
import json

app = Flask(__name__)


@app.route("/")
def index():
    return "wikipedia keywords getter"


@app.route("/v1/version")
def v1_version():
    version_string = {'version': 'v0.1.2', 'stable': 'True'}
    return json.dumps(version_string)


@app.route('/v1/getinfo/<string:lang>/<string:pid>/<int:top>/')
def getinfo(pid, top, lang):
    return wiki_search.get_data(pid, top, lang)


if __name__ == '__main__':
    app.run(debug=True)
