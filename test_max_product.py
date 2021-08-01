import random
from max_product import max_product

array = [x for x in range(0, 201)] # The max product must be 200 * 199 * 198 = 7880400

print("==========================================")
print("# test                          result    ")
print("==========================================")

for test in range(0, 100):
    random.shuffle(array)
    result = max_product(array)
    print(f'{test}                            {result} ')
