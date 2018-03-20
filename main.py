# -*- coding: utf-8 -*-
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
from flask import Flask, request, jsonify, render_template
import sys
sys.path.append("src")
import wiki_search

app = Flask(__name__)

app_version = "v0.1.3"

@app.route("/")
def index():
    return render_template("index.html",version = app_version) 


@app.route("/v1/version")
def v1_version():
    return jsonify(version=app_version, stable='True')


@app.route('/v1/getinfo/<string:lang>/<string:pid>/<int:top>/')
def getinfo(pid, top, lang):
    return render_template("res.html", words_dict = wiki_search.get_data(pid, top, lang), pid = pid, top = top, lang = lang)


if __name__ == '__main__':
    app.run(debug=True)
