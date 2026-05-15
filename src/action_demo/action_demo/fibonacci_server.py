import time
import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer
from my_interfaces.action import MYFibonacci


class FibonacciServer(Node):
    def __init__(self):
        super().__init__('fibonacci_server')
        self.action_server = ActionServer(
            self,
            Fibonacci,
            'fibonacci',
            self.execute_callback
        )
        self.get_logger().info('动作服务器已启动，等待目标...')

    def execute_callback(self, goal_handle):
        self.get_logger().info(f'收到目标: 计算第 {goal_handle.request.order} 个斐波那契数')

        feedback_msg = Fibonacci.Feedback()
        sequence = [0, 1]

        for i in range(1, goal_handle.request.order):
            sequence.append(sequence[i] + sequence[i - 1])
            feedback_msg.sequence = sequence
            goal_handle.publish_feedback(feedback_msg)
            self.get_logger().info(f'反馈: {feedback_msg.sequence}')
            time.sleep(0.5)

        goal_handle.succeed()

        result = Fibonacci.Result()
        result.sequence = sequence
        self.get_logger().info(f'执行完成: {result.sequence}')
        return result


def main(args=None):
    rclpy.init(args=args)
    node = FibonacciServer()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
