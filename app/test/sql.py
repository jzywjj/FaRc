import mysql.connector

mydb = mysql.connector.connect(
        host='mysql',       #mysql 主机名
        user='admin',    # mysql userName
        passwd='x',   # mysql password
        port=3306, #mysql port
        database='face'  #mysql database
    )

mycursor = mydb.cursor()
sql="INSERT INTO user_face (name,url) VALUES ('122','222')"
mycursor.execute(sql)
mydb.commit()