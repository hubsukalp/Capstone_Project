#!/usr/bin/env python

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from geometry_msgs.msg import PoseStamped

def send_goal(x, y, frame="map"):
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = frame
    goal.target_pose.header.stamp = rospy.Time.now()
    goal.target_pose.pose.position.x = x
    goal.target_pose.pose.position.y = y
    goal.target_pose.pose.orientation.w = 1.0

    client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
    client.wait_for_server()
    client.send_goal(goal)
    client.wait_for_result()
    rospy.loginfo("Goal reached.")

if __name__ == "__main__":
    rospy.init_node("autonomous_explore")
    send_goal(1.0, 0.0)
    send_goal(2.0, 0.0)
    send_goal(2.0, 2.0)
    send_goal(0.0, 2.0)
