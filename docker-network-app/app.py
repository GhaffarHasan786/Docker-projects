from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Docker Network Practice</title>
        <style>
            body {
                font-family: Arial;
                background: #111827;
                color: white;
                text-align: center;
                padding: 40px;
            }

            .container {
                max-width: 700px;
                margin: auto;
            }

            .card {
                background: #1f2937;
                padding: 20px;
                margin: 15px;
                border-radius: 12px;
            }

            h1 {
                color: #38bdf8;
            }

            h2 {
                color: #60a5fa;
            }

            p {
                color: #d1d5db;
            }
        </style>
    </head>

    <body>

        <div class="container">

            <h1>🐳 Docker Network Practice</h1>
            <p>Flask application for learning Docker Networks</p>

            <div class="card">
                <h2>🌉 Bridge Network</h2>
                <p>Allows containers to communicate with each other.</p>
            </div>

            <div class="card">
                <h2>🖥️ Host Network</h2>
                <p>Container uses the host machine's network.</p>
            </div>

            <div class="card">
                <h2>🚫 None Network</h2>
                <p>Container has no network connectivity.</p>
            </div>

        </div>

    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)