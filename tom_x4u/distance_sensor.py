import random

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32


class DistanceSensor(Node):

    def __init__(self):
        super().__init__('distance_sensor')
        self.publisher = self.create_publisher(
            Float32, '/distance', 10
        )
        self.timer = self.create_timer(2.0, self.publish_distance)

    def publish_distance(self):
        msg = Float32()
        msg.data = float(random.randint(10, 200))
        self.publisher.publish(msg)
        self.get_logger().info(
            f'Distance: {msg.data} cm'
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

