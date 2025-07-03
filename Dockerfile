FROM osrf/ros:humble-desktop-full

RUN apt update && apt install -y \
    ros-humble-ros-ign \
    ros-humble-ros-ign-gazebo \
    ros-humble-joint-state-publisher-gui \
    && rm -rf /var/lib/apt/lists/*

# Não copie moray_assets — você vai montar como volume depois

# Variáveis de ambiente
ENV GZ_SIM_RESOURCE_PATH=/root/moray/sdf_world
ENV GAZEBO_MODEL_PATH=/root/moray/models
ENV ROS_DISTRO=humble

# Ativa o ROS no bash
SHELL ["/bin/bash", "-c"]
RUN echo "source /opt/ros/$ROS_DISTRO/setup.bash" >> ~/.bashrc

