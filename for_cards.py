import numpy as np
cards = np.random.choice(range(1, 22), size=4, replace=False)
print(f'Дима - {cards[0]}, {cards[2]}, Олег - {cards[1]}, {cards[3]}')