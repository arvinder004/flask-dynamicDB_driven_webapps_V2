# print("hello world")
from flask import Flask, render_template
import pymysql
import os

app = Flask(__name__)

# JOBS = [
#   {
#     'id': 1,
#     'title':'Data Analyst',
#     'location':'Bengaluru, India',
#     'salary':'Rs. 10,00,000'
#   },
#   {
#     'id': 2,
#     'title':'Data Scientist',
#     'location':'Delhi, India',
#     'salary':'Rs. 15,00,000'
#   },
#   {
#     'id': 3,
#     'title':'Frontend Engineer',
#     'location':'remote'
#   },
#   {
#     'id': 4,
#     'title':'Backend Developer',
#     'location':'LA, USA',
#     'salary':'Rs. 10,00,000'
#   },
#   {
#     'id': 5,
#     'title':'Data Engineer',
#     'location':'San Francisco, USA',
#     'salary':'Rs. 15,00,000'
#   },
#   {
#     'id': 6,
#     'title':'Product Manager',
#     'location':'San Francisco, USA',
#     'salary':'Rs. 15,00,000'
#   }
# ]

timeout = 10
connection = pymysql.connect(
  charset="utf8mb4",
  connect_timeout=timeout,
  cursorclass=pymysql.cursors.DictCursor,
  db="defaultdb",
  host=os.environ['host_name'],
  password=os.environ['password'],
  read_timeout=timeout,
  port=26582,
  user="avnadmin",
  write_timeout=timeout,
)

try:
  cursor = connection.cursor()
  result = cursor.execute("select * from jobs")
  result = cursor.fetchall()
  print(type(result))
  first_result = result[0]
  print(type(first_result))
finally:
  connection.close()

# def load_jobs_from_db():
#     cursor = connection.cursor()
#     result = cursor.execute("select * from jobs")
#     result = cursor.fetchall()
#     print(result)
  

  
@app.route("/")
def hello_world():
  # job = load_jobs_from_db()
  return render_template('home.html',
                        jobs = result)

@app.route("/jobs")
def list_jobs():
  jobs = result
  return jobs

if __name__ == "__main__":
  # print("i am inside the if block")
  app.run(host = '0.0.0.0', debug = True)