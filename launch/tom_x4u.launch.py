
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='tom_x4u',
            executable='distance_sensor',
            name='distance_sensor',
            output='screen'
        ),
        Node(
            package='tom_x4u',
            executable='obstacle_avoidance',
            name='obstacle_avoidance',
            output='screen'
        ),
    ])
