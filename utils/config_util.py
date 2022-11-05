import os
import yaml


def get_project_dir():
    """
    :return: 返回项目的根路径
    """
    return os.path.dirname(os.path.dirname(__file__))


def get_file_path(path):
    """
    :param path: 传入项目下的文件路径
    :return: 返回文件的绝对路径
    """
    return os.path.join(get_project_dir(), path)


if __name__ == '__main__':
    log = get_file_path('log')
    print(log)
    print('---------------')
    print(os.getcwd() + '/log')


def get_config(path):
    """
    :param path: 传入项目下的文件路径
    :return: 返回yaml文件内容
    """
    f = open(get_file_path(path), encoding='utf8')
    return yaml.safe_load(f)


def get_data(path):
    f = open(get_file_path(path), encoding='utf8')
    return yaml.safe_load(f)["data"]

