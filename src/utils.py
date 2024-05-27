from src.head_hunter_api import HeadHunterAPI
from src.vacancy import Vacancy
from src.worker import JSONWorker


def user_interaction() -> None:
    """
    Функция для взаимодействия с пользователем. Позволяет искать вакансии на сайте HeadHunter,
    сортировать их, искать по ключевым словам, сохранять и загружать из файла.
    """
    print("Здравствуйте,мы подготовили для вас вакансии с сайта HeadHunter")
    keyword_user: str = input("Введите ключевое слово для поиска вакансий: ")
    # Создание экземпляра класса для работы с API сайтов с вакансиями
    api_hh = HeadHunterAPI()
    # Получение вакансий с hh.ru в формате JSON
    vacancies_info = api_hh.get_vacancies(keyword_user)
    # Преобразование набора данных из JSON в список объектов
    vacancies_object = Vacancy.cast_to_object_list(vacancies_info)

    # Цикл интерфейса для пользователя
    while True:
        print("\nВыберите действие:\n"
              "1. Топ N вакансий\n"
              "2. Поиск вакансий по диапазону зарплат\n"
              "3. Показать все найденные вакансии\n"
              "4. Редактор файла\n"
              "5. Поиск по ключевому слову в описании\n"
              "6. Выйти\n")
        # Проверка правильный ввод
        try:
            choose: int = int(input("Ваш выбор: "))
            if 1 <= choose <= 6:
                # Выбор лучших вакансий
                if choose == 1:
                    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
                    result = sorted(vacancies_object, reverse=True)
                    for obj in result[:top_n]:
                        print(str(obj))
                # Поиск вакансий по диапазону зарплат
                elif choose == 2:
                    salary_range: str = input("Введите диапазон зарплат, через пробел: ")  # Пример: 100000 1500000
                    salary_from, salary_to = salary_range.split(" ")
                    # Фильтрация вакансий
                    filtered_vacancies = [obj for obj in vacancies_object if
                                          int(salary_from) <= obj.salary_from_rub and int(
                                              salary_to) >= obj.salary_to_rub]
                    # Сортировка вакансий
                    result = sorted(filtered_vacancies, reverse=True)
                    for obj in result:
                        print(str(obj))
                # Вывод всех вакансий
                elif choose == 3:
                    for obj in vacancies_object:
                        print(str(obj))
                # Работа с файлом
                elif choose == 4:
                    file_work(vacancies_object)
                # Поиск по ключевому слову
                elif choose == 5:
                    keyword_snippet: str = input("Введите ключевое слово для поиска в описании вакансий: ")
                    filtered_vacancies = [obj for obj in vacancies_object if obj.snippet and keyword_snippet in obj.snippet]
                    for obj in filtered_vacancies:
                        print(str(obj))
                # Выход из цикла
                elif choose == 6:
                    break
            else:
                print("Ошибка: Неверный выбор. Пожалуйста, выберите число от 1 до 6.")
        except ValueError:
            print("Ошибка: Неверный ввод. Пожалуйста, введите целое число.")


def file_work(vacancies_object) -> None:
    """
    Функция для работы с файлом, где хранятся сохраненные вакансии.
    """
    # Цикл интерфейса для пользователя
    while True:
        print("\nВыберите действие:\n"
              "1. Сохранить вакансию\n"
              "2. Сохранить все вакансии\n"
              "3. Удалить вакансию\n"
              "4. Выбрать вакансию\n"
              "5. Выйти\n")
        # Проверка правильный ввод
        try:
            choose: int = int(input("Ваш выбор: "))
            if 1 <= choose <= 5:
                # Сохранение вакансии
                if choose == 1:
                    # Выбор номера вакансии
                    vacancy_number: int = int(input("Введите номер вакансии для сохранения: "))
                    file_worker = JSONWorker('vacancies.json')
                    # Вызов метода для записи вакансии
                    file_worker.add_vacancy(vacancies_object[vacancy_number - 1])
                # Сохранение всех вакансий
                elif choose == 2:
                    file_worker = JSONWorker('vacancies.json')
                    # Вызов метода для записи вакансий
                    file_worker.add_vacancies(vacancies_object)
                # Удаление вакансии
                elif choose == 3:
                    vacancy_number = int(input("Введите номер вакансии для удаления: "))
                    file_worker = JSONWorker('vacancies.json')
                    # Вызов метода для удаления вакансии
                    file_worker.del_vacancy(vacancies_object[vacancy_number - 1])
                # Выбор по слову
                elif choose == 4:
                    keyword_snippet = input("Введите ключевое слово для поиска в описании вакансий: ")
                    file_worker = JSONWorker('vacancies.json')
                    # вызов метода для поиска слова
                    result = file_worker.select_vacancy(keyword_snippet)
                    for vacancy in result:
                        print(vacancy)
                elif choose == 5:
                    break
            else:
                print("Ошибка: Неверный выбор. Пожалуйста, выберите число от 1 до 5.")
        except ValueError:
            print("Ошибка: Неверный ввод. Пожалуйста, введите целое число.")