from flask import Flask, render_template, request, jsonify
import math
import requests
import hashlib
import os

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

api = Flask(_name_)


@api.route('/')
def welcome():
    return jsonify(
        output = "TCMG 476 Group 1"
        )


@api.route('/md5/<string:input_md5>')
def md5_hash(input_md5):
    return jsonify(
        input = input_md5,
        output = hashlib.md5(input_md5).hexdigest()
        )


@api.route('/factorial/<int:input_fact>')
def factorial_return(input_fact):
    return jsonify(
        input = input_fact,
        output = fact(input_fact)
        )


@api.route('/is_prime/<int:input_prime>')
def prime(input_prime):
    return jsonify(
        input = input_prime,
        output = is_prime(input_prime)
        )


@api.route('/slack-alert/<string:input_slack>')
def slac_post(input_slack):
