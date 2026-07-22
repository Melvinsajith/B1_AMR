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


## Setup Environment & Install Dependencies

Bash

```
# Install core ROS 2 Humble packages for simulation, SLAM, and teleop
sudo apt update
sudo apt install ros-humble-joint-state-publisher \
                 ros-humble-joint-state-publisher-gui \
                 ros-humble-xacro \
                 ros-humble-slam-toolbox \
                 ros-humble-teleop-twist-keyboard \
                 ros-humble-rviz2

# Ensure Gazebo setup environment variable is active
source /usr/share/gazebo/setup.sh
```

## 2. Build Workspace

Bash

```
cd ~/ros2_amr_ws
colcon build --symlink-install
source install/setup.bash
```

## 3. Run Simulation & SLAM Pipeline (5 Separate Terminals)

> **Note:** Remember to source your workspace (`source ~/ros2_amr_ws/install/setup.bash`) in **every new terminal** before running commands.
> 

### Terminal 1: Robot State Publisher

Bash

```
source ~/ros2_amr_ws/install/setup.bash
ros2 launch articulated_amr rsp.launch.py
```

### Terminal 2: Start Gazebo Classic

Bash

```
source ~/ros2_amr_ws/install/setup.bash
ros2 launch gazebo_ros gazebo.launch.py
```

### Terminal 3: Spawn Robot into Gazebo

Bash

```
source ~/ros2_amr_ws/install/setup.bash
ros2 run gazebo_ros spawn_entity.py -topic robot_description -entity articulated_amr -z 0.1
```

### Terminal 4: Launch SLAM Toolbox

Bash

```
source ~/ros2_amr_ws/install/setup.bash
ros2 launch articulated_amr slam.launch.py
```

### Terminal 5: RViz2 Visualization

Bash

```
source ~/ros2_amr_ws/install/setup.bash
rviz2
```

- **Fixed Frame:** Change to `map`.
- **Add Displays:** Add `Map` (topic `/map`), `LaserScan` (topic `/scan`), and `RobotModel`.

## 4. Teleoperate & Save Map

### Terminal 6: Drive the Robot

Bash

```
source ~/ros2_amr_ws/install/setup.bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

- Use `i` (forward), `j` (left), `l` (right), `,` (back), `k` (stop) to slowly map your arena.

### Terminal 7: Save Completed Map

Bash

```
cd ~/ros2_amr_ws/src/articulated_amr/maps
ros2 run nav2_map_server map_saver_cli -f my_map
```

*(Generates `my_map.yaml` and `my_map.pgm` inside your `maps/` folder)*
