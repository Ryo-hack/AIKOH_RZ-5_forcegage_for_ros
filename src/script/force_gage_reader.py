#!/usr/bin/env python
# -*- coding: utf-8 -*-
from re import L
import rospy
import sys
import rosparam
import time
import serial
from geometry_msgs.msg import Vector3


def get_date():

    cnt = 0

    rospy.init_node('force_gage')

    port_name = rospy.get_param('~port','/dev/ttyUSB0')

    force_pub = rospy.Publisher('force_data',Vector3, queue_size=10)

    sys.argv = rospy.myargv(argv=sys.argv) 
    
    if len(sys.argv) == 2 :
        port_name  = sys.argv[1]

    rospy.loginfo("Connected on %s" % (port_name) )
    ser = serial.Serial(port_name,38400,timeout=1)

    ser.write("RDF1R1\r\n")
    time.sleep(3)

    r = rospy.Rate(1000) # 10hz
    while not rospy.is_shutdown():
        while ser.in_waiting:

            raw_data = ser.readline()
            
           
            if len(raw_data) >= 4:
               

                hex_force = raw_data[1:4]
                int_force  = int(hex_force,16)     
                print (int_force)
                force_pub.publish(int_force)

            cnt += 1

        r.sleep()   
       


if __name__ == '__main__':
    try:
        get_date()
    except rospy.ROSInterruptException: pass

