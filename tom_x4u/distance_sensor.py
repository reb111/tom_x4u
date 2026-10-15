import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32


class DistanceSensor(Node):

    def __init__(self):
        super().__init__('distance_sensor')
        self.publisher = self.create_publisher(
            Float32, '/distance', 10
        )
        self.distances = [150.0, 80.0, 20.0, 60.0]
        self.index = 0
        self.timer = self.create_timer(2.0, self.publish_distance)

    def publish_distance(self):
        msg = Float32()
        msg.data = self.distances[self.index]
        self.publisher.publish(msg)
        self.get_logger().info(
            f'Mert tavolsag: {msg.data} cm'
        )
        self.index = (self.index + 1) % len(self.distances)


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
