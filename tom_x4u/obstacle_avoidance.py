import random
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32, String


class ObstacleAvoidance(Node):

    def __init__(self):
        super().__init__('obstacle_avoidance')

        self.distance = None
        self.direction = None
        self.new_distance = False
        self.new_direction = False

        self.distance_subscription = self.create_subscription(
            Float32, '/distance', self.distance_callback, 10
        )
        self.direction_subscription = self.create_subscription(
            String, '/obstacle_direction',
            self.direction_callback, 10
        )

    def distance_callback(self, msg):
        self.distance = msg.data
        self.new_distance = True
        self.make_decision()

    def direction_callback(self, msg):
        self.direction = msg.data
        self.new_direction = True
        self.make_decision()

    def make_decision(self):
        if not self.new_distance or not self.new_direction:
            return

        self.new_distance = False
        self.new_direction = False

        if self.distance > 100:
            decision = 'Continue'
        elif self.distance > 10:
            if self.direction == 'left':
                decision = 'Steer right'
            elif self.direction == 'right':
                decision = 'Steer left'
            else:
                decision = random.choice(
                    ['Steer left', 'Steer right']
                )
        else:
            decision = 'Stop'

        self.get_logger().info(
            f'Distance: {self.distance:.2f} cm | '
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
