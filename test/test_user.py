import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_index_route():
    response = client.get('/users/')
    assert response.status_code == 200


def test_index_route():
    response = client.get('/')
    print(response.content)
    assert response.content == b'{"items":[{"name":"http://loremflickr.com/640/480/food","price":"986.00","is_offer":false,"id":"1"},{"name":"http://loremflickr.com/640/480/food","price":"253.00","is_offer":true,"id":"2"},{"name":"http://loremflickr.com/640/480/food","price":"992.00","is_offer":true,"id":"3"},{"name":"http://loremflickr.com/640/480/food","price":"854.00","is_offer":true,"id":"4"},{"name":"http://loremflickr.com/640/480/food","price":"322.00","is_offer":true,"id":"5"},{"name":"http://loremflickr.com/640/480/food","price":"713.00","is_offer":true,"id":"6"},{"name":"http://loremflickr.com/640/480/food","price":"496.00","is_offer":false,"id":"7"},{"name":"http://loremflickr.com/640/480/food","price":"215.00","is_offer":true,"id":"8"},{"name":"http://loremflickr.com/640/480/food","price":"775.00","is_offer":true,"id":"9"},{"name":"http://loremflickr.com/640/480/food","price":"376.00","is_offer":true,"id":"10"},{"name":"http://loremflickr.com/640/480/food","price":"451.00","is_offer":false,"id":"11"},{"name":"http://loremflickr.com/640/480/food","price":"76.00","is_offer":false,"id":"12"},{"name":"http://loremflickr.com/640/480/food","price":"503.00","is_offer":true,"id":"13"},{"name":"http://loremflickr.com/640/480/food","price":"80.00","is_offer":true,"id":"14"},{"name":"http://loremflickr.com/640/480/food","price":"909.00","is_offer":true,"id":"15"},{"name":"http://loremflickr.com/640/480/food","price":"388.00","is_offer":true,"id":"16"},{"name":"http://loremflickr.com/640/480/food","price":"604.00","is_offer":true,"id":"17"},{"name":"http://loremflickr.com/640/480/food","price":"538.00","is_offer":false,"id":"18"},{"name":"http://loremflickr.com/640/480/food","price":"757.00","is_offer":false,"id":"19"},{"name":"http://loremflickr.com/640/480/food","price":"935.00","is_offer":false,"id":"20"},{"name":"http://loremflickr.com/640/480/food","price":"624.00","is_offer":false,"id":"21"},{"name":"http://loremflickr.com/640/480/food","price":"720.00","is_offer":false,"id":"22"},{"name":"http://loremflickr.com/640/480/food","price":"905.00","is_offer":false,"id":"23"},{"name":"http://loremflickr.com/640/480/food","price":"282.00","is_offer":false,"id":"24"},{"name":"http://loremflickr.com/640/480/food","price":"437.00","is_offer":false,"id":"25"},{"name":"http://loremflickr.com/640/480/food","price":"461.00","is_offer":true,"id":"26"},{"name":"http://loremflickr.com/640/480/food","price":"528.00","is_offer":true,"id":"27"},{"name":"http://loremflickr.com/640/480/food","price":"1.00","is_offer":false,"id":"28"},{"name":"http://loremflickr.com/640/480/food","price":"336.00","is_offer":false,"id":"29"},{"name":"http://loremflickr.com/640/480/food","price":"665.00","is_offer":false,"id":"30"},{"name":"http://loremflickr.com/640/480/food","price":"462.00","is_offer":true,"id":"31"},{"name":"http://loremflickr.com/640/480/food","price":"575.00","is_offer":true,"id":"32"},{"name":"http://loremflickr.com/640/480/food","price":"103.00","is_offer":true,"id":"33"},{"name":"http://loremflickr.com/640/480/food","price":"562.00","is_offer":true,"id":"34"},{"name":"http://loremflickr.com/640/480/food","price":"99.00","is_offer":true,"id":"35"},{"name":"http://loremflickr.com/640/480/food","price":"154.00","is_offer":false,"id":"36"},{"name":"http://loremflickr.com/640/480/food","price":"377.00","is_offer":false,"id":"37"},{"name":"http://loremflickr.com/640/480/food","price":"647.00","is_offer":false,"id":"38"},{"name":"http://loremflickr.com/640/480/food","price":"463.00","is_offer":true,"id":"39"},{"name":"http://loremflickr.com/640/480/food","price":"653.00","is_offer":false,"id":"40"},{"name":"http://loremflickr.com/640/480/food","price":"2.00","is_offer":true,"id":"41"},{"name":"http://loremflickr.com/640/480/food","price":"659.00","is_offer":true,"id":"42"},{"name":"http://loremflickr.com/640/480/food","price":"904.00","is_offer":false,"id":"43"},{"name":"http://loremflickr.com/640/480/food","price":"173.00","is_offer":true,"id":"44"},{"name":"http://loremflickr.com/640/480/food","price":"161.00","is_offer":false,"id":"45"},{"name":"http://loremflickr.com/640/480/food","price":"209.00","is_offer":false,"id":"46"},{"name":"http://loremflickr.com/640/480/food","price":"759.00","is_offer":true,"id":"47"},{"name":"http://loremflickr.com/640/480/food","price":"341.00","is_offer":false,"id":"48"},{"name":"http://loremflickr.com/640/480/food","price":"525.00","is_offer":true,"id":"49"},{"name":"http://loremflickr.com/640/480/food","price":"707.00","is_offer":true,"id":"50"},{"name":"http://loremflickr.com/640/480/food","price":"747.00","is_offer":false,"id":"51"},{"name":"http://loremflickr.com/640/480/food","price":"856.00","is_offer":true,"id":"52"},{"name":"http://loremflickr.com/640/480/food","price":"959.00","is_offer":false,"id":"53"},{"name":"http://loremflickr.com/640/480/food","price":"444.00","is_offer":true,"id":"54"},{"name":"http://loremflickr.com/640/480/food","price":"123.00","is_offer":false,"id":"55"},{"name":"http://loremflickr.com/640/480/food","price":"357.00","is_offer":false,"id":"56"},{"name":"http://loremflickr.com/640/480/food","price":"267.00","is_offer":true,"id":"57"},{"name":"http://loremflickr.com/640/480/food","price":"644.00","is_offer":true,"id":"58"}]}'