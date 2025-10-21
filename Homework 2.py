from bisect import bisect_right


class Person:
    def __init__(self,name,brith_date,occupation,higher_edukation):
        self.name = name
        self.brith_date = brith_date
        self.occupation = occupation
        self.higher_edukation = higher_edukation

    def introduce(self):
        return(f'Имя - {self.name}\n'
        f'День рождения - {self.brith_date}\n'
        f'Занятия - {self.occupation}\n'
        f'Высшее_образование - {self.higher_edukation}')

people1 = Person('Жазир', '2006.03.31', 'Книги', 'среднее')
print(people1.introduce())



class Friend(Person):
    def __init__(self,name,brith_date,occupation,higher_edukation, time_fried):
        Person.__init__(self, name, brith_date, occupation, higher_edukation,)
        self.time_friend = time_fried

    def introduce(self):
        return (f'Имя - {self.name}\n'
                f'День рождения - {self.brith_date}\n'
                f'Занятия - {self.occupation}\n'
                f'Высшее_образование - {self.higher_edukation}\n'
                f'Сколько лет дружим - {self.time_friend}')


class Classmate(Person):
    def __init__(self, name, brith_date, occupation, higher_edukation, status):
        Person.__init__(self, name, brith_date, occupation, higher_edukation,)
        self.status = status

    def introduce(self):
        return (f'Имя - {self.name}\n'
                f'День рождения - {self.brith_date}\n'
                f'Занятия - {self.occupation}\n'
                f'Высшее_образование - {self.higher_edukation}\n'
                f'Статус в классе {self.status}')

fr1 = Friend('Бектан', 2008, 'football', 'среднее', 7)
fr2 = Friend('Султан', 2009, 'бокс', 'среднее', 5)
print(fr1.introduce())
print(fr2.introduce())

cl1 = Classmate('Марьям', 2008, 'model', 'среднее', 'отличница')
cl2 = Classmate('Улукбек', 2008, 'math', 'среднее неполное','отличник' )
print(cl1.introduce())
print(cl2.introduce())
