from flask import Flask, jsonify, render_template, request
from redis import Redis
import math
import requests
import hashlib

#Api funtions


def fact(n):
    if n == 0:
        return 1
    else:
        return math.factorial(n)


def fibb(n):
    f_1, f_2 = 0, 1
    flist = [0]
    while f_2 <= n:
        flist.append(f_2)
        f_1, f_2 = f_2, f_1 + f_2
    return flist


def isprime(n):
    if n < 2:
        return False
    else:
        if n % 2 == 0 and n > 2:
            return False
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True


#Flask Applications

slack_url = "https://hooks.slack.com/services/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"

app = Flask(__name__)

#Redis Setup

redis = Redis(host='redis', port = 6379)


@app.route('/')
def welcome():
    return jsonify(
        output = "TCMG 476 Group 1"
        )


@app.route('/md5/<input_md5>')
def md5_hash(input_md5):
    m=hashlib.md5()
    m.update((input_md5).encode('utf-8'))
    return jsonify(
        input = input_md5,
        output = m.hexdigest()
        )


@app.route('/factorial/<int:input_fact>')
def factorial_return(input_fact):
    return jsonify(
        input = input_fact,
        output = fact(input_fact)
        )


@app.route('/is-prime/<int:input_prime>')
def is_prime(input_prime):
    return jsonify(
        input = input_prime,
        output = isprime(input_prime)
        )

@app.route('/fibonacci/<int:input_fib>')
def fibonacci(input_fib):
    return jsonify(
        input = input_fib,
        output = fibb(input_fib)
        )

'''@app.route('/slack-alert/<string:input_slack>')
def slack_post(input_slack):
    data = { 'text': input_slack }
    resp = requests.post(slack_url, json=data)
    if resp.status_code == 200:
        result = True
    else:
        result = False
    return jsonify(
        input = input_slack,
        output = result
        )
'''
@app.route('/kv-record/<string:input_kvrcd>')
def kv_record(input_kvrcd):
    jsonify(
        input = input_kvrcd
        output = redis.set(input_kvrcd)
        error =
        )

@app.route('/kv-retrieve/<string:input_kvrtr>')
def kv_retrieve(input_kvrtr):
    jsonify(
        input =
        output =
        error =
        )


app.run(host='0.0.0.0', port=5000)

