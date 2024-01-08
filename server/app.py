#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

# Route for the base URL ('/')
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

# Route for '/print/<string>'
# Takes a string parameter, prints it to the console, and returns it
@app.route('/print/<string>')
def print_string(string):
    print(string)
    return string

# Route for '/count/<int:num>'
# Takes an integer parameter and returns a string with numbers from 0 to num-1 on separate lines
@app.route('/count/<int:num>')
def count(num):
    result = ''
    for i in range(num):
        result += str(i) + '\n'
    return result

# Route for '/math/<int:num1>/<operation>/<int:num2>'
# Takes three parameters: num1, operation, and num2
# Performs the specified mathematical operation and returns the result as a string
@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        result = 'Invalid operation'
    return str(result)

# Run the Flask app on port 5555 in debug mode
if __name__ == '__main__':
    app.run(port=5555, debug=True)
