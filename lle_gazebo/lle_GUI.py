#!/usr/bin/env python3
import roslaunch
import rospy
import tkinter as tk
import os
from std_msgs.msg import Float64
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Image
import cv2
#import home/mohammad/catkin_ws/src/lle_gazebo/src
import subprocess

#os.popen('source ./catkin_ws/devel/setup.bash')
#source = subprocess.Popen('source /home/mohammad/catkin_ws/devel/setup.bash')
roscore = subprocess.Popen('roscore')


HEIGHT = 700 
WIDTH = 800

rospy.init_node('en_Mapping', anonymous=True)
uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)
#roslaunch.configure_logging(uuid)
#launch = roslaunch.parent.ROSLaunchParent(uuid, ["/home/roboticlab/catkin_ws/src/lle_gazebo/lle_gazebo.launch"])

def callback(data):
	
	cap = cv2.VideoCapture(-1)

def launch():
	#os.system('roslaunch lle_gazebo lle_gazebo.launch')
	#gazebo = subprocess.Popen("roslaunch lle_gazebo lle_gazebo.launch")
	launch = roslaunch.parent.ROSLaunchParent(uuid, ["/home/mohammad/catkin_ws/src/lle_gazebo/launch/lle_gazebo.launch"])
	launch.start()
	
def walk_run():
	roswalk = os.popen('/home/mohammad/catkin_ws/src/lle_gazebo/src/walker.py')
	#os.system('/home/mohammad/catkin_ws/src/lle_gazebo/src/walker.py')
	#root.after(1000, scanning)

def move(a):
	pub=rospy.Publisher('/lle/cmd_vel', Twist, queue_size=10)
	move=Twist()
	move.linear.x=a
	pub.publish(move)

def close():
	root.destroy()
	#roswalk = os.popen('killall -9 rosmaster')
root=tk.Tk()
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

#background_image=tk.PhotoImage(file='./lle.jpg')
#background_label=tk.Label(root, image=background_image)
#background_label.place(relheight=1, relwidth=1)

frame = tk.Frame(root, bg='#11d6f0') 
frame.place(relx= 0.1, rely=0.1, relwidth= 0.8, relheight = 0.8)

#frame1=tk.Frame(root, bg='red')
#frame1.place(relx= 0.1, rely= 0.55, relwidth=0.8, relheight = 0.3)

#label=tk.Label(frame, bg="#d4228f")
#label.place(relx=0.5, rely=0.5, relwidth=0.28, relheight=0.1)


button = tk.Button(frame, text="Run", bg='gray', fg='red', command=lambda: launch())
button.place(relx=0.2, rely=0 , relwidth=0.25, relheight=0.25)

button_u = tk.Button(frame, text="walk", bg='gray', fg='red', command=lambda: walk_run())
button_u.place(relx=0.2, rely=0.3 , relwidth=0.25, relheight=0.25)

button_s = tk.Button(root, text="Close", bg='gray', fg='red', command=lambda: close())
button_s.place(relx=0, rely=0 , relwidth=0.15, relheight=0.05)

button_m = tk.Button(frame, text="Start walking", bg='gray', fg='red', command=lambda: move(20))
button_m.place(relx=0.5, rely=0.2 , relwidth=0.25, relheight=0.25)

button_q = tk.Button(frame, text="Stop walking", bg='gray', fg='red', command=lambda: move(0))
button_q.place(relx=0.5, rely=0.5 , relwidth=0.25, relheight=0.25)


root.mainloop()
rospy.Subscriber("image_raw",Image,self.callback)
rospy.spin()

#key_=rospy.Subscriber('/lle/cmd_vel', Twist, act_walk)
#if __name__ == '__main__':
	#root.mainloop()


