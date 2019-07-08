from librip.iterators import Unique
from librip.gens import gen_random

data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
data2 = gen_random(1, 3, 10)


print('{} \n \n{}'.format(next(Unique(data1)), next(Unique(data2))))
