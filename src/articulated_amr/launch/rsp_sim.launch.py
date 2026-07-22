import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
import xacro

def generate_launch_description():

    package_name = 'articulated_amr'

    # Declare world launch argument (allows specifying a custom .world file)
    world_arg = DeclareLaunchArgument(
        'world',
        default_value='',
        description='Full path to Gazebo world file to load'
    )

    # Process Xacro file to URDF XML string
    pkg_share = get_package_share_directory(package_name)
    xacro_file = os.path.join(pkg_share, 'urdf', 'robot.urdf.xacro')
    robot_description_raw = xacro.process_file(xacro_file).toxml()

    # Node: Robot State Publisher (Publishes TFs and robot_description topic)
    node_robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[{
            'robot_description': robot_description_raw,
            'use_sim_time': True
        }]
    )

    # Action: Include default Gazebo Classic launch file
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(
                get_package_share_directory('gazebo_ros'),
                'launch',
                'gazebo.launch.py'
            )
        ]),
        launch_arguments={'world': LaunchConfiguration('world')}.items()
    )

    # Node: Spawn Entity into Gazebo
    spawn_entity = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=[
            '-topic', 'robot_description',
            '-entity', 'articulated_amr',
            '-z', '0.1'  # Slightly elevated so wheels don't clip into ground
        ],
        output='screen'
    )

    return LaunchDescription([
        world_arg,
        node_robot_state_publisher,
        gazebo,
        spawn_entity
    ])