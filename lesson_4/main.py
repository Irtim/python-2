# from random import choice
# class Marker:
#     def __init__(self, color, size):
#         self.color = color
#         self.size = size
#
#     def throw(self, name, f):
#         a = 'Попал'
#         b = 'Не попал'
#         f = choice((a, b))
#         print(f'Ты {f} в {name}')
#
# mark = Marker('Красный', 20)
# mark_2 = Marker('Синий', 10)
#
# mark.throw('Гена')

# class calculator:
#     def __init__(self):
#         self.result = 0
#
#     def plus(self, amount):
#         self.result += amount
#
#     def minus(self, amount):
#         self.minus -= amount
#     def multiply(self, amount):
#         self.multiply *= amount
#     def expoinii(self, amount):
#         self.expoinii //= amount
#     def division(self, amount):
#         self.division /= amount
#     def clear(self):
#         self.result = 0
#
#     def show_result(self):
#         print(self.result)
#
# calc = calculator()
# calc.plus(5)
# calc.show_result()
# calc.clear()
# calc.show_result()

# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def get_area(self):
#         return self.width + self.height
#
#     def get_perimetr(self):
#         return (self.width + self.height) * 2
#
# class Square(Rectangle):
#     def __init__(selfm, width):
#         super().__init__(width,width)
#
#
# r = Rectangle(5,10)
# print(r.get_area())
# print(r.get_perimetr())
#
# r = super(5)
# print(r.get_area())
# print(r.get_perimetr())
# class Circie:
#     def __init__(self, radius):
#         self.radius = radius
#
#     def get_area(self):
#         return self.radius ** 2 * 3.14159
#     def get_perimetr(self):
#         return 2 * 3.14159 * self.radius
#
# shapes = [Rectangle(5, 10), Square(15), Circie(7)]
# for shape in shapes:
#     print(shape.__class__.__name,'Площадь:', shape.get_area() )
#     print(shape.__class__.__name, 'Периметр:', shape.get_perimetr())
# class Chetchik:
#     def __init__(self):
#         self.da = 0
#
#     def up(self):
#         self.da += 1
#     def down(self):
#         self.da -= 1
#     def clear(self):
#         self.da = 0
#     def show(self):
#         print(self.da)
#
#
# c = Chetchik()
# c.up()
# c.up()
# c.up()
# c.show()
# c.down()
# c.show()

class Question:
    def __init__(self, message):
        self.message = message
        self.achivment = False

    def set_achivment(self, status):
        self.achivment = status

class QuestionList:
    def __init__(self):
        self.question_list = []

    def get_question_by_index(self, index):
        return  self.question_list[index]

    def add(self, message):
        self.question_list.append(Question(message))

    def  remove(self, question):
        self.question_list.remove(question)

    def show_list(self):
        i = 0
        for quest in self.question_list:
            i += 1
            print(f'Task: {quest.message} | status: {quest.status}')

q_list = QuestionList()
