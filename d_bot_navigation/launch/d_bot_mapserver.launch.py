import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    amcl_config = os.path.join(get_package_share_directory('d_bot_localization_server'), 'config', 'amcl.yaml')
    map_file = os.path.join(get_package_share_directory('d_bot_slam'), 'maps', 'cafe.yaml')

    return LaunchDescription([
        Node(
            package='nav2_map_server',
            executable='map_server',
            name='map_server',
            output='screen',
            parameters=[{'use_sim_time': True}, 
                        {'yaml_filename':map_file} 
                       ]),
        # Node(
        #     package='nav2_amcl',
        #     executable='amcl',
        #     name='amcl',
        #     output='screen',
        #     parameters=[amcl_config]
        # ),

        Node(
            package='nav2_lifecycle_manager',
            executable='lifecycle_manager',
            name='lifecycle_manager_mapper',
            output='screen',
            parameters=[{'autostart': True},
                {'node_names': ['map_server',
                                # 'amcl',
                                ]}])          
        ])

