from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node

from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    # Caminho do diretório do pacote instalado
    pkg_share = get_package_share_directory('farm_inspection')

    # Caminho do arquivo SDF
    sdf_path = os.path.join(pkg_share, 'models', 'building_robot.sdf')

    # Processo para iniciar o Gazebo com o modelo
    gazebo = ExecuteProcess(
        cmd=['ign', 'gazebo', sdf_path, '--verbose'],
        output='screen'
    )

    # Nó do lidar_node (já instalado via CMake)
    #lidar_node = Node(
    #    package='farm_inspection',
    #    executable='lidar_node',
    #    name='lidar_node',
    #    output='screen'
    #)

    # Pontes ROS <-> Gazebo
    bridge_cmd_vel = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        arguments=['/cmd_vel@geometry_msgs/msg/Twist@ignition.msgs.Twist'],
        output='screen'
    )

    bridge_imu = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        arguments=['/imu@sensor_msgs/msg/Imu@ignition.msgs.IMU'],
        output='screen'
    )

    bridge_lidar = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        arguments=['/lidar_distance@std_msgs/msg/Float64@ignition.msgs.Double'],
        output='screen'
    )

    bridge_camera_image = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        arguments=['/camera@sensor_msgs/msg/Image@ignition.msgs.Image'],
        output='screen'
    )

    return LaunchDescription([
        gazebo,
        #lidar_node,
        bridge_cmd_vel,
        bridge_imu,
        bridge_lidar,
        bridge_camera_image,
    ])

