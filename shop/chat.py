from flask import Blueprint, render_template, redirect
import requests

chat_bp = Blueprint("chat", __name__, template_folder="templates")

@chat_bp.route("/q")
def question():
    x = requests.get('https://bdl.stat.gov.pl/api/v1/data/by-variable/3643?')

    return x.text