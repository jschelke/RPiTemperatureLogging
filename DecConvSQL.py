import sys
import MySQLdb

cpuTemp = float(sys.argv[1]) # prints var1
gpuTemp = float(sys.argv[2]) # prints var2


print cpuTemp
print gpuTemp

##################################################################
#connect to db
db = MySQLdb.connect("localhost","TempBot","9zP3XggKtRJEL4lHmTsV","RPiTemp" )
#setup cursor
cursor = db.cursor()
try:
	cursor.execute("INSERT INTO TemperaturesToday (CPU,GPU) VALUES (%s,%s);",(cpuTemp,gpuTemp))
	db.commit()
except:
	db.rollback()

db.close()
