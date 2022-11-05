import requests


class SendRequest:
    # 会话，会话对象能够自动的管理cookie关联
    sess = requests.session()

    def send_requests(self, method, url, **kwargs):
        return SendRequest.sess.request(method, url, **kwargs)
