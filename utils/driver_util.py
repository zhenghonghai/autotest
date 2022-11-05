from utils import config_util
from selenium import webdriver


def init_driver(path):
    driver_path = config_util.get_config(path)["chrome"]["path"]
    driver = webdriver.Chrome(driver_path)
    driver.maximize_window()
    return driver
