import pytest

from utils.yaml_util import *

if __name__ == '__main__':
    # data = {'date': '2022-11-02', 'age': 28}
    # write_yaml(data)
    # age = read_yaml('age')
    # update_yaml('age', 30)
    pytest.main()
    os.system('allure generate ./temps -o ./reports --clean')
