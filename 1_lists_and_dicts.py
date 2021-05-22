phones = ['iPhone Xs', 'Samsung Galaxy S10', 'Xiaomi Mi8']

product = {
    'name' : 'Iphone Xs',
    'stock' : 5,
    'price' : 65000.0,
    'recommended': phones,
}

print(product['recommended'][1])
product['recommended'].append('Honor')
print(product)