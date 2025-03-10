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


class SumNextNumbers(Node):
    NUMBERS_IN_QUEUE = 8
    def __init__(self):
        super().__init__('sum_next_numbers')
        
        self.numbers = []
        # self.subscription = self.create_subscription(type, topic, self.listener_callback, 10)
        # self.publisher = self.create_publisher(type, topic, 10)
        


    def listener_callback(self, msg: Int64):
        pass
        # Store consecutive number in a list, calculate the sum and publish it
        # It's important to track the number of numbers in the list
       
        # self.get_logger().info(f"Publishing sum of numbers: {sum}")
    
    '''
    Example function to calculate the sum of numbers:
    '''
    # def sum_numbers(self):
    #     sum = 0

    #     if len(self.numbers) > 0:
    #         for number in self.numbers:
    #             sum = sum + number

    #     return sum

        
        


def main(args=None):
    rclpy.init(args=args)
    sum_node = SumNextNumbers()
    rclpy.spin(sum_node)


    sum_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
