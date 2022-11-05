import pytest
import requests


def setup_class(self):
    print('每个类之前执行')


def teardown_class(self):
    print('每个类之后执行')


def setup(self):
    print('用例之前执行')


def teardown(self):
    print('用例之后执行')


def read_yaml():
    return ['哈1', '哈2', '哈3']


@pytest.fixture(scope='function', autouse=False, params=read_yaml(), ids=['h1', 'h2', 'h3'], name='ea')
def exec_assert(request):
    print('在用例之前执行')
    yield request.param
    print('在用例之后执行')


class TestAPI:

    @pytest.mark.parametrize('name', ['哈1', '哈2'])
    def test_api(self, name):
        print(name)
        assert name == '哈1'
