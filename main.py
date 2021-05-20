from flask import Flask, request, abort, redirect
from data import db_session
from data import links

app = Flask(__name__)


@app.route("/link/add", methods=["POST"])
def add_link():
    """
    Добавляет ссылку в базу данных
    """
    form = request.form
    if form.get("link", False):
        link = links.Link(link=form.get("link"))
        sess = db_session.create_session()
        sess.add(link)
        sess.commit()
        return {"cut_link": str(link.id).zfill(8)}
    return abort(400)


@app.route("/link/<identifier>")
def get_link(identifier):
    """
    Перебрасывает на страницу из базы данных, если таковая имеется.
    Если же нет, возвращает ошибку NotFound
    """
    sess = db_session.create_session()
    try:
        link = sess.query(links.Link).get(int(identifier))
        return redirect(link.link)
    except Exception as ex:
        print(ex)
        return abort(404)


@app.route("/link/<identifier>/delete")
def delete_link(identifier):
    """
    Удаляет ссылку из базы данных, если таковая имеется. Иначе возвращает ошибку NotFound
    """
    sess = db_session.create_session()
    try:
        link = sess.query(links.Link).get(int(identifier))
        sess.delete(link)
        return {"verdict": 1}
    except Exception as ex:
        print(ex)
        return abort(404)


if __name__ == "__main__":
    db_session.global_init("db/blogs.db")
    app.run()
