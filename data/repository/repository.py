# importing the requests library
import requests

# api-endpoint
from data.repository.product_parser import parse_product

URL = "https://fakestoreapi.com/products"


def get_product_list():
    r = requests.get(url=URL)
    data = r.json()
    product_list = []
    for product_json in data:
        product_list.append(parse_product(product_json))

    return product_list

