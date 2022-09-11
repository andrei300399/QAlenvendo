import pytest
from .api_client import ApiClient

HOST_API = 'https://www.lenvendo.ru/api/'


@pytest.fixture(scope="session")
def api_client():
    return ApiClient(HOST_API)
