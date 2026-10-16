
import random

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32, String


class DistanceSensor(Node):

    def __init__(self):
        super().__init__('distance_sensor')

        self.distance_publisher = self.create_publisher(
            Float32, '/distance', 10
        )
        self.direction_publisher = self.create_publisher(
            String, '/obstacle_direction', 10
        )

        self.timer = self.create_timer(2.0, self.publish_data)

    def publish_data(self):
        distance_msg = Float32()
        distance_msg.data = float(random.randint(5, 200))
        self.distance_publisher.publish(distance_msg)

        direction_msg = String()
        direction_msg.data = random.choice(
            ['left', 'center', 'right']
        )
        self.direction_publisher.publish(direction_msg)

        self.get_logger().info(
            f'Distance: {distance_msg.data} cm, '
            f'Position: {direction_msg.data}'
        )


def main(args=None):
    rclpy.init(args=args)
    node = DistanceSensor()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
