import numpy as np

def random_predict(number: int = 1) -> int:
    """Функция угадывания рандомного числа от 1 до 100.

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0                                                   # счетчик попыток поиска числа
    min_value, max_value = 1, 100
    predict_number = np.random.randint(1, 101)                  # предполагаемое число
    
    while predict_number != number:                             # считаем кол-во попыток найти число с помощью цикла
        count += 1                            
        if predict_number > number:
            max_value = predict_number                          # уменьшаем диапазон поиска в цикле
            predict_number = (max_value + min_value)//2         # берем середину от нового диапазона и начинаем цикл по новой с целью минимизации кол-ва попыток
        elif predict_number < number:
            min_value = predict_number
            predict_number = (max_value + min_value)//2   
               
    return count

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за N подходов угадывает наш алгоритм число

    Args:
        random_predict ([type]): функция угадывания рандомного числа от 1 до 100

    Returns:
        int: среднее количество попыток угадывания
    """
    count_ls = []                                               # в пустой список будем добавлять рез-ты для каждого числа
    np.random.seed(1)                                           # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(200))        # загадали список чисел (не беру больше 200, у меня комп-р отказывается считать почему-то)
    
    for number in random_array:                                 # циклом проходимся по списку чисел, к каждому применяя функцию поиска числа
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls))                              # находим среднее значение из списка, которое и будет результатом
    
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    return(score)

if __name__ == '__main__':
    score_game(random_predict)