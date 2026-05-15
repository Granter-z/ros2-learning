import rclpy
from rclpy.node import Node
from std_msgs.msg import String
class TopicNode1(Node):
    def __init__(self):
        super().__init__('topic_node1')
        self.publisher_ = self.create_publisher(String, 'topic', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        msg.data = 'Hello, world! %d' % self.i
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1
def main(args=None):
    rclpy.init(args=args)
    topic_node1 = TopicNode1()
    rclpy.spin(topic_node1)
    topic_node1.destroy_node()
    rclpy.shutdown()
