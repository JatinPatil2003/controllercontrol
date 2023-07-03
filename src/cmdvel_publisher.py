#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
import pygame

    

if __name__ == '__main__':
    pygame.init()
    pygame.joystick.init()

    max_speed = float(input("Enter max speed {0.1 - 0.5}"))
    wheel_width = 0.23

    if pygame.joystick.get_count() == 0:
        rospy.loginfo("No controller connected.")
    else:
        joystick = pygame.joystick.Joystick(0)
        joystick.init()
        try:
            rospy.init_node('cmd_vel_publisher', anonymous=True)
            pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
            rate = rospy.Rate(10)  # 10 Hz
            trans_perc = 0
            rot_perc = 0

            while not rospy.is_shutdown():
                for event in pygame.event.get():
                    if event.type == pygame.JOYAXISMOTION:
                        trans_perc = round(joystick.get_axis(3), 2)
                        rot_perc = round(joystick.get_axis(0), 2)
                        # print(trans_perc, rot_perc)
                trans = max_speed * trans_perc * -1
                rot = (max_speed * rot_perc * 2) / wheel_width

                print(trans,rot)
                twist_msg = Twist()
                twist_msg.linear.x = trans  
                twist_msg.angular.z = rot  

                pub.publish(twist_msg)
                rate.sleep()
        except rospy.ROSInterruptException:
            pass
