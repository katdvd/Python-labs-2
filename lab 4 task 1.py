# TODO: описать базовый класс


class MusicalInstrument:
     """
     Базовый класс для музыкальных инструментов.

     Атрибуты:
         name (str): Название инструмента.
         family (str): Семейство инструментов (например, струнные, духовые).
         material (str): Материал, из которого изготовлен инструмент.
         _is_tuned (bool): Признак того, настроен инструмент или нет. Инкапсулирован,
         потому что не должен меняться напрямую извне.

     Методы:
         __init__: Конструктор класса.
         __str__: Возвращает строковое представление объекта.
         __repr__: Возвращает строковое представление объекта для отладки.
         tune: Метод для настройки инструмента.
         is_tuned: Возвращает текущее состояние настройки.
     """
     def __init__(self, name: str, family: str, material: str) -> None:
         """
         Инициализирует объект MusicalInstrument.

         Args:
             name (str): Название инструмента.
             family (str): Семейство инструментов.
             material (str): Материал инструмента.
         """
         self.name = name
         self.family = family
         self.material = material
         self._is_tuned = False

     def __str__(self) -> str:
         """
         Возвращает строковое представление объекта.

         Returns:
             str: Строковое представление объекта.
         """
         return f"{self.name} ({self.family})"

     def __repr__(self) -> str:
         """
         Возвращает строковое представление объекта для отладки.

         Returns:
              str: Строковое представление объекта для отладки.
         """
         return f"MusicalInstrument(name='{self.name}', family='{self.family}', material='{self.material}')"

     def tune(self) -> None:
         """
         Настраивает инструмент.
         """
         self._is_tuned = True

     def is_tuned(self) -> bool:
         """
         Возвращает состояние настройки инструмента.

         Returns:
             bool: True, если инструмент настроен, иначе False.
         """
         return self._is_tuned

# TODO: описать дочерний класс

    from typing import List, Optional

class StringInstrument(MusicalInstrument):
     """
     Дочерний класс для струнных инструментов.

     Атрибуты:
         name (str): Название инструмента.
         family (str): Семейство инструментов, всегда 'string'.
         material (str): Материал, из которого изготовлен инструмент.
         num_strings (int): Количество струн.
         _is_tuned (bool): Признак того, настроен инструмент или нет.
         tuning (List[str]): Строй инструмента.

     Методы:
         __init__: Конструктор класса.
         __str__: Возвращает строковое представление объекта.
         __repr__: Возвращает строковое представление объекта для отладки.
         tune: Перегруженный метод для настройки струнного инструмента.
         play_note: Имитация игры на одной струне.
         get_tuning: Возвращает текущий строй инструмента.
     """
     def __init__(self, name: str, material: str, num_strings: int, tuning: Optional[List[str]] = None) -> None:
         """
         Инициализирует объект StringInstrument.

         Args:
             name (str): Название инструмента.
             material (str): Материал инструмента.
             num_strings (int): Количество струн.
             tuning (Optional[List[str]]): Строй инструмента.
         """
         super().__init__(name, "string", material)
         self.num_strings = num_strings
         self.tuning = tuning if tuning else []

     def __str__(self) -> str:
         """
         Возвращает строковое представление объекта.

         Returns:
             str: Строковое представление объекта.
         """
         return f"{self.name} ({self.family}, {self.num_strings} strings)"

     def __repr__(self) -> str:
         """
         Возвращает строковое представление объекта для отладки.

         Returns:
             str: Строковое представление объекта для отладки.
         """
         return (f"StringInstrument(name='{self.name}', material='{self.material}', "
                 f"num_strings={self.num_strings}, tuning={self.tuning})")

     def tune(self) -> None:
         """
         Перегруженный метод для настройки струнного инструмента.

         Поскольку настройка струнного инструмента более сложная, чем обычного,
         он дополнительно выводит в консоль информацию о строе.
         """
         super().tune()
         print(f"Настроено {self.name} в строй: {', '.join(self.tuning)}")

     def play_note(self, string_number: int) -> str:
         """
         Имитирует игру на одной струне.

         Args:
             string_number (int): Номер струны.

         Returns:
             str: Строка с имитацией звука струны.
         """
         if self.is_tuned() and 1 <= string_number <= self.num_strings:
             return f"Звучит струна № {string_number} на {self.name}."
         else:
             return f"{self.name} не настроен или указана неверная струна."

     def get_tuning(self) -> List[str]:
         """
         Возвращает текущий строй инструмента.

         Returns:
              List[str]: Список нот, представляющих строй инструмента.
         """
         return self.tuning

 if __name__ == '__main__':
     guitar = StringInstrument("Guitar", "wood", 6, ["E2", "A2", "D3", "G3", "B3", "E4"])
     print(guitar)
     print(repr(guitar))
     print(f"Инструмент настроен: {guitar.is_tuned()}")
     guitar.tune()
     print(f"Инструмент настроен: {guitar.is_tuned()}")
     print(guitar.play_note(3))
     print(guitar.play_note(7))
     print(f"Текущий строй: {guitar.get_tuning()}")

     violin = StringInstrument("Violin", "wood", 4, ["G3", "D4", "A4", "E5"])
     print(violin)
     print(repr(violin))
     print(violin.play_note(1))
     violin.tune()
     print(violin.play_note(1))

     piano = MusicalInstrument("Piano", "keyboard", "wood and metal")
     print(piano)
     print(repr(piano))
     print(piano.is_tuned())
     piano.tune()
     print(piano.is_tuned())