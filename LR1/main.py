import sys
import math


def get_coef(index, prompt):
    '''
    Читаем коэффициент из командной строки или вводим с клавиатуры
    Args:
        index (int): Номер параметра в командной строке
        prompt (str): Приглашение для ввода коэффицента
    Returns:
        float: Коэффициент квадратного уравнения
    '''
    try:
        # Пробуем прочитать коэффициент из командной строки
        coef_str = sys.argv[index]
        coef = float(coef_str)
    except:
        # Проверяем на число
        while True:
            try:
                # Вводим с клавиатуры
                print(prompt, end="")
                coef_str = input()
                # Переводим строку в действительное число
                coef = float(coef_str)
            except:
                print("Введите число!")
            else:
                break

    return coef


def get_roots(a, b, c):
    '''
    Вычисление корней квадратного уравнения
    Args:
        a (float): коэффициент А
        b (float): коэффициент B
        c (float): коэффициент C
    Returns:
        result[float]: Список корней
    '''
    preresult = []
    result = set()
    D = b * b - 4 * a * c
    if D == 0.0:
        preresult.append(-b / 2.0 * a)
    elif D > 0.0:
        root1 = (-b + D**0.5) / (2.0 * a)
        root2 = (-b - D**0.5) / (2.0 * a)
        if root1 >= 0.0:
            preresult.append(root1)
        if root2 >= 0.0:
            preresult.append(root2)
    for root in preresult:
        result.add(root ** 0.5)
        result.add(-root ** 0.5)

    return result


def main():
    '''
    Основная функция
    '''
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    # Вычисление корней
    roots = list(get_roots(a, b, c))
    # Вывод корней
    len_roots = len(roots)
    if len_roots == 0:
        print("Нет корней")
    if len_roots == 1:
        print(f"Один корень: {roots[0]}")
    if len_roots == 2:
        print(f"Два корня: {roots[0]} и {roots[1]}")
    if len_roots == 3:
        print(f"Три корня: {roots[0]}, {roots[1]} и {roots[2]}")
    if len_roots == 4:
        print(f"Четыре корня: {roots[0]}, {roots[1]}, {roots[2]} и {roots[3]}")


# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()
