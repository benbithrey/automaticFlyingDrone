#!/usr/bin/env python3

#Include "plugin_drone.h"

import rospy
import os
import geometry_msgs.msg
from std_msgs.msg import String, Bool, Empty, Time
from sensor_msgs.msg import Imu
from geometry_msgs.msg import Twist, Pose, Point
from nav_msgs.msg import Odometry
from math import pow, atan2, sqrt
from rosgraph_msgs.msg import Clock


class Drone:
	def __init__(self):
		self.imu = Imu()
		self.pose = Pose()
		self.odom = Odometry()
		self.posctrl = Bool()
		self.time = Time()

		rospy.init_node('Controller', anonymous=True)
		self.takeoff = rospy.Publisher('/drone/takeoff', Empty, queue_size=1)
		self.pub_clock = rospy.Publisher('/clock', Time, queue_size=10)

#		rospy.Subscriber('/drone/gt_pose', Pose, self.pos(self))
		rospy.Subscriber('/drone/posctrl', Bool, self.posc(self))

		self.zero_time = rospy.get_time()
		#self.sim_time_multiplier = 10
		#self.sim_clock = Clock()

#	def pos(self, data):
#		self.pose.position = data
#		print(self.pose)
#		print(data.pose.position)

	def posc(self, data):
		self.posctrl = data
		print(self.posctrl)
		print(data)

	def take_off(self):
		count = 0
		start_time = rospy.Time.now()
		self.pub_clock.publish()
		while count < 100:
			time = start_time
			print(rospy.Time.now())
#			print(count)
			print(time)
			#print(self.data)
			count = count + 1


if __name__ == '__main__':
	try:
		x = Drone()
		x.take_off()
	except rospy.ROSInterruptException:
		pass
