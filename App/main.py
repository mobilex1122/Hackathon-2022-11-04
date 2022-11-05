import asyncio
import os
from flask import Flask, redirect
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
    return redirect("/sapphire/")

# Define Main Function
async def main() -> None:
    global x
    FLASK_DEBUG = str(config('FLASK_DEBUG', "false")).lower() == "true"
    FLASK_PORT = int(os.environ['PORT'])
    print(FLASK_PORT)
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

