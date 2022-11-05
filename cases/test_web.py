import time

from selenium.webdriver.common.by import By

from utils.config_util import get_config,get_data
from utils.log_util import Logger
from utils.driver_util import init_driver


def test_one():
    # Logger().logger.debug("开始测试")
    # wb = init_driver("configs\\env_test.yaml")
    # wb.get("https://www.baidu.com")
    # wb.save_screenshot('../image/百度.png')
    # if data["name"] == "输入框":
    # wb.find_element(By.ID, data["shuru"]["id"]).send_keys("哈哈")
    # wb.save_screenshot('../image/百度1.png')
    # wb.find_element(By.ID, baidu["sousuo"]["id"]).click()
    # wb.save_screenshot('../image/百度2.png')
    # time.sleep(3)
    # wb.quit()
    # Logger().logger.debug("结束测试")
    locator_map = dict()
    data = get_data("configs\\env_test.yaml")
    locator_map[data[0]["name"]] = data[0]
    for i in range(0, len(data)):
        locator_map[data[i]["name"]] = data[i]
    print(locator_map)
