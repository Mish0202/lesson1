product = {
    'name' : 'Iphone Xs',
    'stock' : 5,
    'price' : 65000.0
}
print(product)

product['stock'] = 10
print(product)
product['memory'] = 64
print(product)
print(product.get('name1', 0))
del product['memory']
print(product)
