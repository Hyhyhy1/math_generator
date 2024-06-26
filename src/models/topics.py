from enum import Enum

'''
Topics:
"Элементы линейной алгебры и аналитическая геометрия" = 0
"Введение в математический анализ" = 1
"Дифференциальное исчисление функции одной переменной" = 2
"Дифференциальное исчисление функции нескольких переменных" = 3

Elements:
topic = 0:
    Матрицы = 0
    Определители = 1
    Обратная матрица = 2
    Ранг = 3
    Матричные уравнения = 4
    Системы линейных уравнений = 5
    Метод матричного исчисления = 6
    Формулы Крамера = 7
    Метод Гаусса = 8
    Скалярное, векторное, смешанное произведение векторов = 9
    Прямая на плоскости = 10
    Прямая и плоскость в пространстве = 11
    Кривые второго порядка = 12
    Поверхности второго порядка = 13

topic = 1:
    Комплексные числа и действия над ними = 0
    Понятие функции = 1
    Основные свойства функции = 2
    Предел последовательности = 3
    Предел функции = 4
    Непрерывность функции = 5

topic = 2:
    Производная функции = 0
    Дифференциал функции = 1
    Правила дифференцирования = 2
    Производные высших порядков = 3
    Правило Лопиталя = 4
    Экстремум функции = 5
    Выпуклость, вогнутость = 6 
    Асимптоты = 7 
    Применение производной для исследования функций = 8
    Формула Тейлора = 9

topic = 3:
    Частные производные = 0
    Дифференцирование функций нескольких переменных = 1
    Экстремум функции нескольких переменных: локальный, глобальный, условный экстремум = 2
    Касательная плоскость и нормаль к поверхности = 3
    Производная по направлению = 4
    Градиент = 5

'''
class ExtendedEnum(Enum):

    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))

class First_Topic(str, ExtendedEnum):
    none = "None"
    matrix = "Матрицы"
    determinant = "Определители"
    inbertible_matrix = "Обратная матрица"
    rank = "Ранг"
    matrix_equation = "Матричные уравнения"
    linear_equation_system = "Системы линейных уравнений"
    matrix_method = "Метод матричного исчисления"
    cramer = "Формулы Крамера"
    gaussian = "Метод Гаусса"
    vector_multiplication = "Скалярное, векторное, смешанное произведение векторов"
    line_in_plane = "Прямая на плоскости"
    line_plane_space = "Прямая и плоскость в пространстве"
    conic_section = "Кривые второго порядка"
    second_surface = "Поверхности второго порядка"

class Second_Topic(str, ExtendedEnum):
    complex_numbers = "Комплексные числа и действия над ними"
    function = "Понятие функции"
    function_propetries = "Основные свойства функции"
    sequence_limit = "Предел последовательности"
    function_limit = "Предел функции"
    сontinuous_function = "Непрерывность функции"

class Third_Topic(str, ExtendedEnum):
    derivative = "Производная функции"
    differential = "Дифференциал функции"
    derivation_rule = "Правила дифференцирования"
    high_derivative = "Производные высших порядков"
    lopital_rule = "Правило Лопиталя"
    extremum = "Экстремум функции"
    convex_function = "Выпуклость, вогнутость"
    asymptote = "Асимптоты"
    function_solving = "Применение производной для исследования функций"
    taylor = "Формула Тейлора"

class Forth_Topic(str, ExtendedEnum):
    partial_derivative = "Частные производные"
    differential_vars = "Дифференцирование функций нескольких переменных"
    extremum_vars = "Экстремум функции нескольких переменных: локальный, глобальный, условный экстремум"
    tangent = "Касательная плоскость и нормаль к поверхности"
    directional_derivative = "Производная по направлению"
    gradient = "Градиент"


topics = {
    'first_topic' : First_Topic.list(),
    'second_topic' : Second_Topic.list(),
    'third_topic' : Third_Topic.list(),
    'forth_topic' : Forth_Topic.list()
}

# [
# {
#     topic: "Элементы линейной алгебры и аналитическая геометрия",
#     subtopic : "Матрицы",
#     complexity : "Сложная",
#     count: 10,
# },
# {
#     topic : "Матрицы",
#     complexity : "Сложная",
#     count: 10,
# }
# ]