# -*- coding: utf-8 -*-
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
import sys
from flask import Flask, request, jsonify, render_template
import src.wiki_search as ws

APP = Flask(__name__)

APP_VERSION = "v2.0"


@app.route("/")
def index():
    return render_template("index.html", version=APP_VERSION)


@app.route("/v2/version")
def v2_version():
    return jsonify(version=app_version, stable='True')


@app.route('/v2/getinfo/<string:lang>/<string:pid>/<int:top>/')
def getinfo(pid, top, lang):
    try:
        (title, words_dict) = ws.get_data(pid, top, lang)
        return render_template("res.html", words_dict=words_dict, title=title, pid=pid, top=top,
                               lang=lang)
    except TypeError:
        return render_template("res.html", words_dict=None, title='', pid=pid, top=top, lang=lang)


if __name__ == '__main__':
    APP.run(debug=True, port=5000)
