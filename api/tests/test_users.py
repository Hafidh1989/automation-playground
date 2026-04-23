from api.schemas.user_schema import User, UserListResponse


def test_get_users_list(dummyjson_client):
    response = dummyjson_client.get_users(limit=10, skip=0)

    assert response.status_code == 200

    user_list = UserListResponse(**response.json())

    assert user_list.limit == 10
    assert len(user_list.users) > 0
    assert user_list.total > 0


def test_get_single_user(dummyjson_client):
    response = dummyjson_client.get_single_user(user_id=1)

    assert response.status_code == 200

    user = User(**response.json())

    assert user.id == 1
    assert user.username == "emilys"