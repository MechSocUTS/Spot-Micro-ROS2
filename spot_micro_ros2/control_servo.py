#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class ServoControl(Node):
    def __init__(self):
        super().__init__('servo_controller')
        self.publisher_ = self.create_publisher(Float32, '/servo_angle', 10)

    def publish_angle(self, angle):
        msg = Float32()
        msg.data = float(angle)
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    controller = ServoControl()

    try:
        while rclpy.ok():
            angle = input("Enter angle (0-180) or 'q' to quit: ")
            if angle.lower() == 'q':
                break
            controller.publish_angle(angle)
    except KeyboardInterrupt:
        pass

    controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
