# ROS 2 Obstacle Avoidance

This project is a small ROS 2 Humble application that simulates a distance sensor and a simple obstacle avoidance system.

The package contains two nodes:

- **`distance_sensor`** – generates simulated distance measurements and obstacle directions.
- **`obstacle_avoidance`** – subscribes to the sensor data and makes a decision based on the distance and obstacle direction.

## Packages and build

It is assumed that the ROS 2 workspace is `~/ros2_ws/` and ROS 2 Humble is installed.

### Clone the package

```bash
cd ~/ros2_ws/src
git clone https://github.com/reb111/tom_x4u.git
```

### Build the ROS 2 package

```bash
cd ~/ros2_ws
source /opt/ros/humble/setup.bash
colcon build --packages-select tom_x4u --symlink-install
```

### Source the workspace and launch the nodes

Source the workspace before running ROS 2 commands:

```bash
source ~/ros2_ws/install/setup.bash
```

Start both nodes:

```bash
ros2 launch tom_x4u tom_x4u.launch.py
```

### Check

While the nodes are running, open another terminal and source the workspace:

```bash
source /opt/ros/humble/setup.bash
source ~/ros2_ws/install/setup.bash
```

Check the distance topic:

```bash
ros2 topic echo /distance
```

Check the obstacle direction topic:

```bash
ros2 topic echo /obstacle_direction
```

The `distance_sensor` node publishes simulated distance and obstacle direction data. The `obstacle_avoidance` node subscribes to both topics and prints its decision to the terminal.

## Nodes and topics

### `distance_sensor`

This node generates simulated sensor data every two seconds.

It publishes:

| Topic | Message type | Description |
|---|---|---|
| `/distance` | `std_msgs/msg/Float32` | Simulated distance in centimeters |
| `/obstacle_direction` | `std_msgs/msg/String` | Obstacle direction: `left`, `center` or `right` |

The distance is randomly generated between 5 and 200 cm. The obstacle direction is randomly selected.

### `obstacle_avoidance`

This node subscribes to `/distance` and `/obstacle_direction`.

It makes a decision based on the received data:

- Distance greater than 100 cm: `Continue`
- Distance greater than 10 cm and at most 100 cm: `Steer left` or `Steer right`, depending on the obstacle direction
- Distance at most 10 cm: `Stop`

When the obstacle is in the center, the node selects a turning direction randomly.

## Node-topic diagram

```mermaid
flowchart LR
    A([distance_sensor])
    B["/distance<br/>std_msgs/msg/Float32"]
    C["/obstacle_direction<br/>std_msgs/msg/String"]
    D([obstacle_avoidance])

    A --> B
    A --> C
    B --> D
    C --> D
```

