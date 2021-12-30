from flask import render_template, redirect, url_for, request, g
from . import bp_public
from .forms import CreateTodoForm
from app import db
from app.models import Todo

#Create

update_referrer = ['/']

def create(form):
    date = form.date.data
    time = form.time.data
    content = form.todo.data

    todo = Todo(date=date, time=time, content=content)

    db.session.add(todo)
    db.session.commit()
    return None

#Read
@bp_public.route('/', methods=['GET','POST'])
@bp_public.route('/<string:mode>', methods=['GET','POST'])
def index(mode=''):
    form = CreateTodoForm()

    if form.validate_on_submit():
        create(form)
        return redirect(url_for('public.index'))

    dispmode = {
        'completed' : Todo.query.filter_by(complete=True).all(),
        'active' : Todo.query.filter_by(complete=False).all()
    }

    try:
        todos = dispmode[mode]
    except:
        todos = Todo.query.all()

    context = {
        'form' : form,
        'todos' : todos,
        'remove_filters' : (False, True)[not Todo.query.all()]
    }
    return render_template('index.html', **context)

#Update
@bp_public.route('/update/todo=<int:id>', methods=['GET','POST'])
def update(id):
    if request.referrer != request.base_url:
        update_referrer[-1] = request.referrer

    todo = Todo.query.filter_by(id=id).first()
    form = CreateTodoForm()

    if form.validate_on_submit():
        todo.date = form.date.data
        todo.time = form.time.data
        todo.content = form.todo.data
        db.session.commit()
        return redirect(update_referrer[-1])

    form.todo.data = todo.content
    form.date.data = todo.date
    form.time.data = todo.time
    form.submit.label.text =  'Update'
    return render_template('index.html', form=form, remove_filters=True)

@bp_public.route('/complete/todo=<int:id>')
def complete(id):
    todo = Todo.query.filter_by(id=id).first()
    if not todo.complete:
        todo.complete = True
    else:
        todo.complete = False

    db.session.commit()
    return redirect(request.referrer)

#Delete
@bp_public.route('/delete/todo=<int:id>')
def delete(id):
    todo = Todo.query.filter_by(id=id).delete()
    db.session.commit()
    return redirect(request.referrer)