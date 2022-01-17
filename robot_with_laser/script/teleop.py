
#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

rospy.init_node('topic_publisher')
pub = rospy.Publisher('/jackal_velocity_controller/cmd_vel', Twist, queue_size=10)
rate = rospy.Rate(2)
move = Twist() # defining the way we can allocate the values
move.linear.x = -0.5 # allocating the values in x direction - linear
move.angular.z = 0.0  # allocating the values in z direction - angular

while not rospy.is_shutdown(): 
  pub.publish(move)
  rate.sleep()
