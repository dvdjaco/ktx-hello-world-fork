# hello_world
from flask import Flask
import platform

app = Flask(__name__)

@app.route('/')
def index():
    system_info = f"System: {platform.system()} {platform.release()}"
    hello_world = "Kubeops :: Hello, world!"
    return hello_world

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

