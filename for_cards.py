import numpy as np
regole = np.random.choice(range(1, 37), size=2, replace=False)
esercizii = np.random.choice(range(1, 7), size=2, replace=False)
print(f'Дима: правила - {regole[0]}, упражнения - {esercizii[0]}; \nОлег: правила - {regole[1]}, упражнения - {esercizii[1]}')