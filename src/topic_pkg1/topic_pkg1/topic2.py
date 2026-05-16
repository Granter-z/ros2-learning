import rclpy
from rclpy.node import Node
from std_msgs.msg import String
class Topic2(Node):
    def __init__(self):
        super().__init__('topic2')
        self.subscription = self.create_subscription(
            String,
            'topic',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)
def main(args=None):
    rclpy.init(args=args)
    topic2 = Topic2()
    rclpy.spin(topic2)
    topic2.destroy_node()
    rclpy.shutdown()
if __name__ == '__main__':
    main()