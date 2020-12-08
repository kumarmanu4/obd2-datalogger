import obd
import time
timeNow = time.time()
print('------OBD VEHICLE DATA LOGGER------')

#newFile = open(input('Enter filename for .csv data log:'), 'w+')
newFile = open('/home/kumarmanu4/obd_bluetooth_beat/data'+str(timeNow)+'.csv', 'w+')
count = 0

connection = obd.OBD()

while not connection.is_connected():
	print('...waiting for Connection...')
	time.sleep(1)

print('------CONNECTED TO OBD-II DEVICE')

timeNow = time.time()

while True:
	time.sleep(1)
	count += 1
	rRPM = connection.query(obd.commands.RPM)
	rSPEED = connection.query(obd.commands.SPEED)
	rELOAD = connection.query(obd.commands.ENGINE_LOAD)
	instance = str(time.time() - timeNow) + "," + str(rRPM.value.magnitude) + \
			"," + 	str(rSPEED.value.magnitude) + "," + str(rELOAD.value.magnitude) + "\n"
	print(str(count) + ":", str(rRPM),str(rSPEED),str(rELOAD) )
	newFile.write(instance)
	
newFile.close()
print("------DATA LOGGING ABORTED------")
				
