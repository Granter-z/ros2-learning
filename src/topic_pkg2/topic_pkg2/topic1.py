import rclpy
from rclpy.node import Node
from my_interfaces.msg import Student   
class StudentPublisher(Node):
    def __init__(self):
        super().__init__('student_publisher')
        self.publisher_ = self.create_publisher(Student, 'student_info', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = Student()
        msg.name = '张三'
        msg.age = 20 + self.i
        msg.score = 90.0 + self.i
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: name: {msg.name}, age: {msg.age}, score: {msg.score}')
        self.i += 1
def main(args=None):
    rclpy.init(args=args)
    student_publisher = StudentPublisher()
    rclpy.spin(student_publisher)
    student_publisher.destroy_node()
    rclpy.shutdown()