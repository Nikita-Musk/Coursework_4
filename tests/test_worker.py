import os
import json
from src.worker import JSONWorker
from src.vacancy import Vacancy
from config import DATA_PATH


def test_json_worker_init():
    """
    Тест инициализации класса JSONWorker
    """
    json_worker = JSONWorker("test_file.json")
    assert json_worker.file_path == os.path.join(DATA_PATH, "test_file.json")


def test_json_worker_add_vacancy():
    """
    Тест метода add_vacancy класса JSONWorker
    """
    json_worker = JSONWorker("test_file.json")
    with open(json_worker.file_path, 'w', encoding='utf-8') as file:
        json.dump([], file)  # Create the file with an empty list
    vacancy = Vacancy({
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
    })
    json_worker.add_vacancy(vacancy)
    with open(json_worker.file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    assert len(data) == 1

def test_json_worker_add_vacancies():
    """
    Тест метода add_vacancies класса JSONWorker
    """
    json_worker = JSONWorker("test_file.json")
    with open(json_worker.file_path, 'w', encoding='utf-8') as file:
        json.dump([], file)  # Create the file with an empty list
    vacancy1 = Vacancy({
        "name": "Тестовая вакансия 1",
        "salary": {
            "from": 50000,
            "to": 70000,
            "currency": "RUB"
        },
        "alternate_url": "https://test.ru/vacancy1",
        "snippet": {
            "requirement": "Требования к тестовой вакансии 1"
        }
    })
    vacancy2 = Vacancy({
        "name": "Тестовая вакансия 2",
        "salary": {
            "from": 60000,
            "to": 80000,
            "currency": "RUB"
        },
        "alternate_url": "https://test.ru/vacancy2",
        "snippet": {
            "requirement": "Требования к тестовой вакансии 2"
        }
    })
    json_worker.add_vacancies([vacancy1, vacancy2])
    with open(json_worker.file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    assert len(data) == 2
