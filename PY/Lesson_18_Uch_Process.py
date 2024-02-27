class Data:                             # Класс для хранения тем обучения
    def __init__(self, spisok):
        self.spisok = spisok            # в виде списка
class Teacher:                          # класс учителей
    def __init__(self):
        self.work = 0                   # учет сколько тем и учеников
    def teach_individual(self, info, pupil): # индивидуальное обучение
        pupil.take(info)                # вызов метода ученика получения информации
        self.work += 1
    def teach_group(self, info):        # групповое обучение
        for i in Pupil.group:           # цикл по списку учеников
            i.take(info)                # вызов метода ученика получения инфы
            self.work += 1
class Pupil:                            # класс учеников
    group = []                          # список учеников
    def __init__(self, name):
        self.knowledge = []
        self.name = name
        Pupil.group.append(self)
    def take(self, info):               # метод получения информации
        self.knowledge.append(info)
    def info(self):                     # метод печати, что ученик выучил
        print(self.name, end= ':')
        for i in self.knowledge:
            print(i, end = ', ')
        print()
        
lesson = Data(['class', 'object', 'inheritance', 
	'polymorphism', 'encapsulation'])

marIvanna = Teacher()
vasya = Pupil('Vasya')
petya = Pupil('Petya')

marIvanna.teach_individual(lesson.spisok[2], vasya)
marIvanna.teach_individual(lesson.spisok[0], petya)
marIvanna.teach_group(lesson.spisok[1])

vasya.info()
petya.info()
print(marIvanna.work)
