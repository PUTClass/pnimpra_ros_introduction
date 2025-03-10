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
from geometry_msgs.msg import Twist
import threading
import math

class TurtleTrajectory(Node):

    def __init__(self):
        super().__init__('turtle_trajectory')
        # self.traj_pub = self.create_publisher(type, topic, 10)
        
        # Every move command can be executed at intervals
        # timer_period = 2.0  # seconds
        # self.rate = self.create_rate(1/timer_period)

    def run(self):
        while rclpy.ok():
            ### A sequence of moves to execute/publish can be written here.
            pass

    '''
    geometry_msgs/msg/Twist
    # This expresses velocity in free space broken into its linear and angular parts.

    Vector3  linear
        float64 x
        float64 y
        float64 z
    Vector3  angular
        float64 x
        float64 y
        float64 z
    '''
    # def sample_twist_message(self, angular, linear):
    #     trajectory_msg = Twist()
    #     trajectory_msg.angular.z = rotation
    #     trajectory_msg.linear.z = linear_movement
        

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
