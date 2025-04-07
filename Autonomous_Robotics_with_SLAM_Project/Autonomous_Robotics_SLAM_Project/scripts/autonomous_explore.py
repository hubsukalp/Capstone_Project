
#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

def callback(msg):
    twist = Twist()
    if msg.ranges[0] < 1:
        twist.angular.z = 0.5
    else:
        twist.linear.x = 0.2
    pub.publish(twist)

rospy.init_node('autonomous_explore')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
sub = rospy.Subscriber('/scan', LaserScan, callback)
rospy.spin()
