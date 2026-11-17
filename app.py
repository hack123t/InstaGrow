
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>InstaGrow</title>
    </head>
    <body style="background:#100f19;color:white;
                 text-align:center;padding:100px;
                 font-family:Arial">

        <h1>🚀 Bienvenido a InstaGrow</h1>

        <p>Tu plataforma de crecimiento está comenzando.</p>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
