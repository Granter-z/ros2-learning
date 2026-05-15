import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from my_interfaces.action import MYFibonacci


class FibonacciClient(Node):
    def __init__(self):
        super().__init__('fibonacci_client')
        self.action_client = ActionClient(self, Fibonacci, 'fibonacci')
        self.get_logger().info('动作客户端已启动，等待服务器...')

    def send_goal(self, order):
        goal = Fibonacci.Goal()
        goal.order = order

        self.action_client.wait_for_server()

        self.get_logger().info(f'发送目标: 计算第 {order} 个斐波那契数')

        future = self.action_client.send_goal_async(
            goal,
            feedback_callback=self.feedback_callback
        )

        # 等待目标被接受
        rclpy.spin_until_future_complete(self, future)
        goal_handle = future.result()

        if not goal_handle:
            self.get_logger().error('目标被拒绝')
            return None

        # 等待结果
        result_future = goal_handle.get_result_async()
        rclpy.spin_until_future_complete(self, result_future)
        result = result_future.result()

        self.get_logger().info(f'最终结果: {result.result.sequence}')
        return result.result

    def feedback_callback(self, feedback_msg):
        self.get_logger().info(f'反馈: {feedback_msg.feedback.sequence}')


def main(args=None):
    rclpy.init(args=args)
    node = FibonacciClient()
    node.send_goal(10)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
