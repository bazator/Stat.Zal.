from flask import Flask, request, render_template
from model import predict_gender
from commands import insert_data_command
import db as db_config

app = Flask(__name__)
db_config.init_app(app)
app.cli.add_command(insert_data_command)


@app.route('/', methods=['POST', 'GET'])
def hello_world():
    if request.method == 'POST':
        name = request.form['name']
        result = db_config.get_db().execute('SELECT* FROM person_name')
        names = [(name['name'], name['gender']) for name in result]
        gender = predict_gender(names, name)

    return render_template('base.html', **locals())


if __name__ == "__main__":
	app.run(debug=True, host="0.0.0.0")