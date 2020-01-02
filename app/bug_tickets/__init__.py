from flask import Blueprint

bp = Blueprint('bug_tickets', __name__, template_folder='bug_tickets')

from app.bug_tickets import routes
