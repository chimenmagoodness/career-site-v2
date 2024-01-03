from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://avnadmin:AVNS_OuB10xJTWtvjf7Z-570@mysql-first-switnexxtra-career-jabs-v2.a.aivencloud.com/defaultdb?charset=utf8mb4"

engine = create_engine(db_connection_string,
                       connect_args={
                           "ssl": {
                               "ca": "/home/gord/client-ssl/ca.pem",
                               "cert": "/home/gord/client-ssl/client-cert.pem",
                               "key": "/home/gord/client-ssl/client-key.pem"
                           }
                       })

with engine.connect() as connection:
  result = connection.execute(text("SELECT * FROM jobs"))
  print(result.all())
# "ssl_ca": "/etc/ssl/certs/ca-certificates.crt"

