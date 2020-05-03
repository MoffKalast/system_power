#!/usr/bin/env python

from __future__ import print_function

import rospy
import sys
import os

from std_msgs.msg import String

class SystemPower:

	def __init__(self):
		rospy.init_node('system_power', anonymous=False)
		self.cmd = rospy.Subscriber('/system_power', String, self.command)

	def command(self, msg):
		if msg.data == "poweroff":
			os.system('sudo systemctl poweroff')
		elif msg.data == "reboot":
			os.system('sudo systemctl reboot')

try:
	t = SystemPower()
	rospy.spin()

except rospy.ROSInterruptException:
	print("Script interrupted", file=sys.stderr)
