import pytest
from api.clients.dummyjson_client import DummyJsonClient


@pytest.fixture(scope="session")
def base_url() -> str:
    return "https://dummyjson.com"


@pytest.fixture(scope="session")
def dummyjson_client(base_url: str) -> DummyJsonClient:
    return DummyJsonClient(base_url)