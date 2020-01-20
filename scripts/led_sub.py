#!/usr/bin/env python

import rospy
from std_msgs.msg import Bool

def led0_callback(msg):
    if msg.data:
        with open("/dev/myled0", "w") as f:
                f.write("0\n")

def led1_callback(msg):
    if msg.data:
	with open("/dev/myled0", "w") as f:
		f.write("1\n")

def led2_callback(msg):
    if msg.data:
	with open("/dev/myled0", "w") as f:
		f.write("2\n")

def led3_callback(msg):
    if msg.data:
        with open("/dev/myled0", "w") as f:
                f.write("3\n")

def led4_callback(msg):
    if msg.data:
        with open("/dev/myled0", "w") as f:
                f.write("4\n")
def led5_callback(msg):
    if msg.data:
        with open("/dev/myled0", "w") as f:
                f.write("5\n")

def led6_callback(msg):
    if msg.data:
        with open("/dev/myled0", "w") as f:
                f.write("6\n")

def led7_callback(msg):
    if msg.data:
        with open("/dev/myled0", "w") as f:
                f.write("7\n")

def led8_callback(msg):
    if msg.data:
        with open("/dev/myled0", "w") as f:
                f.write("8\n")

if __name__ == "__main__":
	rospy.init_node("led_pub")
	sub0 = rospy.Subscriber("led0", Bool, led0_callback, queue_size=10)
	sub1 = rospy.Subscriber("led1", Bool, led1_callback, queue_size=10)
        sub2 = rospy.Subscriber("led2", Bool, led2_callback, queue_size=10)
        sub3 = rospy.Subscriber("led3", Bool, led3_callback, queue_size=10)
        sub4 = rospy.Subscriber("led4", Bool, led4_callback, queue_size=10)
        sub5 = rospy.Subscriber("led5", Bool, led5_callback, queue_size=10)
        sub6 = rospy.Subscriber("led6", Bool, led6_callback, queue_size=10)
        sub7 = rospy.Subscriber("led7", Bool, led7_callback, queue_size=10)
        sub8 = rospy.Subscriber("led8", Bool, led8_callback, queue_size=10)
	rospy.spin()
