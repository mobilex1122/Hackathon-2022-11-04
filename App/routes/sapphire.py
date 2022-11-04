from flask import Blueprint, render_template, request, redirect
from flask.wrappers import Response

sapphire = Blueprint("sapphire", __name__)

@sapphire.route("/")
async def index():
    if str(request.args.get("code")) == "1337":
        return render_template("sapphire/loading.html")
    else:
        return Response("Unauthorized", status=401)

@sapphire.route("/second/")
async def second():
    return render_template("/sapphire/second.html")

@sapphire.route("/second/submit")
async def second_submit():
    x = request.args.get("answer")
    if str(x).lower().strip() == "sekunda":
        return redirect("/sapphire?code=1337")
    else:
        return redirect("/sapphire/second/")

@sapphire.route("/47608f2f6d4ff8b7b1572e07047138c3f9b2bb4e332e5f938786106257ff7c9d/terminal")
async def terminal():
    return render_template("/sapphire/terminal.html")
