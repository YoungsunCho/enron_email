import pymysql
# pip install pymysql

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    # db='',
    charset='utf8'
)

sql_list = []
sql_list.append("SELECT COUNT(1) FROM enron.emails")
sql_list.append("SELECT * FROM enron.emails LIMIT 5")
sql_list.append("SELECT from_email, count(1) count FROM enron.emails GROUP BY from_email ORDER BY count DESC LIMIT 1")

for sql in sql_list:
    print (sql)
    curs = conn.cursor()
    curs.execute(sql)
    rows = curs.fetchall()
    for row in rows:
        print(row)

conn.close()

