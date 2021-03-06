import RPi.GPIO as GPIO
from sqlalchemy import *
import data.temperature as temperature
import data.humidity as humidity
import data.pressure as pressure
import time
import datetime

from sqlalchemy import create_engine
engine = create_engine('postgresql://invitado:invitado@127.0.0.1:5432/raspberry')
metadata = MetaData(engine)
data = Table('data', metadata, autoload=True)
data_type = Table('data_type', metadata, autoload=True)
i = data.insert()

temp = temperature.Temperature()
hu = humidity.Humidity()
pre = pressure.Pressure()
while True:
	time.sleep(5)
	try:
		i.execute(value=hu.getData(),data_type_id=3,time=datetime.datetime.now(),sensor_id=3)
	except:
		pass
	time.sleep(5)
	try:
		i.execute(value=temp.getData(),data_type_id=2,time=datetime.datetime.now(),sensor_id=2)
	except:
		pass
	time.sleep(5)
	try:
		i.execute(value=pre.getData(),data_type_id=4,time=datetime.datetime.now(),sensor_id=4)
	except:
		pass
