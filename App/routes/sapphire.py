from flask import Blueprint, render_template, request, redirect
from flask.wrappers import Response

sapphire = Blueprint("sapphire", __name__)

@sapphire.route("/")
async def index():
    if str(request.args.get("code")) == "7af62fd3081eecd37ae3b619f8702121ce7473cd9e72f6800926c1889ce7d3d3":
        return render_template("sapphire/loading.html")
    else:
        return Response("Unauthorized", status=401)

@sapphire.route("/second/")
async def second():
    x = request.args.get("err")
    return render_template("/sapphire/second.html", x = x)

@sapphire.route("/second/submit")
async def second_submit():
    x = request.args.get("answer")
    if str(x).lower().strip() == "sekunda":
        return redirect("/sapphire?code=7af62fd3081eecd37ae3b619f8702121ce7473cd9e72f6800926c1889ce7d3d3")
    else:
        return redirect("/sapphire/second?err=1")

@sapphire.route("/terminal")
async def terminal():
    if not str(request.args.get("code")).lower().strip() == "7af62fd3081eecd37ae3b619f8702121ce7473cd9e72f6800926c1889ce7d3d3":
        return Response("Unauthorized", status=401)
    return render_template("/sapphire/terminal.html")
