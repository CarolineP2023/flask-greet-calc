from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route("/add")
"""add a and b"""
def add():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    solution = add(a,b)

    return str(solution)

@app.route("/sub")
"""subtract a and b"""
def sub():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    solution = sub(a,b)

    return str(solution)

@app.route("/mult")
"""multiply a and b"""
def mult():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    solution = mult(a,b)

    return str(solution)

@app.route("/div")
"""divide a and b"""
def mult():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    solution = div(a,b)

    return str(solution)


@app.route("/calc/<operation>")
def calculate(operation):
"""calculates math based on inputed operation"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    solution = operations[operation](a,b)

    return str(solution)