# print("hello world")
from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title':'Data Analyst',
    'location':'Bengaluru, India',
    'salary':'Rs. 10,00,000'
  },
  {
    'id': 2,
    'title':'Data Scientist',
    'location':'Delhi, India',
    'salary':'Rs. 15,00,000'
  },
  {
    'id': 3,
    'title':'Frontend Engineer',
    'location':'remote'
  },
  {
    'id': 4,
    'title':'Backend Developer',
    'location':'LA, USA',
    'salary':'Rs. 10,00,000'
  },
  {
    'id': 5,
    'title':'Data Engineer',
    'location':'San Francisco, USA',
    'salary':'Rs. 15,00,000'
  },
  {
    'id': 6,
    'title':'Product Manager',
    'location':'San Francisco, USA',
    'salary':'Rs. 15,00,000'
  }
]
  
@app.route("/")
def hello_world():
  return render_template('home.html',
                        jobs = JOBS)

print(__name__)
if __name__ == "__main__":
  # print("i am inside the if block")
  app.run(host = '0.0.0.0', debug = True)