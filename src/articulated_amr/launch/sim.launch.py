import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():

    package_name = 'articulated_amr'
    pkg_share = get_package_share_directory(package_name)

    world_arg = DeclareLaunchArgument(
        'world',
        default_value='',
        description='Full path to Gazebo world file to load'
    )

    # Include RSP launch file
    rsp = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(pkg_share, 'launch', 'rsp.launch.py')
        ]),
        launch_arguments={'use_sim_time': 'true'}.items()
    )

    # Include Gazebo launch file
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

    # Spawn Robot Node
    spawn_entity = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=[
            '-topic', 'robot_description',
            '-entity', 'articulated_amr',
            '-z', '0.1'
        ],
        output='screen'
    )

    return LaunchDescription([
        world_arg,
        rsp,
        gazebo,
        spawn_entity
    ])