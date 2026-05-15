from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():

    return LaunchDescription([
        Node(
            package='server_node',
            executable='add_server',
            name='add_server_node',
            output='screen'
        ),
        Node(
            package='server_node',
            executable='add_client',
            name='add_client_node',
            output='screen'
        ),
    ])