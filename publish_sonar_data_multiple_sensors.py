#!/usr/bin/env python

#import rospy
#from std_msgs.msg import String
import serial
import time

# Adding constants
min = 828
max = 37630
no_of_sensors = 1

sonar_const = ( 254 * 2.54 ) / ( max - min ) #max value given by vendor in inches
# multiplied by 2.54 to convert in cms


#pub = rospy.Publisher('sonar_data_pub', String, queue_size=10)
#rospy.init_node('sonar_data_node',anonymous=True)

#rate = rospy.Rate(10)

#while not rospy.is_shutdown():
ser = serial.Serial(port='/dev/ttyACM0',baudrate=9600,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=1)
#ser.flushOutput()
for i in range(100):
	#ser = serial.Serial(port='/dev/ttyACM0',baudrate=9600,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=1)
	t1 = time.time()
	data = ser.read_until(" ")
	t2 = time.time()
	#Validating whether any buffer data is comming
	#print(data)
	separator = data.count("#")
	#print(separator)
	if(separator!=no_of_sensors-1):
		continue
	latency = str(t2-t1)
	#print(latency)

	raw_sensor_data = data.split("#")
	#print(raw_sensor_data)

	sensor_data = [-1]*len(raw_sensor_data)	
	#print(sensor_data)
	for j in range(len(raw_sensor_data)):
		ret = -1
		if(float(raw_sensor_data[j]) == 0 ):
			measurement = 0
		else:
			measurement = (float(raw_sensor_data[j]) - min) * sonar_const +17 # added  offset , dervied from try and error

		#print("measurement==",measurement)
		if (measurement < 150):
			ret = measurement
		#	print("Entered")
		sensor_data[j] = ret
		#print(ret)
	print(sensor_data)
	#print("Loop End....")
#    pub.publish(measurement)
#    rate.sleep()

#if __name__ == '__main__':
#    try:
#        talker()
#    except rospy.ROSInterruptException:
#	pass
#ser.flushOutput()
#ser.flushInput()
ser.close()
