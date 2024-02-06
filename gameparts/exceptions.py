class FieldIndexError(IndexError):

    def __str__(self) -> str:
        return 'Введено значение за границами игрового поля'
    

class FieldValueError(ValueError):

    def __str__(self) -> str:
        return 'Введеное значение должно содержать только цифры'
    

class CellOccupiedError(Exception):

    def __str__(self) -> str:
        return 'Попытка изменить занятую ячейку'