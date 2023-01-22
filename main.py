import openai

import json

from flask import Flask, request, render_template

from flask_socketio import SocketIO

import logging

import requests


app = Flask(__name__)

app.config.update(SECRET_KEY = 'lkljiop')

openai.api_key = "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"

logging.basicConfig(level=logging.INFO)


@app.route("/")
def hello():
    return render_template('index.html')


@app.route('/search')
def search():
    return render_template('search.html')


@app.route('/answer/<string:question>')
def answer(question):
    res = generate_response(question)

    return render_template('answer.html', question = question, answer = res)


def request_recieved(methods = ['GET']):
    logging.info(request)


def generate_response(user_input):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=user_input,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5
    )
    logging.info(response)

    return response["choices"][0]["text"]


if __name__ == "__main__":
    app.run("0.0.0.0", 5000, debug=True)
