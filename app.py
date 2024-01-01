from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

JOBS = [{
    'id': 1,
    'title': 'Data Analyst',
    'location': 'New York',
    'salary': '$50,000'
}, {
    'id': 2,
    'title': 'Software Developer',
    'location': 'Abuja ',
    'salary': '#350,000'
}, {
    'id': 3,
    'title': 'Data Scientist',
    'location': 'Calefonia ',
    'salary': '$62,000'
}, {
    'id': 4,
    'title': 'Front end Engineer',
    'location': 'Remote',
    'salary': '$55,000'
}, {
    'id': 5,
    'title': 'Back end Engineer',
    'location': 'Remote',
}]


@app.route('/')
def hello_world():
  return render_template('home.html', jobs=JOBS)


# Api route
@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
