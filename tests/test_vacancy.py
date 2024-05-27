from src.vacancy import Vacancy


def test_vacancy_init():
    """
    Тест инициализации класса Vacancy
    """
    vacancy_data = {
        "name": "Тестовая вакансия",
        "salary": {
            "from": 50000,
            "to": 70000,
            "currency": "RUB"
        },
        "alternate_url": "https://test.ru/vacancy",
        "snippet": {
            "requirement": "Требования к тестовой вакансии"
        }
    }
    vacancy = Vacancy(vacancy_data)
    assert vacancy.title == "Тестовая вакансия"
    assert vacancy.salary_from == 50000
    assert vacancy.salary_to == 70000
    assert vacancy.currency == "RUB"
    assert vacancy.salary_from_rub == 50000
    assert vacancy.salary_to_rub == 70000
    assert vacancy.vacancy_url == "https://test.ru/vacancy"
    assert vacancy.snippet == "Требования к тестовой вакансии"

def test_vacancy_no_salary():
    """
    Тест создания вакансии без указания зарплаты
    """
    vacancy_data = {
        "name": "Тестовая вакансия без зарплаты",
        "alternate_url": "https://test.ru/vacancy",
        "snippet": {
            "requirement": "Требования к тестовой вакансии без зарплаты"
        }
    }
    vacancy = Vacancy(vacancy_data)
    assert vacancy.title == "Тестовая вакансия без зарплаты"
    assert vacancy.salary_from == 0
    assert vacancy.salary_to == 0
    assert vacancy.currency == "N/A"
    assert vacancy.salary_from_rub == 0
    assert vacancy.salary_to_rub == 0
    assert vacancy.vacancy_url == "https://test.ru/vacancy"
    assert vacancy.snippet == "Требования к тестовой вакансии без зарплаты"

def test_vacancy_str():
    """
    Тест строкового представления класса Vacancy
    """
    vacancy_data = {
        "name": "Тестовая вакансия",
        "salary": {
            "from": 50000,
            "to": 70000,
            "currency": "RUB"
        },
        "alternate_url": "https://test.ru/vacancy",
        "snippet": {
            "requirement": "Требования к тестовой вакансии"
        }
    }
    vacancy = Vacancy(vacancy_data)
    assert str(vacancy) == ("Вакансия Тестовая вакансия. Зарплата от 50000 RUB до 70000 RUB. Ссылка на вакансию: "
                            "https://test.ru/vacancy. Требования: Требования к тестовой вакансии")

def test_vacancy_lt():
    """
    Тест сравнения вакансий по зарплате
    """
    vacancy1_data = {
        "name": "Вакансия 1",
        "salary": {
            "from": 50000,
            "to": 70000,
            "currency": "RUB"
        },
        "alternate_url": "https://test.ru/vacancy1",
        "snippet": {
            "requirement": "Требования к вакансии 1"
        }
    }
    vacancy2_data = {
        "name": "Вакансия 2",
        "salary": {
            "from": 60000,
            "to": 80000,
            "currency": "RUB"
        },
        "alternate_url": "https://test.ru/vacancy2",
        "snippet": {
            "requirement": "Требования к вакансии 2"
        }
    }
    vacancy3_data = {
        "name": "Вакансия 3",
        "salary": {
            "from": 70000,
            "to": 90000,
            "currency": "RUB"
        },
        "alternate_url": "https://test.ru/vacancy3",
        "snippet": {
            "requirement": "Требования к вакансии 3"
        }
    }
    vacancy1 = Vacancy(vacancy1_data)
    vacancy2 = Vacancy(vacancy2_data)
    vacancy3 = Vacancy(vacancy3_data)
    assert vacancy1 < vacancy2
    assert vacancy2 < vacancy3
    assert not vacancy1 > vacancy2
    assert not vacancy2 > vacancy3
    assert not vacancy1 > vacancy3

def test_vacancy_to_dict():
    """
    Тест конвертации объекта Vacancy в словарь
    """
    vacancy_data = {
        "name": "Тестовая вакансия",
        "salary": {
            "from": 50000,
            "to": 70000,
            "currency": "RUB"
        },
        "alternate_url": "https://test.ru/vacancy",
        "snippet": {
            "requirement": "Требования к тестовой вакансии"
        }
    }
    vacancy = Vacancy(vacancy_data)
    assert vacancy.to_dict() == {
        'title': 'Тестовая вакансия',
        'salary_from': 50000,
        'salary_to': 70000,
        'currency': 'RUB',
        'vacancy_url': 'https://test.ru/vacancy',
        'snippet': 'Требования к тестовой вакансии'
    }
