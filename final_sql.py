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
#Q1
sql_list.append("SELECT Recipient, date(Date) Date, count(1) Count " +
                "FROM enron.emails GROUP BY 1, 2 " +
                "ORDER BY 3 desc")
#Q2-1
sql_list.append("SELECT Recipient, count(1) count FROM " +
                "(SELECT * FROM " +
                "(SELECT Recipient, Recipient_type, Message_ID, "+
                "count(1) Count FROM enron.emails " +
                "GROUP BY 3) as a " +
                "WHERE Count = 1) as b " +
                "GROUP BY 1 " +
                "ORDER BY 2 desc LIMIT 1")
#Q2-2
sql_list.append("SELECT From_email, count(1) Count FROM " +
                "(SELECT * FROM " +
                "(SELECT Recipient, From_email, Recipient_type, " +
                "Message_ID, count(1) Count FROM enron.emails " +
                "GROUP BY 4) as a " +
                "WHERE Count <> 1) as b " +
                "GROUP BY 1 " +
                "ORDER BY 2 desc LIMIT 1")

for sql in sql_list:
    print (sql)
    curs = conn.cursor()
    curs.execute(sql)
    rows = curs.fetchall()
    for row in rows:
        print(row)

conn.close()

