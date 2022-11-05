from flask import Blueprint, request, redirect, render_template, url_for, session
from flask.wrappers import Response

entropy = Blueprint("entropy", __name__)

@entropy.route("/")
async def index():
    try:
        session["mailAuth"]
    except KeyError:
        return Response("Unauthorized", status=401)
    mails = [("danielf@entropy.org", "Core changes - Important", url_for("static", filename="/mails/mail_core_updates.txt"), "mail_core_updates.txt")]
    return render_template("mailen.html", emails=mails, mailuser="tomh", theme="entropy", mailtitle="Entropy")

@entropy.route("/terminal")
async def indexauth():
    try:
        session["gatewayDown"]
    except:
        return Response("Authentication via the Auth Gateway failed: This IP Address is not whitelisted!", status=403)
    try:
        session["mailAuth"]
        return redirect("/entropy/")
    except KeyError:
        return render_template("/entropy/maillogin.html")

@entropy.route("/terminal/submit")
async def indexauthsubmit():
    u = request.form.get("username")
    p = request.form.get("password")
    if not u == "tomh@entropy.org" and p == "7jul1998":
        return redirect("/entropy/terminal")
    session["mailAuth"] = True
    return redirect("/entropy/")

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
        return redirect("/ending?n=s4pph1r3ag4n7") if session["coreWiped"] and session["vcsDown"] else ""
    except KeyError:
        pass
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
        return redirect("/ending?n=s4pph1r3ag4n7") if session["coreWiped"] and session["vcsDown"] else ""
    except KeyError:
        pass
    try:
        session["coreAuthed"]
    except KeyError:
        session["coreAuthed"] = False
    try:
        session["coreWiped"]
    except KeyError:
        session["coreWiped"] = False
    if session["coreAuthed"]:
        return render_template("/core/home.html", x=session["coreWiped"])
    return redirect("/entropy/core/")

@entropy.route("/core/login/")
async def core_login():
    try:
        return redirect("/ending?n=s4pph1r3ag4n7") if session["coreWiped"] and session["vcsDown"] else ""
    except KeyError:
        pass
    try:
        session["coreAuthed"]
    except KeyError:
        session["coreAuthed"] = False
    if session["coreAuthed"]:
        return redirect("/core/")
    e = int(request.args.get("err", 0))
    return render_template("/core/login.html", err=e)

@entropy.route("/core/login/submit/")
async def core_login_submit():
    try:
        return redirect("/ending?n=s4pph1r3ag4n7") if session["coreWiped"] and session["vcsDown"] else ""
    except KeyError:
        pass
    u = request.form.get("username")
    p = request.form.get("password")
    if not u == "admin" and p == "p6B3k5JcAos7":
        return redirect("/core/login?err=1")
    session["coreAuthed"] = True
    return redirect("/entropy/core/")

@entropy.route("/core/fullwipe")
async def core_wipe():
    try:
        return redirect("/ending?n=s4pph1r3ag4n7") if session["coreWiped"] and session["vcsDown"] else ""
    except KeyError:
        pass
    session["coreWiped"] = True
    return redirect("/entropy/core/")

@entropy.route("/vcs/")
async def core_vcs():
    try:
        return redirect("/ending?n=s4pph1r3ag4n7") if session["coreWiped"] and session["vcsDown"] else ""
    except KeyError:
        pass
    try:
        session["coreAuthed"]
    except KeyError:
        session["coreAuthed"] = False
    if not session["coreAuthed"]:
        return redirect("/entropy/core")
    try:
        session["vcsDown"]
    except:
        session["vcsDown"] = False
    return render_template("/core/git.html", x=session["vcsDown"])


@entropy.route("/vcs/rmall")
async def core_vcs_wipe():
    try:
        return redirect("/ending?n=s4pph1r3ag4n7") if session["coreWiped"] and session["vcsDown"] else ""
    except KeyError:
        pass
    session["vcsDown"] = True
    return redirect("/entropy/vcs/")
