
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32


class ObstacleAvoidance(Node):

    def __init__(self):
        super().__init__('obstacle_avoidance')
        self.subscription = self.create_subscription(
            Float32,
            '/distance',
            self.distance_callback,
            10
        )

    def distance_callback(self, msg):
        distance = msg.data

        if distance > 100:
            decision = 'Continue'
        elif distance > 30:
            decision = 'Slow down'
        else:
            decision = 'Stop'

        self.get_logger().info(
            f'Distance: {distance} cm | Decision: {decision}'
        )


def main(args=None):
    rclpy.init(args=args)
    node = ObstacleAvoidance()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
