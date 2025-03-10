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
from turtlesim.msg import Pose
from std_msgs.msg import Float64
import threading
import math

def distance_between_poses(a: Pose, b: Pose):
    return math.sqrt((a.x-b.x)**2 + (a.y-b.y)**2)

class TurtleDistance(Node):

    def __init__(self):
        super().__init__('turtle_distance')
        # self.dist_pub = self.create_publisher(type, topic, 10)
        # self.pose_sub = self.create_subscription(type, topic, self.pose_callback, 10)

        self.last_pose = None
        self.accumulated_distance = 0.0

        # Distance can be published at equal intervals
        # self.timer = self.create_timer(0.5, self.publish_distance)
    
    def pose_callback(self, msg: Pose):
        ### Get the pose and sum up the distance
        pass

    def publish_distance(self):
        pass

    def run(self):
        while rclpy.ok():
            pass

def main(args=None):
    rclpy.init(args=args)

    node = TurtleDistance()
    thread = threading.Thread(target=rclpy.spin, args=(node,), daemon=True)
    thread.start()
    node.run()
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()