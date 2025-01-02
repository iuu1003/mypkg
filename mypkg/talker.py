import rclpy
from rclpy.node import Node
from std_srvs.srv import Trigger
from datetime import datetime

class DateNode(Node):

    def __init__(self):
        super().__init__('date_node')
        # サービスを作成。リクエストをTrigger型で受け取り、レスポンスに日付を返す。
        self.srv = self.create_service(Trigger, 'get_current_date', self.get_current_date)

    def get_current_date(self, request, response):
        # 現在の日付を取得
        current_date = datetime.now().strftime('%Y-%m-%d')  # 例: 2025-01-02
        # 日付をレスポンスにセット
        self.get_logger().info(f"現在の日付: {current_date}")
        response.success = True
        response.message = current_date
        return response

def main(args=None):
    rclpy.init(args=args)
    date_node = DateNode()
    rclpy.spin(date_node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

