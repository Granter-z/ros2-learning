import math
import rclpy
from rclpy.node import Node

from geometry_msgs.msg import TransformStamped

from tf2_ros import TransformBroadcaster

def quaternion_from_yaw(yaw):

    qx = 0.0
    qy = 0.0

    qz = math.sin(yaw / 2.0)

    qw = math.cos(yaw / 2.0)

    return [qx, qy, qz, qw]

class DynamicTF(Node):

    def __init__(self):

        super().__init__('dynamic_tf_node')

        self.br = TransformBroadcaster(self)

        self.timer = self.create_timer(
            0.1,
            self.broadcast_tf
        )

        self.t = 0.0

    def broadcast_tf(self):

        tf_msg = TransformStamped()

        tf_msg.header.stamp = \
            self.get_clock().now().to_msg()

        tf_msg.header.frame_id = 'world'

        tf_msg.child_frame_id = 'base_link'

        # 圆周运动
        tf_msg.transform.translation.x = math.cos(self.t)

        tf_msg.transform.translation.y = math.sin(self.t)

        tf_msg.transform.translation.z = 0.0

        q = quaternion_from_yaw(self.t)

        tf_msg.transform.rotation.x = q[0]
        tf_msg.transform.rotation.y = q[1]
        tf_msg.transform.rotation.z = q[2]
        tf_msg.transform.rotation.w = q[3]

        self.br.sendTransform(tf_msg)

        self.t += 0.05


def main(args=None):

    rclpy.init(args=args)

    node = DynamicTF()

    rclpy.spin(node)

    rclpy.shutdown()


if __name__ == '__main__':
    main()