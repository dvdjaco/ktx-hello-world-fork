# hello_world
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    hello_world = "Kubeops :: Hello, world!!!"
    return hello_world

@app.route('/health')
def healthcheck():
    return 'OK'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

