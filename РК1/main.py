# используется для сортировки
from operator import itemgetter


class Сhp:
    """Раздел"""

    def __init__(self, id, n1, ws, doc_id):
        self.id = id
        self.n1 = n1
        self.ws = ws
        self.doc_id = doc_id


class Doc:
    """Документ"""

    def __init__(self, id, n2):
        self.id = id
        self.n2 = n2


class СhpDoc:
    """
    'Разделы документа' для реализации
    связи многие-ко-многим
    """

    def __init__(self, doc_id, сhp_id):
        self.doc_id = doc_id
        self.сhp_id = сhp_id


# Документы
docs = [
    Doc(1, 'Рубежный контроль по БКИТ'),
    Doc(2, 'Домашнее задание по Правоведению'),
    Doc(3, 'Отчёт по практике УПСП'),
    Doc(4, 'Лекция по Экологии'),
    Doc(5, 'Курсовая работа по АСОИУ'),
    Doc(6, 'Ответы к РК'),
]

# Разделы
сhps = [
    Сhp(1, 'Содержание', 159, 1),
    Сhp(2, 'Введение', 255, 2),
    Сhp(3, 'Основная часть', 1532, 3),
    Сhp(4, 'Заключение', 199, 3),
    Сhp(5, 'Приложение', 532, 3),
]

сhps_docs = [
    СhpDoc(1, 1),
    СhpDoc(2, 2),
    СhpDoc(3, 3),
    СhpDoc(3, 4),
    СhpDoc(3, 5),

    СhpDoc(1, 1),
    СhpDoc(2, 2),
    СhpDoc(3, 3),
    СhpDoc(3, 4),
    СhpDoc(3, 5),
]

def main():
    """Основная функция"""

    # Соединение данных один-ко-многим
    one_to_many = [(с.n1, с.ws, d.n2)
                   for d in docs
                   for с in сhps
                   if с.doc_id == d.id]

    # Соединение данных многие-ко-многим
    many_to_many_temp = [(d.n2, cd.doc_id, cd.сhp_id)
                          for d in docs
                          for cd in сhps_docs
                          if d.id == cd.doc_id]

    # many_to_many = [(c.n1, c.ws, doc_n2)
    #                 for doc_n2, doc_id, chp_id in many_to_many_temp
    #                 for c in сhps if c.id == chp_id]

    # print('Задание А1')
    # res_11 = sorted(one_to_many, key=itemgetter(2))
    # print(res_11)
    #
    # print('\nЗадание А2')
    # res_12_unsorted = []
    # # Перебираем все отделы
    # for d in deps:
    #     # Список сотрудников отдела
    #     d_emps = list(filter(lambda i: i[2] == d.name, one_to_many))
    #     # Если отдел не пустой
    #     if len(d_emps) > 0:
    #         # Зарплаты сотрудников отдела
    #         d_sals = [sal for _, sal, _ in d_emps]
    #         # Суммарная зарплата сотрудников отдела
    #         d_sals_sum = sum(d_sals)
    #         res_12_unsorted.append((d.name, d_sals_sum))
    #
    # # Сортировка по суммарной зарплате
    # res_12 = sorted(res_12_unsorted, key=itemgetter(1), reverse=True)
    # print(res_12)
    #
    # print('\nЗадание А3')
    # res_13 = {}
    # # Перебираем все отделы
    # for d in deps:
    #     if 'отдел' in d.name:
    #         # Список сотрудников отдела
    #         d_emps = list(filter(lambda i: i[2] == d.name, many_to_many))
    #         # Только ФИО сотрудников
    #         d_emps_names = [x for x, _, _ in d_emps]
    #         # Добавляем результат в словарь
    #         # ключ - отдел, значение - список фамилий
    #         res_13[d.name] = d_emps_names
    #
    # print(res_13)


if __name__ == '__main__':
    main()

