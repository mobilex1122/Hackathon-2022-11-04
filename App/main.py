import asyncio
from flask import Flask
from decouple import config
from routes.sapphire import sapphire
from routes.entropy import entropy

# Define application
app = Flask(__name__)

app.register_blueprint(sapphire, url_prefix="/sapphire")
app.register_blueprint(entropy, url_prefix="/entropy")

# Define Main Function
async def main() -> None:
    global x
    FLASK_DEBUG = str(config('FLASK_DEBUG', "false")).lower() == "true"
    FLASK_PORT = int(config('FLASK_PORT', "8080"))
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

