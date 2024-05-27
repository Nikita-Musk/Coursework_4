import json
import os
from abc import ABC, abstractmethod
from config import DATA_PATH


class BaseWorker(ABC):
    """
    Абстрактный класс для работы с вакансиями
    """

    # Абстрактный метод для добавления вакансии
    @abstractmethod
    def add_vacancy(self, vacancy: any):
        pass

    # Абстрактный метод для удаления вакансии
    @abstractmethod
    def del_vacancy(self, vacancy: any):
        pass

    # Абстрактный метод для добавления вакансий
    @abstractmethod
    def add_vacancies(self, vacancies: any):
        pass

    # Абстрактный метод для поиска вакансии по ключевому слову
    @abstractmethod
    def select_vacancy(self, keyword: str):
        pass


class JSONWorker(BaseWorker):
    """
    Класс для работы с вакансиями в формате JSON
    """

    def __init__(self, file_name: str):
        """
        Инициализация атрибутов класса
        """
        self.file_path = os.path.join(DATA_PATH, file_name)
        self.prepare()

    def prepare(self):
        """
        Метод для инициализации файла, если он не существует
        """
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w', encoding='utf-8') as file:
                json.dump([], file)

    def add_vacancy(self, vacancy: any):
        """
        Метод для добавления вакансии в файл
        """
        with open(self.file_path, 'r+', encoding='utf-8') as file:
            # Читаем данные из файла
            data = json.load(file)
            # Добавляем вакансию в список
            data.append(vacancy.to_dict())
            # Перезаписываем файл
            file.seek(0)
            json.dump(data, file, indent=4)
            file.truncate()

    def add_vacancies(self, vacancies: any):
        """
        Метод для добавления списка вакансий в файл
        """
        with open(self.file_path, 'r+', encoding='utf-8') as file:
            data = json.load(file)
            # Добавляем список вакансий в список
            data.extend([vacancy.to_dict() for vacancy in vacancies])
            file.seek(0)
            json.dump(data, file, indent=4)
            file.truncate()

    def del_vacancy(self, vacancy: any):
        """
        Метод для удаления вакансии из файла
        """
        with open(self.file_path, 'r+', encoding='utf-8') as file:
            data = json.load(file)
            # Удаляем вакансию из списка
            data.remove(vacancy.to_dict())
            file.seek(0)
            json.dump(data, file, indent=4)
            file.truncate()

    def select_vacancy(self, keyword: str):
        """
        Метод для поиска вакансии по ключевому слову
        """
        with open(self.file_path, 'r+', encoding='utf-8') as file:
            with open(self.file_path, 'r+', encoding='utf-8') as file:
                data = json.load(file)
                # Ищем вакансии, содержащие ключевое слово в описании
                result = [vacancy for vacancy in data if
                          'snippet' in vacancy and vacancy['snippet'] is not None and keyword in vacancy['snippet']]
                return result