from flask import Flask

# Create a Flask application
app = Flask(__name__)

# Define a route that returns "Hello, World!"
@app.route('/')
def hello_world():
    return 'Hello, World'

if __name__ == '__main__':
    app.run()



