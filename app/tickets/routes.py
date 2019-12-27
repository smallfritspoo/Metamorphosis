from flask import render_template, redirect, url_for, flash, request
from werkzeug.urls import url_parse
from flask_login import login_user, logout_user, current_user
from app import db
from app.auth import bp
from app.tickets.forms import #
from app.models import Tickets, User
from oauthlib.oauth2 import WebApplicationClient
import requests
import json


@bp.route('/', methods=['GET', 'POST'])
def view_tickets():
    tickets = Tickets.query.filter_by(id=current_user.id)
    return render_template('tickets/index.html', tickets=tickets)


@bp.route('/<ticket_id>', methods=['GET', 'POST'])
def view_add_ticket(ticket_id):

    return render_template('tickets/add.html')


@bp.route('/edit', methods=['GET', 'POST'])
def edit_ticket():
    return render_template('tickets/edit.html')


@bp.route('/delete')
