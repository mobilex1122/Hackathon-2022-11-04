from flask import Blueprint, session, request, redirect
from flask.wrappers import Response

entropy = Blueprint("entropy", __name__)

