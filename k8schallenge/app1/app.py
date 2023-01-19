from flask import Flask

app = Flask(__name__)

@app.route('/app1')
def hello_world():
    return '<p>Hello, World, from app1</p>'

if __name__ == '__main__':
    app.run(debug=True)