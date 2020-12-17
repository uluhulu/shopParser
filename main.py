from terminaltables import AsciiTable

from data.repository.repository import get_product_list
from data.util import TableIt


def print_productList():
    product_list = get_product_list()
    tableOfProducts = [['product', 'description', 'price']]
    for product in product_list:
        tableOfProducts.append([product.title, product.description, product.price])

    table = AsciiTable(tableOfProducts)
    print(table.table)

print_productList()