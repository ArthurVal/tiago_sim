#!/usr/bin/env python

"""ROS2 launch file launching a GZ server."""

from launch import LaunchDescription

from tiago_lfc.launch import (
    gz_server,
)


def generate_launch_description():
    """Create a GZ server."""
    return LaunchDescription(gz_server())
