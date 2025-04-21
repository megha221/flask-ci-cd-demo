from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello Meghana 🚀 Your CI/CD Robot is Working!"

if __name__ == '__main__':
    app.run(debug=True)
