import 
from rclpy.node import Node
from std_srvs.srv import Trigger
from datetime import datetime

def main():
    rclpy.init()
    node = Node("date_provider")

    def date_request(request, response):
        current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        response.message = f"現在の日付: {current_date}"
        return response

    srv = node.create_service(Trigger, "get_date", date_request)

    node.get_logger().info("日付提供サービス 'get_date' を起動しました")
    rclpy.spin(node)

    node.destroy_service(srv)
    rclpy.shutdown()



if __name__ == "__main__":
    main()
