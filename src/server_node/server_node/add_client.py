import rclpy
from rclpy.node import Node

from my_interfaces.srv import MyAdd


class AddClient(Node):
    def __init__(self):
        super().__init__('add_client')
        self.client = self.create_client(
            MyAdd,
            'add_two_ints'
        )
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available...')
        self.req = MyAdd.Request()
    def send_request(self, a, b):
        self.req.a = a
        self.req.b = b
        future = self.client.call_async(self.req)
        rclpy.spin_until_future_complete(self, future)
        return future.result()

def main(args=None):
    rclpy.init(args=args)
    node = AddClient()
    response = node.send_request(10, 20)
    node.get_logger().info(
        f'result: {response.result}'
    )

    rclpy.shutdown()


if __name__ == '__main__':
    main()