import os

import yaml


# 读取yaml文件
def read_all_yaml():
    with open(os.getcwd() + '/extract.yaml', encoding='utf-8') as f:
        return yaml.safe_load(f)


# 读取yaml文件
def read_yaml(key):
    with open(os.getcwd() + '/extract.yaml', encoding='utf-8') as f:
        value = yaml.safe_load(f)
        return value[key]


# 写入yaml文件
def write_yaml(data):
    with open(os.getcwd() + '/extract.yaml', encoding='utf-8', mode='a') as f:
        yaml.safe_dump(data, f)


# 更新yaml文件
def update_yaml(key, value):
    data = read_all_yaml()
    data[key] = value
    clear_yaml()
    write_yaml(data)


# 清空yaml文件
def clear_yaml():
    with open(os.getcwd() + '/extract.yaml', encoding='utf-8', mode='w') as f:
        f.truncate()
