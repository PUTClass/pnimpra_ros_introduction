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
from random import seed, randint

class RandomNumbers(Node):

    def __init__(self):
        super().__init__('random_Numbers')
        # self.publisher_ = self.create_publisher(type, topic, 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        seed(1337)

    def timer_callback(self):
        ### Create message and publish it
        # self.get_logger().info(f"Publishing number {value}")
        pass


def main(args=None):
    rclpy.init(args=args)

    number_publisher = RandomNumbers()

    rclpy.spin(number_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    number_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
