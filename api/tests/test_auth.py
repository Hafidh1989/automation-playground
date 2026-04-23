from api.data.payloads import INVALID_LOGIN_PAYLOAD, VALID_LOGIN_PAYLOAD
from api.schemas.auth_schema import LoginResponse


def test_login_success(dummyjson_client):
    response = dummyjson_client.login(VALID_LOGIN_PAYLOAD)

    assert response.status_code == 200

    login_response = LoginResponse(**response.json())

    assert login_response.username == "emilys"
    assert login_response.accessToken
    assert login_response.refreshToken


def test_login_failed_with_invalid_password(dummyjson_client):
    response = dummyjson_client.login(INVALID_LOGIN_PAYLOAD)

    assert response.status_code in [400, 401]
    assert "message" in response.json() or "error" in response.json()