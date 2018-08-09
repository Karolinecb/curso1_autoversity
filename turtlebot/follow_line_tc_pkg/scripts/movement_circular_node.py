#!/usr/bin/env python
#
import rospy 
from geometry_msgs.msg import Twist

class Movement(object):
	
	def __init__(self):
		# Create publisher
		self.vel_pub = rospy.Publisher('/cmd_vel_mux/input/safety_controller',Twist, queue_size = 1)
		r = rospy.Rate(10) # 

		# Message
		twist = Twist()
		twist.linear.x  = 0.6
		twist.angular.z = 0.3

		# Publish
		while not rospy.is_shutdown():
			self.vel_pub.publish()
			r.sleep()
	
def main():

	rospy.init_node('movement_circular_node', anonymous=True)
	movement_object = Movement()
	rospy.spin()

if __name__ == '__main__':
	try:
		main()
	except rospy.ROSInterruptException:
		pass   
 