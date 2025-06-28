FROM osrf/ros:humble-desktop-full

RUN apt update && apt install -y \
    ros-humble-ros-ign \
    ros-humble-ros-ign-gazebo \
    ros-humble-joint-state-publisher-gui \
    && rm -rf /var/lib/apt/lists/*

# Copia os arquivos do robô e mundo para dentro do container
COPY moray_assets/ /root/moray/

# Exporta caminhos para que o Gazebo e ROS encontrem os recursos
ENV GZ_SIM_RESOURCE_PATH=/root/moray/sdf_world
ENV GAZEBO_MODEL_PATH=/root/moray/models

# Seta o ROS 2 Humble como ambiente padrão
ENV ROS_DISTRO=humble
SHELL ["/bin/bash", "-c"]
RUN echo "source /opt/ros/$ROS_DISTRO/setup.bash" >> ~/.bashrc
