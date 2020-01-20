#!/usr/bin/env python 

import rospy
from std_msgs.msg import Bool

if __name__ == "__main__":
	rospy.init_node("led_pub")
	pub0 = rospy.Publisher("led0", Bool, queue_size=10)
        pub1 = rospy.Publisher("led1", Bool, queue_size=10)
        pub2 = rospy.Publisher("led2", Bool, queue_size=10)
        pub3 = rospy.Publisher("led3", Bool, queue_size=10)
        pub4 = rospy.Publisher("led4", Bool, queue_size=10)
        pub5 = rospy.Publisher("led5", Bool, queue_size=10)
        pub6 = rospy.Publisher("led6", Bool, queue_size=10)
        pub7 = rospy.Publisher("led7", Bool, queue_size=10)
        pub8 = rospy.Publisher("led8", Bool, queue_size=10)
	rate = rospy.Rate(10)

        while not rospy.is_shutdown():
            i = input()
            i = bin(i)
            s = '00000000' + str(i)
         
            print(s[-1])
            print(s[-2])
            print(s[-3])
            print(s[-4])
            print(s[-5])
            print(s[-6])
            print(s[-7])
            print(s[-8])
            pub0.publish(True)

            if s[-1] == '1':
        	pub1.publish(True)
            else:
                pub1.publish(False)

            if s[-2] == '1':
                pub2.publish(True)
            else:
                pub2.publish(False)

            if s[-3] == '1':
                pub3.publish(True)
            else:
                pub3.publish(False)

            if s[-4] == '1':
                pub4.publish(True)
            else:
                pub4.publish(False)

            if s[-5] == '1':
                pub5.publish(True)
            else:
                pub5.publish(False)

            if s[-6] == '1':
                pub6.publish(True)
            else:
                pub6.publish(False)

            if s[-7] == '1':
                pub7.publish(True)
            else:
                pub7.publish(False)

            if s[-8] == '1':
                pub8.publish(True)
            else:
                pub8.publish(False)

        rate.sleep()
