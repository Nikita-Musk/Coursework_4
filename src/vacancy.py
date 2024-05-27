from src.convert_currency import convert_currency


class Vacancy:
    """
    Класс для создания вакансии
    """

    def __init__(self, vacancies_date: dict):
        """
        Инициализация атрибутов класса
        """
        self.title: str = vacancies_date.get("name")
        salary_date = vacancies_date.get("salary")
        if salary_date:
            self.salary_from: int = salary_date.get("from", 0) or 0
            self.salary_to: int = salary_date.get("to", 0) or 0
            self.currency: str = salary_date.get("currency", "N/A") or "N/A"
            self.salary_from_rub: int = convert_currency(self.salary_from, "RUB")
            self.salary_to_rub: int = convert_currency(self.salary_to, "RUB")
        else:
            self.salary_from: int = 0
            self.salary_to: int = 0
            self.currency: str = "N/A"
            self.salary_from_rub: int = 0
            self.salary_to_rub: int = 0
        self.vacancy_url: str = vacancies_date.get('alternate_url')
        self.snippet: str = vacancies_date.get("snippet", {}).get('requirement', "Требования отсутствуют")

    def __str__(self) -> str:
        """
        Строковое представление объекта
        """
        if self.salary_from == 0 and self.salary_to == 0:
            return (f"Вакансия {self.title}. Зарплата не указана. Ссылка на вакансию: {self.vacancy_url}. "
                    f"Требования: {self.snippet}")
        else:
            return (f"Вакансия {self.title}. Зарплата от {self.salary_from} {self.currency} до {self.salary_to} "
                    f"{self.currency}. Ссылка на вакансию: {self.vacancy_url}. Требования: {self.snippet}")

    def __repr__(self) -> str:
        """
        Репрезентация объекта для отладки
        """
        return f"Vacancy('{self.title}', {self.salary_from} - {self.salary_to}, '{self.vacancy_url}', '{self.snippet}'"

    def __lt__(self, other) -> bool:
        """
        Метод сравнения вакансий по зарплате
        """
        if self.salary_to_rub == 0 and other.salary_to_rub != 0:
            return False
        if self.salary_to_rub != 0 and other.salary_to_rub == 0:
            return True
        if self.salary_to_rub == other.salary_to_rub:
            return self.salary_from_rub < other.salary_from_rub
        if self.salary_from_rub == other.salary_from_rub:
            return self.salary_to_rub < other.salary_to_rub
        if self.salary_from_rub > other.salary_from_rub and self.salary_to_rub > other.salary_to_rub:
            return False
        if self.salary_from_rub > other.salary_from_rub and self.salary_to_rub < other.salary_to_rub:
            return True
        if self.salary_from_rub < other.salary_from_rub and self.salary_to_rub < other.salary_to_rub:
            return True
        if self.salary_from_rub < other.salary_from_rub and self.salary_to_rub > other.salary_to_rub:
            return False
        return False

    def to_dict(self) -> dict:
        """
        Метод для конвертации объекта в словарь
        """
        return {
            'title': self.title,
            'salary_from': self.salary_from,
            'salary_to': self.salary_to,
            'currency': self.currency,
            'vacancy_url': self.vacancy_url,
            'snippet': self.snippet
        }

    @classmethod
    def cast_to_object_list(cls, vacancies_data) -> list:
        """
        Классовый метод для конвертации списка словарей в список объектов
        """
        return [cls(vacancy_data) for vacancy_data in vacancies_data]