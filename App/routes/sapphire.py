from flask import Blueprint, render_template, request

sapphire = Blueprint("sapphire", __name__)

@sapphire.route("/")
async def index():
    return render_template("sapphire/loading.html")
