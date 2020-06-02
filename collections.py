from collections import namedtuple

a = namedtuple('courses', 'name, technology')

b = a('machine learning', 'python')

print(b)
