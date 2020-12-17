class Product():
    def __init__(self,id,title,price,description,category,image):
        self.id = id
        self.title = title
        self.price = price
        self.description = description
        self.category = category
        self.image = image

    def __str__(self):
        return f'Product(id: {self.id},' \
               f' title: {self.title},' \
               f' price: {self.price},' \
               f' descr: {self.description}' \
               f' category: {self.category} )'
