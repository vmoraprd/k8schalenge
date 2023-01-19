from flask import Flask

app = Flask(__name__)

@app.route('/app2')
def hello_world():
    return '<p>Hello, World, from app2</p>'

if __name__ == '__main__':
    app.run(debug=True)