# Замените "YOUR_BOT_TOKEN" на токен, который вы получили от BotFather
API_TOKEN = '7857746311:AAHK3nmF-JpgbgjH-dmUK41oFv6LAqXHhnY'

# Зададим имя базы данных
DB_NAME = 'quiz_bot.db'

# Глобальный словарь
user_scores = {}

# Структура квиза
quiz_data = [
    {
        'question': 'Что такое Python?',
        'options': ['Язык программирования', 'Тип данных', 'Музыкальный инструмент', 'Змея на английском'],
        'correct_option': 0
    },
    {
        'question': 'Какой тип данных используется для хранения целых чисел?',
        'options': ['int', 'float', 'str', 'natural'],
        'correct_option': 0
    },
    {
        'question': 'Какое расширение имеют файлы языка Python?',
        'options': ['.exe', '.midi', '.doc', '.py'],
        'correct_option': 3
    },
    {
        'question': 'В каком году появился Python?',
        'options': ['1990', '1991', '1992', '1993'],
        'correct_option': 1
    },
    {
        'question': 'Чем известен Гвидо Ван Россум?',
        'options': ['Он изобрёл язык Java', 'Основал Microsoft', 'Взорвал Башни-близнецы в 2001', 'Ничем из перечисленного'],
        'correct_option': 3
    },

    {
        'question': 'Какой тип данных НЕ существует в Python?',
        'options': ['Числа', 'Символы', 'Кортежи', 'Строки'],
        'correct_option': 1
    },

    {
        'question': 'Что выведет следующий код: print(type([1, 2, 3]))',
        'options': ['<class ''tuple''>', '<class ''list''>', 'class ''set''>', '<class ''dict''>'],
        'correct_option': 1
    },

    {
        'question': 'Что делает оператор is в Python?',
        'options': ['Сравнивает значения двух переменных', 'Сравнивает типы переменных', 'Проверяет, указывают ли переменные на один и тот же объект', 'Проверяет, есть ли переменная в области видимости'],
        'correct_option': 2
    },

    {
        'question': 'Какой из этих типов изменяемый (mutable)?',
        'options': ['tuple', 'str', 'int', 'list'],
        'correct_option': 3
    },

      {
        'question': 'Что делает __init__ в классе?',
        'options': ['Удаляет объект', 'Создаёт статическое свойство', 'Выполняется при импорте модуля', 'Инициализирует объект при создании'],
        'correct_option': 3
    },
    
]