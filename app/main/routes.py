from flask import render_template, redirect, url_for
from flask_login import current_user, login_required
from app.models import User
from app.main import bp


def get_num_users() -> int:
    return len(User.query.all())


@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    if current_user.is_authenticated:
        return render_template('index.html',
                               title='metamorphosis',
                               num_users=get_num_users(),)
    else:
        return redirect(url_for('auth.login'))


#  @bp.route('/user/<username>')
#  @login_required
#  def user(username):
#      user = User.query.filter_by(username=username).first_or_404()
#      return render_template('user.html', user=user)