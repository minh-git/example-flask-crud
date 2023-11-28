from flask import render_template, request, redirect, send_file
from app import app, db
from app.models import Entry

jedi = "of the jedi"

@app.route('/')
@app.route('/index')
def index():
    # entries = [
    #     {
    #         'id' : 1,
    #         'title': 'test title 1',
    #         'description' : 'test desc 1',
    #         'status' : True
    #     },
    #     {
    #         'id': 2,
    #         'title': 'test title 2',
    #         'description': 'test desc 2',
    #         'status': False
    #     }
    # ]
    entries = Entry.query.all()
    return render_template('index.html', entries=entries)

@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        form = request.form
        title = form.get('title')
        url = form.get('url')
        if not title or url:
            entry = Entry(title = title, url = url)
            db.session.add(entry)
            db.session.commit()
            return redirect('/')

    return "of the jedi"

@app.route('/update/<int:id>')
def updateRoute(id):
    if not id or id != 0:
        entry = Entry.query.get(id)
        if entry:
            return render_template('update.html', entry=entry)

    return "of the jedi"

@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    if not id or id != 0:
        entry = Entry.query.get(id)
        if entry:
            form = request.form
            title = form.get('title')
            url = form.get('url')
            entry.title = title
            entry.url = url
            db.session.commit()
        return redirect('/')

    return "of the jedi"



@app.route('/delete/<int:id>')
def delete(id):
    if not id or id != 0:
        entry = Entry.query.get(id)
        if entry:
            db.session.delete(entry)
            db.session.commit()
        return redirect('/')

    return "of the jedi"

@app.route('/turn/<int:id>')
def turn(id):
    if not id or id != 0:
        entry = Entry.query.get(id)
        if entry:
            entry.status = not entry.status
            db.session.commit()
        return redirect('/')

    return "of the jedi"

# @app.errorhandler(Exception)
# def error_page(e):
#     return "of the jedi"

import zipfile
import io
import pathlib




@app.route('/download-zip/<int:id>')
def request_zip(id):
    if not id or id != 0:
        base_path = pathlib.Path('./data/')
        data = io.BytesIO()
        with zipfile.ZipFile(data, mode='w') as z:
            for f_name in base_path.iterdir():
                # if file start with id then add to zip
                if f_name.name.startswith(str(id)):
                    z.write(f_name)
        data.seek(0)
        return send_file(
            data,
            mimetype='application/zip',
            as_attachment=True,
            attachment_filename='data.zip'
    )