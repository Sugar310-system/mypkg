#!/usr/bin/env python3
import rospy
import math

from std_msgs.msg import Int32

def cb(message):
    rospy.loginfo(message.data**2*math.pi)

if __name__ == '__main__':
    rospy.init_node('pi')
    sub = rospy.Subscriber('count_up', Int32, cb)
    rospy.spin()
