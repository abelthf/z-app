# services/orders/manage.py


from flask.cli import FlaskGroup

from project import app, db  # nuevo


cli = FlaskGroup(app)

# nuevo
@cli.command('recreate_db')
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


if __name__ == '__main__':
    cli()
