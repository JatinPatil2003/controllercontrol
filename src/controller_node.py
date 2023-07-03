#!/usr/bin/env python3

import rospy
import pygame

def controller_node():
    rospy.init_node('controller_node', anonymous=True)
    pygame.init()
    pygame.joystick.init()

    if pygame.joystick.get_count() == 0:
        rospy.loginfo("No controller connected.")
        return

    joystick = pygame.joystick.Joystick(0)
    joystick.init()

    rospy.loginfo("Controller Name: %s", joystick.get_name())
    rospy.loginfo("Number of Axes: %d", joystick.get_numaxes())
    rospy.loginfo("Number of Buttons: %d", joystick.get_numbuttons())
    rospy.loginfo("Number of Hats: %d", joystick.get_numhats())

    while not rospy.is_shutdown():
        for event in pygame.event.get():
            if event.type == pygame.JOYAXISMOTION:
                axis_value = joystick.get_axis(3)
                print(axis_value)
        # for event in pygame.event.get():
        #     if event.type == pygame.JOYAXISMOTION:
        #         for axis in range(joystick.get_numaxes()):
        #             axis_value = joystick.get_axis(axis)
        #             rospy.loginfo("Axis %d: %.2f", axis, axis_value)

        #     elif event.type == pygame.JOYBUTTONDOWN:
        #         for button in range(joystick.get_numbuttons()):
        #             button_state = joystick.get_button(button)
        #             rospy.loginfo("Button %d: %d", button, button_state)

        #     elif event.type == pygame.JOYHATMOTION:
        #         for hat in range(joystick.get_numhats()):
        #             hat_value = joystick.get_hat(hat)
        #             rospy.loginfo("Hat %d: %s", hat, hat_value)

    pygame.quit()

if __name__ == '__main__':
    try:
        controller_node()
    except rospy.ROSInterruptException:
        pass
