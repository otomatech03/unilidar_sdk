# ~/ros2_ws/src/unilidar_sdk/unitree_lidar_ros2/launch/launch.py
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, LogInfo
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Declare a launch argument for the parameter 'param'
        DeclareLaunchArgument('param', default_value='default_value', description='An argument for the node'),
        
        # Define the node for the unitree_lidar_ros2 package
        Node(
            package='unitree_lidar_ros2',
            executable='unitree_lidar_ros2_node',  # Replace with the actual executable name
            name='unitree_lidar_ros2_node',
            output='screen',
            parameters=[{'param': 'value'}],  # Add any parameters here if needed
        ),
    ])
