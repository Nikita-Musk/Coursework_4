from forex_python.converter import CurrencyRates, RatesNotAvailableError


def convert_currency(amount: float, currency: str):
    """
    Функция для конвертации валюты
    """
    cr = CurrencyRates()
    # Пытаемся выполнить конвертацию валюты, возвращаем сумму в рублях
    try:
        return cr.convert(currency, 'RUB', amount)
    # Возвращаем значение по умолчанию, если курс валюты не доступен
    except RatesNotAvailableError:
        return 0