import rclpy
from rclpy.node import Node

class ParamNode(Node):
    def __init__(self):
        super().__init__('param_node')
        self.declare_parameter('speed', 5.0)
        speed = self.get_parameter('speed').value
        self.get_logger().info(f'速度: {speed}')
        self.timer = self.create_timer(speed, self.timer_callback)
    def timer_callback(self):
        self.get_logger().info('节点运行中...')

def main(args=None):
    rclpy.init(args=args)
    node = ParamNode()
    rclpy.spin(node)
    rclpy.shutdown()
if __name__ == '__main__':
    main()