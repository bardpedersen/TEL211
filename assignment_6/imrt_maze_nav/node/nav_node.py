#! /usr/bin/env python3

import rospy
from sensor_msgs.msg import Range
from geometry_msgs.msg import Twist
from imrt_speech.srv import Phrase

class Sensor:
    def __init__(self):
        rospy.wait_for_service('/text_to_speech/say_phrase')
        self.my_service_proxy = rospy.ServiceProxy('/text_to_speech/say_phrase', Phrase)
        self.response = self.my_service_proxy("Hello")
        
        self.left_threshold = 0.2
        self.left_opt_dist = 0.3
        self.left_senser_diff = 0.05
        self.front_threshold = 0.3

        self.left1_dist = 0.0
        self.left2_dist = 0.0
        self.front1_dist = 0.0
        self.front2_dist = 0.0

        self.sub1 = rospy.Subscriber("/ranges/rangesens_1", Range, self.process_front1)
        self.sub2 = rospy.Subscriber("/ranges/rangesens_2", Range, self.process_front2)
        self.sub3 = rospy.Subscriber("/ranges/rangesens_3", Range, self.process_left1)
        self.sub4 = rospy.Subscriber("/ranges/rangesens_4", Range, self.process_left2)

        self.pub = rospy.Publisher("/imrt_velocity_controller/cmd_vel", Twist, queue_size=1)
        self.move = Twist()


    def process_left1(self, msg):
        self.left1_dist = msg.range
        
    def process_left2(self, msg):
        self.left2_dist = msg.range
        
    def process_front1(self, msg):
        self.front1_dist = msg.range
        
    def process_front2(self, msg):
        self.front2_dist = msg.range
        self.move_forward()


    def move_forward(self):

        self.left_dist_avg = (self.left1_dist + self.left2_dist) / 2.0
        self.front_dist_avg = (self.front1_dist + self.front2_dist) / 2.0
    
        # Front free wall
        if self.front1_dist > self.front_threshold and self.front2_dist > self.front_threshold:
            self.response = self.my_service_proxy("Follow wall")

            # Closer to wall
            if self.left_dist_avg > self.left_opt_dist:
                self.move.linear.x = 0.1 * abs(self.left_dist_avg - self.left_opt_dist) + 0.1
                self.move.angular.z = 0.5 * abs(self.left_dist_avg - self.left_opt_dist) + 0.1

            # Further from wall
            elif self.left_dist_avg < self.left_opt_dist:
                self.move.linear.x = 0.1 * abs(self.left_opt_dist - self.left_dist_avg) + 0.1
                self.move.angular.z = - (0.5 * abs(self.left_opt_dist - self.left_dist_avg) + 0.1)


            # Turn when wall sticker
            if abs(self.left1_dist - self.left2_dist) > self.left_senser_diff:
                self.response = self.my_service_proxy("Outsticker wall, follow")

                if self.left1_dist > self.left2_dist:
                    self.move.linear.x = 0.1
                    self.move.angular.z = 1 * abs(self.left1_dist - self.left2_dist)

                elif self.left1_dist < self.left2_dist:
                    self.move.linear.x = 0.1
                    self.move.angular.z = -1 * abs(self.left1_dist - self.left2_dist)

            # Front free no wall


        # Front not free

        # Turn right
        elif self.front1_dist < self.front_threshold or self.front2_dist < self.front_threshold or self.front_dist_avg < self.left_dist_avg:
            self.move.linear.x = 0.0
            self.move.angular.z = -0.5
            self.response = self.my_service_proxy("Front not free, turn right")

        
        # Drive forward
        else:
            self.move.linear.x = 0.5 * (self.front_dist_avg + self.front_threshold) + 0.1
            self.move.angular.z = 0.0
            self.response = self.my_service_proxy("No wall, drive straight")

        self.pub.publish(self.move)


if __name__ == "__main__":
    rospy.init_node("nav_node")
    sensor = Sensor()
    rospy.spin()


