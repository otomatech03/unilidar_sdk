cmake_minimum_required(VERSION 3.5)
project(unitree_lidar_ros2)

# Default to C++14 if no language is specified
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

# Find the ament package
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(sensor_msgs REQUIRED)

# Add executable and link dependencies
add_executable(unitree_lidar_ros2_node src/unitree_lidar_ros2_node.cpp)

# Specify include directories
target_include_directories(unitree_lidar_ros2_node
  PRIVATE
    include
)

# Link dependencies
ament_target_dependencies(unitree_lidar_ros2_node
  rclcpp
  sensor_msgs
)

# Install executables and launch files
install(TARGETS
  unitree_lidar_ros2_node
  DESTINATION lib/${PROJECT_NAME}
)

# Install launch files (if any)
install(DIRECTORY launch/
  DESTINATION share/${PROJECT_NAME}/launch
)

ament_package()
