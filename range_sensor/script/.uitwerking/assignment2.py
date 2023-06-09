#! /usr/bin/env python

# Assignment 2 for Week1: In this assignment you will subscribe to the topic that
# publishes information on the box height in metres and use the metres_to_feet
# service to convert this height in metres to height in feet.


import rospy
from range_sensor_msgs.msg import BoxHeightInformation
from range_sensor_msgs.srv import ConvertMetresToFeet, ConvertMetresToFeetRequest, ConvertMetresToFeetResponse

def box_height_info_callback(data):
    try:
        # Create a proxy for the service to convert metres to feet - Part2.
        metres_to_feet = rospy.ServiceProxy('metres_to_feet', ConvertMetresToFeet)

        # Extract box_height_meters from data
	box_height_meters = data.box_height

        # Call the service here.
        service_response = metres_to_feet(box_height_meters)

        # Extract box_height_feet from service_response
        box_height_feet = service_response.distance_feet

        # Write a log message here to print the height of this box in feet.
        rospy.loginfo("The hight of the box is %4.2f metres or %4.2f feet" %(box_height_meters, box_height_feet)) 

    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

if __name__ == '__main__':
    # Initialize the ROS node here.
    rospy.init_node('box_height_in_feet', anonymous = False)

    # First wait for the service to become available - Part2.
    rospy.loginfo("Waiting for service...")
    rospy.wait_for_service('metres_to_feet')
    rospy.loginfo("Service %s is now available", 'metres_to_feet')

    # Create a subscriber to the box height topic - Part1.
    rospy.Subscriber('box_height_info', BoxHeightInformation, box_height_info_callback)

    # Prevent this ROS node from terminating until Ctrl+C is pressed.
    rospy.spin()
