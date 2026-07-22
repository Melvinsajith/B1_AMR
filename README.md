# B1_AMR

# AMR — ROS 2 Humble Autonomous Mobile Robot

A differential-drive Autonomous Mobile Robot (AMR) package configured for **ROS 2 Humble** and **Gazebo Classic**. Features include URDF/Xacro kinematics, LiDAR/Camera integrations, SLAM mapping via `slam_toolbox`, and Nav2 navigation readiness.

## System Architecture & Features
- **Kinematics:** 2-Wheel Differential Drive + Low-friction Caster Wheel.
- **Sensors:** 360° LiDAR (`/scan`), RGB Camera (`/camera/image_raw`).
- **Plugins:** `libgazebo_ros_diff_drive.so`, `libgazebo_ros_ray_sensor.so`.
- **SLAM:** `slam_toolbox` with `CeresSolver`.

## Quickstart Guide

### 1. Build Package
```bash
cd ~/ros2_amr_ws
colcon build --symlink-install
source install/setup.bash
