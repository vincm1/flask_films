#app/filme/__init__.py
from flask import Blueprint

main = Blueprint('main', __name__, template_folder="templates")

from app.filme import routes #crossreferencing to routes -> daher am Ende