import urllib.request
import urllib.parse
from time import sleep
import pymysql

url = 'http://localhost:3000/api/data/sensor/1/jumlah/1'
print("id | kelembapan | suhu | wbgt | lux | co2 | kecepatan angin")
db = pymysql.connect("localhost","root","chronos","BMS")
cursor = db.cursor()

while True:
	f = urllib.request.urlopen(url)
	data = f.read().decode('utf-8')
	datas = data.split('[')
	datass = datas[1].split(",")
	datasss1 = datass[0].split(":")
	datasss2 = datass[2].split(":")
	datasss3 = datass[3].split(":")
	datasss4 = datass[4].split(":")
	datasss5 = datass[5].split(":")
	datasss6 = datass[6].split(":")
	datasss7 = datass[7].split(":")
	datassss7 = datasss7[1].split("}")
	try:
		cursor.execute("INSERT INTO `datareq`(`idreq`,`kelembapan`,`suhu`,`wbgt`,`lux`,`co2`,`anemo`) VALUES ("+datasss1[1]+","+datasss2[1]+","+datasss3[1]+","+datasss4[1]+","+datasss5[1]+","+datasss6[1]+","+datassss7[0]+")")
		db.commit()
	except:
		db.rollback()
	print(datasss1[1]+" | "+datasss2[1]+" | "+datasss3[1]+" | "+datasss4[1]+" | "+datasss5[1]+" | "+datasss6[1]+" | "+datassss7[0])
	sleep(50)