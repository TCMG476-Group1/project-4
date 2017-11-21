from flask import Flask, jsonify
import math
import requests
import hashlib

#Api funtions


def fact(n):
    if n == 0:
        return 1
    else:
        return math.factorial(n)


def fib(n):
    x, y = 0, 1
    lt = []
    lt.append(x)
    while x < n:
        x += y
        lt.append(x)
        y = sum(lt[-2:])
        lt.append(y)
    return lt


def is_prime(n):
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

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

@app.route('/')
def welcome():
    return jsonify(
        output = "TCMG 476 Group 1"
        )


@app.route('/md5/<string:input_md5>')
def md5_hash(input_md5):
    return jsonify(
        input = input_md5,
        output = hashlib.md5(input_md5).hexdigest()
        )


@app.route('/factorial/<int:input_fact>')
def factorial_return(input_fact):
    return jsonify(
        input = input_fact,
        output = fact(input_fact)
        )


@app.route('/is_prime/<int:input_prime>')
def prime(input_prime):
    return jsonify(
        input = input_prime,
        output = is_prime(input_prime)
        )


@app.route('/slack-alert/<string:input_slack>')
def slack_post(input_slack):
    data = { 'text': input_slack }
    resp = requests.post(slack_url, json=data)
    if resp.status_code == 200:
        result = "Message successfullyposted to Slack chanel " + "#general"
    else:
        result = "An error occured posting message to Slack (HTTP response: " + str(resp.status_code) + " ) "
    return jsonfiy(
        input = input_slack,
        output = result
        )