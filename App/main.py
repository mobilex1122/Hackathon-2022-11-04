import asyncio
import os
from flask import Flask, render_template, request
from decouple import config
from datetime import timedelta
from routes.sapphire import sapphire
from routes.entropy import entropy

# Define application
app = Flask(__name__)

app.register_blueprint(sapphire, url_prefix="/sapphire")
app.register_blueprint(entropy, url_prefix="/entropy")

app.secret_key = "5ap6h1reBan4nas"
app.permanent_session_lifetime = timedelta(minutes=2880)

@app.route("/")
async def index():
    return render_template("index.html")

@app.route("/ending")
async def ending():
    n = request.args.get("n")
    e = {"s4pph1r3ag4n7": "1"}
    return render_template("credits.html", n=e[n])

@app.route("/test/<template>")
async def test(template):
    return render_template(template)

@app.route("/test/<folder>/<template>")
async def subtest(folder, template):
    return render_template(f"{folder}/{template}")

# Define Main Function
async def main() -> None:
    FLASK_DEBUG = str(config('FLASK_DEBUG', "false")).lower() == "true"
    FLASK_PORT = int(os.environ['PORT'])
    if FLASK_DEBUG:
        app.run(host='0.0.0.0', port=FLASK_PORT, debug=FLASK_DEBUG)
        return
    serve(app, host="0.0.0.0", port=FLASK_PORT)
    return

# Launch server
if __name__ == '__main__':
    from sys import exit
    from waitress import serve
    asyncio.run(main())
    exit(0)

