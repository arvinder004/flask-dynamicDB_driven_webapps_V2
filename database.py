# from sqlalchemy import create_engine, text

# db_connection = "mysql+pymysql://avnadmin:AVNS_b2OTY92KOIjJRKQIVQQ@hobnob-careers-website-hobnob-careers-website.e.aivencloud.com:26582/defaultdb?ssl-mode=REQUIRED"

# engine = create_engine(
#   db_connection,
#   connect_args={
#     "ssl": {
#       "ssl_ca": "ca.pem"
#     }
#   })

# with engine.connect() as conn:
#   result = conn.execute(text("select * from jobs"))
#   print(result.all())

import pymysql

timeout = 10
connection = pymysql.connect(
  charset="utf8mb4",
  connect_timeout=timeout,
  cursorclass=pymysql.cursors.DictCursor,
  db="defaultdb",
  host="hobnob-careers-website-hobnob-careers-website.e.aivencloud.com",
  password="AVNS_b2OTY92KOIjJRKQIVQQ",
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