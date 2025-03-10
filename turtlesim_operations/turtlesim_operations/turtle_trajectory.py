# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int64
from geometry_msgs.msg import Twist
import threading
import math

class TurtleTrajectory(Node):

    def __init__(self):
        super().__init__('turtle_trajectory')
        self.traj_pub = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        timer_period = 2.0  # seconds
        self.rate = self.create_rate(1/timer_period)

    def run(self):
        while rclpy.ok():
            for i in range(4):
                self.go_forward()
                self.rate.sleep()
                self.rotate_left()
                self.rate.sleep()

    def rotate_left(self):
        trajectory_msg = Twist()
        trajectory_msg.angular.z = math.pi/2
        self.traj_pub.publish(trajectory_msg)

    def rotate_right(self):
        trajectory_msg = Twist()
        trajectory_msg.angular.z = -math.pi/2
        self.traj_pub.publish(trajectory_msg)

    def go_forward(self):
        trajectory_msg = Twist()
        trajectory_msg.linear.x = 2.0
        self.traj_pub.publish(trajectory_msg)

    def go_backward(self):
        trajectory_msg = Twist()
        trajectory_msg.linear.x = -2.0
        self.traj_pub.publish(trajectory_msg)

def main(args=None):
    rclpy.init(args=args)

    node = TurtleTrajectory()
    thread = threading.Thread(target=rclpy.spin, args=(node,), daemon=True)
    thread.start()
    node.run()
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
