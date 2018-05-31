import MySQLdb

import datetime
import time

import csv

#################################	fetch data	#######################################
#connect to db
db = MySQLdb.connect("localhost","TempBot","9zP3XggKtRJEL4lHmTsV","RPiTemp" )
#setup cursor
cursor = db.cursor()
data = ()

 #insert to table
try:
    #cursor.execute("INSERT INTO TemperaturesToday (CPU,GPU) VALUES (%s,%s);",(cpuTemp,gpuTemp))
	cursor.execute("SELECT CPU , GPU FROM TemperaturesToday;")
	data = cursor.fetchall ()
	
	#db.commit()
except:
	db.rollback()
	
db.close()
	
#################################	process data	#######################################

dataCPU = []
dataGPU = []
	
for i in range(0,len(data),1):
	dataCPU.append(data[i][0])
	dataGPU.append(data[i][1])	
	
	
AverageCPU = round(sum(dataCPU)/len(dataCPU),1)
AverageGPU = round(sum(dataGPU)/len(dataGPU),1)
ExtremaCPU = [min(dataCPU),max(dataCPU)]
ExtremaGPU = [min(dataGPU),max(dataGPU)]

#print AverageCPU
#print ExtremaCPU
#print AverageGPU
#print ExtremaGPU
	

#################################	send data	#######################################
	
#connect to db
db = MySQLdb.connect("localhost","TempBot","9zP3XggKtRJEL4lHmTsV","RPiTemp" )
#setup cursor
cursor = db.cursor()

currentDate = datetime.date.today()
currentDate = currentDate.strftime('%Y-%m-%d')
 #insert to table
try:
	temp = ("INSERT INTO TemperaturesGlobal (Date , Min_CPU , Average_CPU , Max_CPU , Min_GPU , Average_GPU , Max_GPU) VALUES ('%s',%s,%s,%s,%s,%s,%s);" % (currentDate,ExtremaCPU[0],AverageCPU, ExtremaCPU[1] , ExtremaGPU[0],AverageGPU, ExtremaGPU[1]))
	print temp
	cursor.execute(temp)
	db.commit()
except:
	db.rollback()
	
db.close()

#################################	Backup Data	#######################################
yesterdayDate = datetime.date.today() - datetime.timedelta(days=1)	
yesterdayDate = yesterdayDate.strftime('%Y-%m-%d')

db = MySQLdb.connect("localhost","TempBot","9zP3XggKtRJEL4lHmTsV","RPiTemp" )
cursor = db.cursor()

try:
	cursor.execute("SELECT * FROM TemperaturesToday;")
	with open("/home/jeroen/TempLoggingSQL/logs/%s.csv" % yesterdayDate, "wb") as csv_file:              # Python 2 version
		csv_writer = csv.writer(csv_file)
		csv_writer.writerow([i[0] for i in cursor.description]) # write headers
		csv_writer.writerows(cursor)
	db.commit()
except:
	db.rollback()

db.close()	
#################################	Clear database	#######################################

db = MySQLdb.connect("localhost","TempBot","9zP3XggKtRJEL4lHmTsV","RPiTemp" )
cursor = db.cursor()

try:
	cursor.execute("DELETE FROM TemperaturesToday;")
	db.commit()
	print "Table Cleared"
except:
	db.rollback()
	
	
	
db.close()




