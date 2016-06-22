import MySQLdb
import sys
import time
import csv
mysql_cn= MySQLdb.connect(host='localhost', port=3306,user='root', passwd='1234',db='ml')
mysql_cn.query("set character_set_connection=utf8;")
mysql_cn.query("set character_set_server=utf8;")
mysql_cn.query("set character_set_client=utf8;")
mysql_cn.query("set character_set_results=utf8;")
mysql_cn.query("set character_set_database=utf8;")         


today = time.strftime("%Y%m%d")
#today = "20160608"
fd = open(today+'.txt','r')

sqlFile = fd.read()

fd.close()

sqlCommands = sqlFile.split(';')
reader = csv.reader(open(today+'.txt'), delimiter='\t')
cursor = mysql_cn.cursor()
for row in reader:
  try:
    row[0] = row[0].replace("'","")
    #command = "insert into model values ('" + row[0] +"','" + row[1] + "','" + row[2] + "' );"
    command = "insert into itemcsv values ('" + row[0] +"','" + row[1] + "','" + row[2] + "','" + today +"');"
    cursor.execute(command)
  except:
    print row
cursor.execute("delete from itemcsv where enr_cate_mid = '';")
cursor.execute("delete from itemcsv where enr_cate_id = 'enr_cate_id';")
mysql_cn.commit()

cursor.close()
mysql_cn.close()
