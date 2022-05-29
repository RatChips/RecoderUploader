# TODO

1. 写完const.WebhookData
2. 实现两个dataclass的工厂方法
3. 在utils中实现获取直播间封面的函数
4. 用https://pypi.org/project/biliup/ 实现上传到b站
5. 两个线程：web服务（接收webhook转WebhookData）+上传视频
6. 线程通信使用queue

# 难点
1. 线程通信(queue的使用)