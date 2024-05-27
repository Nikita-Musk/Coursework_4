import requests
from abc import ABC, abstractmethod


class BaseAPI(ABC):
    """
    Абстрактный класс для работы с API вакансий
    """
    @abstractmethod
    def get_vacancies(self, keyword: str) -> list[dict]:
        """
        Метод для получения вакансий по ключевому слову
        """
        pass


class HeadHunterAPI(BaseAPI):
    """
    Класс для работы с API HeadHunter
    """

    def __init__(self):
        """
        Инициализация атрибутов класса
        """
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 50}
        self.vacancies = []

    def get_vacancies(self, keyword: str) -> list[dict]:
        """
        Метод для получения вакансий по ключевому слову
        """
        self.params.update({"text": keyword})
        # Цикл для получения вакансий со следующих страниц
        while self.params.get('page') != 10:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1
        return self.vacancies
