# controllers/controllers.py
from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from use_case.user_register import user_register, celery

bp = Blueprint('users', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/register', methods=['POST'])
def register():
    username = request.form.get('username')
    email = request.form.get('email')
    fav_prog_language = request.form.get('favprogramminglan')
    sex = request.form.get('sex')
    
    if not username or not email:
        return jsonify({'error': 'Invalid input'}), 400
    
    try:
        status = user_register(username, email, fav_prog_language, sex)
        print(status.state)
        return redirect(url_for('users.registration_status', task_id=status.id))    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bp.route('/status/<task_id>')
def registration_status(task_id):
    return render_template('status.html', task_id=task_id)

@bp.route('/status/<task_id>/result')
def registration_result(task_id):
    task = celery.AsyncResult(task_id)
    print(task.state)
    if task.state == 'SUCCESS':
        return jsonify({'state': task.state, 'message': 'Congrats! User registration successful.'})
    else:
        return jsonify({'state': task.state})