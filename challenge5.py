def linearSearchProduct(productList,targetProduct):
    indices = []

    for index,product in enumerate(productList):
      if product == targetProduct:
       indices.append(index)

    return indices

#Example Usages:
product =["shoes","boots","loafer","shoes","converse","shoes"]

target = "shoes"
result = linearSearchProduct(product,target)
print(result)