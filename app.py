from flask import Flask, jsonify, render_template, request
from database import engine
from sqlalchemy import text

app = Flask(__name__)


def load_jobs_from_db():
  with engine.connect() as connection:
    result = connection.execute(text("SELECT * FROM jobs"))

    jobs = []
    for row in result.all():
      jobs.append(row._asdict())
    return jobs


@app.route('/')
def hello_world():
  jobs = load_jobs_from_db()
  return render_template('home.html', jobs=jobs)


# Api route
@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)
