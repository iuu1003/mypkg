#!/usr/bin/python3
# SPDX-FileCopyrightText: 2024 Miyuu Taniguchi
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

rclpy.init()
node = Node("talker")
pub = node.create_publisher(Int16, "countup", 10)
n = 0


def cb():
    global n
    msg = Int16()
    msg.data = n
    pub.publish(msg)
    node.get_logger().info(f"Published: {msg.data}")
    n += 1

def main():
    node.get_logger().info("Node started!")
    node.create_timer(0.5, cb)
    rclpy.spin(node)

if __name__ == "__main__":
    main()
