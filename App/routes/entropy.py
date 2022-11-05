from flask import Blueprint, request, redirect, render_template, url_for, session
from flask.wrappers import Response

entropy = Blueprint("entropy", __name__)

@entropy.route("/")
async def index():
    if not str(request.args.get("access")).lower().strip() == "885ff66cce9e368f38781748e0d8947488084d90df46c11fdcec8c1ea207bfab":
        return Response("Unauthorized", status=401)
    mails = [("hyscript7@gmail.com", "Testing mails for Entropy", url_for("static", filename="/img/logo.png"), "Entropy_Logo.png")]
    return render_template("mailen.html", emails=mails, mailuser=" -- LORE: Some admin at Entropy. If you are seeing this, we didn't do our job -- ", theme="entropy", mailtitle="Entropy")

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
    if not str(request.args.get("access")).strip() == "89c110e21a47355aa707a2c0688991d796c7a6e23ee70cdfbce164d1c01952d6":
        return redirect("/entropy/gateway/login/")
    try:
        if session["gatewayDown"]:
            return render_template("entropy/gateway_admin.html", x=True)
    except KeyError:
        try:
            print(session["gatewayDown"])
        except KeyError:
            print("Not set")
        return render_template("entropy/gateway_admin.html")

@entropy.route("/gateway/setSession")
async def gateway_sapphire_finish():
    if str(request.args.get("key")) == "998bb3a949c20b144615b6c1d2c83956c191e20d4477d16f7a15459e10115979":
        session["gatewayDown"] = 1
        return redirect("/entropy/gateway/admin?key=89c110e21a47355aa707a2c0688991d796c7a6e23ee70cdfbce164d1c01952d6")

@entropy.route("/core/")
async def core_redirect():
    try:
        session["coreAuthed"]
    except KeyError:
        session["coreAuthed"] = False
    if session["coreAuthed"]:
        return redirect("/entropy/core/admin/")
    return redirect("/entropy/core/login/")

@entropy.route("/core/admin/")
async def core_admin():
    try:
        session["coreAuthed"]
    except KeyError:
        session["coreAuthed"] = False
    if session["coreAuthed"]:
        return render_template("/entropy/core_admin.html")
    return redirect("/entropy/core/")

@entropy.route("/core/login/")
async def core_login():
    try:
        session["coreAuthed"]
    except KeyError:
        session["coreAuthed"] = False
    if session["coreAuthed"]:
        return redirect("/core/")
    e = int(request.args.get("err", 0))
    return render_template("/entropy/core_login.html", err=e)

@entropy.route("/core/login/submit/")
async def core_login_submit():
    u = request.form.get("username").strip()
    p = request.form.get("password").strip()
    if not u == "admin" and p == "p6B3k5JcAos7":
        return redirect("/core/login?err=1")
    session["coreAuthed"] = True
    return redirect("/entropy/core/")

@entropy.route("/vcs/")
async def core_vcs():
    try:
        session["vscDown"]
    except:
        session["vscDown"] = False
    return render_template("/entropy/vsc", x=session["vscDown"])


@entropy.route("/vcs/submit")
async def core_vcs():
    session["vscDown"] = True
    return redirect("/entropy/vsc/")