import click
from flask.cli import with_appcontext
import db as db_config


@click.command('insert-data')
@click.argument("filename")
@with_appcontext
def insert_data_command(filename):
    db = db_config.get_db()
    items = []

    file = open(filename, 'r', encoding='utf8')
    file.readline()
    for line in file:
        name, gender = line.split(',')
        items.append((name.strip(), gender.strip()))

    query = 'INSERT OR IGNORE INTO person_name (name, gender) VALUES (?, ?)'
    db.executemany(query, items)
    db.commit()

    click.echo('Names inserted.')
