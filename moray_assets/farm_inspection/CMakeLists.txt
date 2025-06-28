cmake_minimum_required(VERSION 3.8)
project(farm_inspection)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# Encontrar dependências
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)

# (Removido lidar_node completamente)

# Instalar outros diretórios
install(
  DIRECTORY launch models scripts
  DESTINATION share/${PROJECT_NAME}
)

ament_package()

