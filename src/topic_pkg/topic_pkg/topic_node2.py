import rclpy
from rclpy.node import Node
from std_msgs.msg import String
class TopicNode2(Node):
    def __init__(self):
        super().__init__('topic_node2')
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
    topic_node2 = TopicNode2()
    rclpy.spin(topic_node2)
    topic_node2.destroy_node()
    rclpy.shutdown()