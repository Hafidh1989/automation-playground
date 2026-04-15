from api.schemas.product_list_rspn_schema import *
from api.schemas.product_detail_schema import *

def test_get_product_list(dummyjson_client):
    response = dummyjson_client.get_product_list(limit=10, skip=0)

    assert response.status_code == 200
    product_list = ProductListResponse(**response.json())
    assert product_list.limit == 10
    # assert no empty title
    for product in product_list.products:
        assert product.title, "Product title should not be empty"
        assert product.price > 0

def test_get_product_detail(dummyjson_client):
    response = dummyjson_client.get_product_detail(1)
    assert response.status_code == 200

    product_detail = ProductDetailResponse(**response.json())
    assert product_detail.title, "Product title should not be empty"
    assert product_detail.price > 0

def test_get_product_with_non_existent_id(dummyjson_client):
    response = dummyjson_client.get_product_detail("abcd")
    assert response.status_code == 404
    assert "not found" in (response.json())["message"]