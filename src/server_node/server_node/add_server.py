import rclpy
from rclpy.node import Node

from my_interfaces.srv import MyAdd


class AddServer(Node):

    def __init__(self):

        super().__init__('add_server')

        self.srv = self.create_service(
            MyAdd,
            'add_two_ints',
            self.callback
        )

        self.get_logger().info('Service started')

    def callback(self, request, response):

        response.result = request.a + request.b

        self.get_logger().info(
            f'{request.a} + {request.b} = {response.result}'
        )

        return response


def main(args=None):

    rclpy.init(args=args)

    node = AddServer()

    rclpy.spin(node)

    rclpy.shutdown()


if __name__ == '__main__':
    main()