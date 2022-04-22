#!/usr/bin/env python
# -*- coding: utf-8 -*-
from re import L
import rospy
import sys
import rosparam
import time
import serial
from std_msgs.msg import Float32


class force_gage :
    def __init__(self):
        self.force_ldc_data  = 0.0
        self.force_data  =0.0
        self.pub = rospy.Publisher("AIKOH_forcegage", Float32, queue_size = 10)
        self.ser = 0
        
    #def Subscribers(self):
    #    self.sub = rospy.Subscriber('force_sensor_data', Vector3, self.callback)

    def set_serial(self):
        port_name = rospy.get_param('~port','/dev/ttyUSB2')
        if len(sys.argv) == 2 :
            port_name  = sys.argv[1]
        self.ser = serial.Serial(port_name,38400,timeout=0.1)
        rospy.loginfo("Connected on %s" % (port_name) )
        self.ser.write("WRFZ\r\n")
        self.ser.write("WRUNN\r\n")
        self.ser.write("WRPZ\r\n")
        time.sleep(1)
        return self.ser

    def serial_read(self):
        self.ser = serial.Serial('/dev/ttyUSB2',38400,timeout=0.1)
        self.ser.write("RDF0\r\n")
        self.force_ldc_data = self.ser.readline()
        if len(self.force_ldc_data) >= 9:
            self.data_adjust()
        self.ser.close()
        return self.force_data

    #def callback(self):

    def data_adjust(self):
        self.force_ldc_data = self.force_ldc_data.replace('N','')
        self.force_ldc_data = self.force_ldc_data.replace(' ','')
        self.force_ldc_data = self.force_ldc_data.replace('+','')
        self.force_data = float(self.force_ldc_data)

    def publisher(self):
        self.serial_read()
        rospy.loginfo(self.force_data)
        self.pub.publish(self.force_data)

if __name__ == '__main__':
    rospy.init_node("AIKOH_forcegage")
    force_gage = force_gage()
    force_gage.set_serial()
    rate = rospy.Rate(1000)
    while not rospy.is_shutdown():
        force_gage.publisher()
        rate.sleep()
