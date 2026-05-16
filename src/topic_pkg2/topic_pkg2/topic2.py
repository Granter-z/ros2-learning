import rclpy
from rclpy.node import Node
from my_interfaces.msg import Student
class StudentSubscriber(Node):
    def __init__(self):
        super().__init__('student_subscriber')
        self.subscription = self.create_subscription(
            Student,
            'student_info',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
    def listener_callback(self, msg):
        self.get_logger().info(f'I heard: name: {msg.name}, age: {msg.age}, score: {msg.score}')
def main(args=None):
    rclpy.init(args=args)
    student_subscriber = StudentSubscriber()
    rclpy.spin(student_subscriber)
    student_subscriber.destroy_node()
    rclpy.shutdown()
if __name__ == '__main__':
    main(args=None)