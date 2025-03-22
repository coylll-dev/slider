from typing import Tuple, Dict

def slider(out: bool=False, length: int=10, position: int=2, curs: str = "O") -> Tuple[str, Dict[str, int]]:
    """Переменные требующиеся для работы ползунка"""
    isTwo: bool = False
    isEnd: bool = False
    polzunok: str = ""
    countSliders = 1
    TempLength = length
    TempPosition = position

    """Проверка на то что длина ползунка четная, и последующие действия"""
    if length % 2 == 0:
        isTwo = True
        countSliders: int = 2
        TempLength -= 1

    if position == TempLength+1:
        isEnd = True
    
    """Корректировка position, если оно выходит за пределы длины"""
    if position > TempLength:
        position = TempLength

    """Создание ползунка"""
    for i in range(1, TempLength + 1):
        if i == position:
            if isEnd:
                if out: print("-", end="")
                polzunok += "-"
            if out: print(curs, end="")
            polzunok += curs
            if isTwo and not isEnd:
                """Если слайдер состоит из двух символов"""
                if out: print(curs, end="")
                polzunok += curs
        else:
            if out: print("-", end="")
            polzunok += "-"
    """Переход на новую строку"""
    if out: print()

    cursor = {'value': TempPosition, 'length': length, 'countSliders': countSliders, 'result': polzunok}

    return polzunok, cursor


if __name__ == "__main__":
    """Тута вводим длину ползунка"""
    length = int(input("Enter the length of slider: "))
    while True:
        try:
            value = input("Enter the value of slider: ")
            """Че число или нет?"""
            if value.isdigit():
                value = int(value)
                slider(out=True, length=length, position=value)
            
        except KeyboardInterrupt:
            print("Exit...")
            exit(0)