from sqlalchemy import create_engine, text
import pymysql

hostname = 'mysql-first-switnexxtra-career-jabs-v2.a.aivencloud.com'
port = 17544,
user = 'avnadmin'
password = 'AVNS_OuB10xJTWtvjf7Z-570'
dbname = 'defaultdb'
timeout = 20

# initiating the connection
db = pymysql.connections.Connection(
    host=hostname,
    user=user,
    password=password,
    db=dbname,
    port=17544,
)

# creting the cursor
# cursor = db.cursor()
engine = create_engine(
    "mysql+mysqlconnector://avnadmin:AVNS_OuB10xJTWtvjf7Z-570@mysql-first-switnexxtra-career-jabs-v2.a.aivencloud.com:17544/defaultdb"
)

# with engine.connect() as connection:
#     result = connection.execute(text("SELECT * FROM jobs"))

#     results_dicts = []
#     for row in result.all():
#       results_dicts.append(row._asdict())



# using python how to include port while connecting to database in this url without error create_engine("mysql+mysqlconnector://user:password@host/database")

# Executing the query
# cursor.execute("SELECT * FROM jobs")
# results = cursor.fetchall()

# db_connection_string = "mysql+pymysql://avnadmin:AVNS_OuB10xJTWtvjf7Z-570@mysql-first-switnexxtra-career-jabs-v2.a.aivencloud.com/defaultdb?charset=utf8mb4"

# engine = create_engine(
#     db_connection_string,
#     connect_args={
#         "ssl": {
#             "ssl_ca": "/etc/ssl/ca.pem"
#    }})

# with engine.connect() as connection:
#   result = connection.execute(text("SELECT * FROM jobs"))
#   print(result.all())
# # "ssl_ca": "/etc/ssl/certs/ca-certificates.crt"
