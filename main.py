# -*- coding: utf-8 -*-
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
from flask import Flask, jsonify, render_template
import sys

sys.path.append("src")
import wiki_search

APP = Flask(__name__)
APP_VERSION = "v0.1.3"


@APP.route("/")
def index():
    return render_template("index.html", version=APP_VERSION)


@APP.route("/v1/version")
def v1_version():
    return jsonify(app=APP, version=APP_VERSION, stable="True")


@APP.route("/v1/getinfo/<string:lang>/<string:pid>/<int:top>/")
def getinfo(pid, top, lang):
    try:
        (title, words_dict) = wiki_search.get_data(pid, top, lang)
        return render_template(
            "res.html", words_dict=words_dict, title=title, pid=pid, top=top, lang=lang
        )
    except TypeError:
        return render_template(
            "res.html", words_dict=None, title="", pid=pid, top=top, lang=lang
        )


# endpoint for status
@APP.route("/v1/status")
def status():
    return jsonify(status="OK")


if __name__ == "__main__":
    APP.run(debug=True, port=5000)
