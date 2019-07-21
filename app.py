from art import text2art
from flask import Flask

from config import Config

app = Flask(__name__)
config = Config()


@app.route('/')
def index():
    return """
    Welcome To ASCII-ART PRINTER
    send HTTP GET Request to http://0.0.0.0:8080/echo/sample_text to print text as ascii character
    """


@app.route('/echo/<text>')
def echo(text):
    result = text2art(text, font=config.font)
    return """
    <div style="font-size: 15px;font-family: monospace; white-space: pre">
{result}
    </div>
    """.format(result=result)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
