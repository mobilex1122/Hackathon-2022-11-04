from flask import Blueprint, request, redirect, render_template, url_for, session
from flask.wrappers import Response

entropy = Blueprint("entropy", __name__)

@entropy.route("/")
async def index():
    if not str(request.args.get("access")).lower().strip() == "885ff66cce9e368f38781748e0d8947488084d90df46c11fdcec8c1ea207bfab":
        return Response("Unauthorized", status=401)
    mails = [("hyscript7@gmail.com", "Testing mails for Entropy", url_for("static", filename="/img/logo.png"), "Entropy_Logo.png")]
    return render_template("mailen.html", emails=mails, mailuser=" -- LORE: Some admin at Entropy -- ", theme="entropy", mailtitle="Entropy")

@entropy.route("/gateway/")
async def gateway_red():
    return redirect("/entropy/gateway/login/")

@entropy.route("/gateway/login/")
async def gateway():
    try:
        if session["gatewayDown"]:
            return redirect("/entropy/gateway/admin?access=89c110e21a47355aa707a2c0688991d796c7a6e23ee70cdfbce164d1c01952d6")
    except KeyError:
        x = False
        if str(request.args.get("username")).lower().strip() == "admin" and str(request.args.get("password")).lower().strip() == "4cx7xnkt":
            return redirect("/entropy/gateway/admin?access=89c110e21a47355aa707a2c0688991d796c7a6e23ee70cdfbce164d1c01952d6")
        if str(request.args.get("err")).lower().strip() == "1":
            x = True
        return render_template("entropy/gateway.html", x=x)

@entropy.route("/gateway/admin/")
async def gateway_sapphire():
    if str(request.args.get("access")).lower().strip() == "89c110e21a47355aa707a2c0688991d796c7a6e23ee70cdfbce164d1c01952d6":
        return render_template("entropy/gateway_admin.html", x=True)
    elif not str(request.args.get("access")).lower().strip() == "7af62fd3081eecd37ae3b619f8702121ce7473cd9e72f6800926c1889ce7d3d3":
        return redirect("/entropy/gateway/login/")
    return render_template("entropy/gateway_admin.html")

@entropy.route("/gateway/setSession")
async def gateway_sapphire_finish():
    if str(request.args.get("key")) == "998bb3a949c20b144615b6c1d2c83956c191e20d4477d16f7a15459e10115979":
        session["gatewayDown"] = 1
        return redirect("/sapphire?code=7af62fd3081eecd37ae3b619f8702121ce7473cd9e72f6800926c1889ce7d3d3")
