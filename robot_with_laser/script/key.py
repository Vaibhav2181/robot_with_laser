#!/usr/bin/env python3
import rospy
import sys
from geometry_msgs.msg import Twist

def mybot_velocity_commands():
  # Velocity publisher
  vel_pub = rospy.Publisher('/jackal_velocity_controller/cmd_vel', Twist, queue_size=10)
  rospy.init_node('mybot_cmd_vel', anonymous=True)

  msg = Twist()
  msg.linear.x = -0.5
  msg.linear.y = 0
  msg.linear.z = 0
  msg.angular.x = 0
  msg.angular.y = 0
  msg.angular.z = -0.5

  rate = rospy.Rate(10) # 10hz
  while not rospy.is_shutdown():
    vel_pub.publish(msg)
    rate.sleep()

if __name__ == '__main__':
  if len(sys.argv) == 1:
    try:
      mybot_velocity_commands()      
    except rospy.ROSInterruptException:
      pass
  else:
    print("Usage: mybot_cmd_vel arg1")
