#!/usr/bin/python3
# SPDX-FileCopyrightText: 2024 Miyuu Taniguchi
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

rclpy.init()
node = Node("talker")
pub = node.create_publisher(Int16, "countup", 10)
n = 1896


def cb():
    global n
    msg = Int16()
    msg.data = n
    pub.publish(msg)
    node.get_logger().info(f"olympic year: {n}")
    n += 2

def main():
    node.create_timer(0.5, cb)
    rclpy.spin(node)
