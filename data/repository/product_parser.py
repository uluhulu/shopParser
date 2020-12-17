from data.model.product import Product


def parse_product(productJson) -> Product:
    return Product(productJson['id'],
                   productJson['title'],
                   productJson['price'],
                   productJson['description'],
                   productJson['category'],
                   productJson['image'],
                   )
