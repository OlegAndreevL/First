import numpy as np
cards = np.random.choice(range(1, 25), size=4, replace=False)
print(f'Дима - {int(cards[0]), int(cards[1])}, Олег - {int(cards[2]), int(cards[3])}')