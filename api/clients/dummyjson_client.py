from typing import Any

import requests


class DummyJsonClient:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.default_headers = {
            "Content-Type": "application/json"
        }

    def get_users(self, limit: int = 30, skip: int = 0) -> requests.Response:
        return requests.get(
            f"{self.base_url}/users",
            params={"limit": limit, "skip": skip},
            headers=self.default_headers,
            timeout=30,
        )

    def get_single_user(self, user_id: int) -> requests.Response:
        return requests.get(
            f"{self.base_url}/users/{user_id}",
            headers=self.default_headers,
            timeout=30,
        )

    def login(self, payload: dict[str, Any]) -> requests.Response:
        return requests.post(
            f"{self.base_url}/auth/login",
            json=payload,
            headers=self.default_headers,
            timeout=30,
        )