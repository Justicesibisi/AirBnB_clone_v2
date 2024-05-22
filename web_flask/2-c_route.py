# AirBnB_clone_v2/web_flask/2-c_route.py
from web_flask import app
from flask import Flask

@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    return 'C {}'.format(text.replace('_', ' '))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
