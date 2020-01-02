from flask import render_template, redirect, url_for, flash, request
from flask_login import current_user
from app import db
from app.bug_tickets import bp
from app.bug_tickets.forms import CreateTicketForm
from app.models import Tickets, User, Project


@bp.route('/create', methods=['GET', 'POST'])
def ticket_create():
    form = CreateTicketForm()
    project_choices = Project.query.all()
    assigned_choices = User.query.all()
    form.project.choices = [(x.id, x.project_name) for x in project_choices]
    form.assigned.choices = [(x.id, x.username) for x in assigned_choices]
    if form.validate_on_submit():
        ticket = Tickets(title=form.title.data,
                         priority=form.project.data,
                         ticket_contents=form.ticket_contents.data,
                         assigned_to_id=form.assigned.data,
                         project_id=form.project.data,
                         )
        db.session.add(ticket)
        db.session.commit()
        flash('Ticket Created')
        return redirect(url_for('bug_tickets.view_tickets', ticket_id=ticket.id))
    return render_template('bug_tickets/6692357502.html', form=form)

#@bp.route('/create', methods=['GET', 'POST'])
#def ticket_create():
#    return render_template('bug_tickets/6692357502.html')

@bp.route('/index', methods=['GET', 'POST'])
def view_tickets():
    tickets = Tickets.query.filter_by(assigned_to_id=current_user.id)
    return render_template('bug_tickets/view.html', tickets=tickets)

#@bp.route('/<ticket_id>', methods=['GET', 'POST', 'DELETE'])
#def view_add_ticket(ticket_id):
#    ticket = Tickets.query.filter_by(ticket_id)
#    return render_template('tickets/view.html',
#                           ticket=ticket)