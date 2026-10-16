import random

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32, String


class ObstacleAvoidance(Node):

    def __init__(self):
        super().__init__('obstacle_avoidance')

        self.distance = None
        self.direction = None

        self.distance_subscription = self.create_subscription(
            Float32, '/distance', self.distance_callback, 10
        )
        self.direction_subscription = self.create_subscription(
            String, '/obstacle_direction',
            self.direction_callback, 10
        )

    def distance_callback(self, msg):
        self.distance = msg.data
        self.make_decision()

    def direction_callback(self, msg):
        self.direction = msg.data
        self.make_decision()

    def make_decision(self):
        if self.distance is None or self.direction is None:
            return

        if self.distance > 100:
            decision = 'Continue'
        elif self.distance > 10:
            if self.direction == 'left':
                decision = 'Steer left'
            elif self.direction == 'right':
                decision = 'Steer right'
            else:
                decision = random.choice(
                    ['Steer left', 'Steer right']
                )
        else:
            decision = 'Stop'

        self.get_logger().info(
            f'Distance: {self.distance} cm | '
            f'Obstacle: {self.direction} | '
            f'Decision: {decision}'
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
