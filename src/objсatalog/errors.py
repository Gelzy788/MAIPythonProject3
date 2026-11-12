class CatalogError(Exception):
    """ Родительский класс ошибки для всей программы
    """

class InvalidItemError(CatalogError):
    """ Ошибка неверной сущности
    """
    def __init__(self, message: str = "Неверно задана сущность"):
        super().__init__(message)


class DuplicateIdError(CatalogError):
    """ Ошибка дублирования id сущности
    """
    def __init__(self, message: str = "Два одинаковых id у разных сущностей"):
        super().__init__(message)

class ItemNotFoundError(CatalogError):
    """ Ошибка ненахождения объекта
    """
    def __init__(self, message: str = "Объект не найден"):
        super().__init__(message)

class UnsupportedVersionError(CatalogError):
    """ Неподдерживаемая версия формата json-файла
    """
    def __init__(self, message: str = "Неподдерживаемый формат json"):
        super().__init__(message)

class CorruptedFileError(CatalogError):
    """ Ошибка поврежденного файла
    """
    def __init__(self, message: str = "На фход подан сломанный файл"):
            super().__init__(message)