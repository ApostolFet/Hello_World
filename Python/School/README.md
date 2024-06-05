#задача

Создать класс Human, который представляет собой человека.
• У человека должно быть имя и пол (мужской/женский).
• У человека должен быть метод introduce, который выводит на экран строку вида "Привет, я мужчина, меня зовут Иван.". Где мужчина/женщина выводится исходя из его пола и так же подставляется имя

Создать подкласс SoftwareDeveloper, который представляет собой человека, пишущего на каком-то языке программирования.
• Кроме основных атрибутов человека у него должен быть указан язык программирования
•Метод introduce, который выводит на экран строку с доп информацией: "Привет, я мужчина, меня зовут Иван. Я пишу на Python".

Создать класс DeveloperSchool, который создает разработчиков из людей.
• Должен быть метод teach, который получает человека и возвращает программиста.
• Каждая школа умеет обучать только одному языку программирования
• Должна быть возможность узнать сколько раз обучались в школе

Создать класс DebugSchool, который создает разработчиков из людей с помощью существующей другой школы
• Должна быть полностью совместимость с классом DeveloperSchool с точки зрения использования
• Дополнительно при обучении надо вывести приветствие человека до и после обучения. То есть в таком виде:
До: Привет, я мужчина, меня зовут Иван.
После: Привет, я мужчина, меня зовут Иван. Я пишу на Python

Создать пару человек, обучить js, переобучить на python с выводом приветствий. Вывести по каждому языку сколько раз было обучение.

Что изучаем:
• Создание классов
• Форматирование строк
• Наследование и вызов доступ к родительским методам
• Полиморфизм, утиная типизация, совместимость объектов разных типов
• Композиция объектов
• Паттерн декоратор

## Запустить программу:

```sh
python main.py
```