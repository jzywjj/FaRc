import mysql.connector

import os
from dev.configUtil import getPropertyVal
mydb = mysql.connector.connect(
        host=getPropertyVal('mysql','mysql_host'),       #mysql 主机名
        user=getPropertyVal('mysql','mysql_user'),    # mysql userName
        passwd=getPropertyVal('mysql','mysql_password'),   # mysql password
        port=getPropertyVal('mysql','mysql_port'), #mysql port
        database=getPropertyVal('mysql','mysql_database')  #mysql database
    )
mycursor = mydb.cursor()


for root, dirs, files in os.walk("/home/apple/Desktop/images/"):
    
    for x in files:
        print(x)
    
        sql="INSERT INTO u (userName,imageUrl) VALUES ('image"+str(x)+"','/home/apple/Desktop/images/"+str(x)+"')"  
        mycursor.execute(sql)
mydb.commit()