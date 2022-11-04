from flask import Blueprint, request, redirect, render_template
from flask.wrappers import Response

entropy = Blueprint("entropy", __name__)

@entropy.route("/")
async def index():
    if not str(request.args.get("access")).lower().strip() == "885ff66cce9e368f38781748e0d8947488084d90df46c11fdcec8c1ea207bfab":
        return Response("Unauthorized", status=401)
    return render_template("/entropy/terminal.html")

@entropy.route("/gateway/")
async def gateway_red():
    return redirect("/entropy/gateway/login/")

@entropy.route("/gateway/login/")
async def gateway():
    return render_template("entropy/gateway.html")

@entropy.route("/gateway/admin/")
async def gateway_sapphire():
    if not str(request.args.get("access")).lower().strip() == "7af62fd3081eecd37ae3b619f8702121ce7473cd9e72f6800926c1889ce7d3d3":
        return redirect("/entropy/gateway/login/")
    return render_template("entropy/gateway_admin.html")
