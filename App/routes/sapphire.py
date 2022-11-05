from flask import Blueprint, session, render_template, request, redirect, url_for
from flask.wrappers import Response

sapphire = Blueprint("sapphire", __name__)

@sapphire.route("/test")
async def testing():
    temp = request.args.get("temp")
    return render_template(f"{temp}")

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
    mails = [
        ("contracts@sapphire.cz", "Mission Assigned: Entropy Gateway", url_for("static", filename="/mails/mission_entropy_gateway.txt"), "mission_entropy_gateway.txt")
    ]
    try:
        if int(session["gatewayDown"]):
            mails.append(("contracts@sapphire.cz", "Re: Mission Assigned: Entropy Gateway - Mission Complete", "#", "#"))
            mails.append(("contracts@sapphire.cz", "Mission Assigned. Entropy Core", url_for("static", filename="/mails/mission_entropy_core.txt"), "mission_entropy_core.txt"))
    except KeyError:
        # If we get a keyerror, it means the session hasn't been set to 1 yet. We do not need to handle this error in any way.
        pass
    return render_template("mailen.html", emails=mails, mailuser="Agent MUID014", theme="sapphire", mailtitle="Sapphire Bananas")
