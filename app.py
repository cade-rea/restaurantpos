from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/create-order')
def create_order():
    return "new order!"

if __name__ == '__main__':
    app.run()
