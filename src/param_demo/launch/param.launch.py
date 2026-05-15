import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    config_dir = os.path.join(
        get_package_share_directory('param_demo'), 'config')
    param_file = os.path.join(config_dir, 'parms.yaml')

    return LaunchDescription([
        Node(
            package='param_demo',
            executable='param_node',
            name='param_node',
            parameters=[param_file]
        )
    ])