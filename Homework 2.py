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
        Person.__init__(name, brith_date, occupation, higher_edukation)
        self.time_friend = time_fried


class Classmate(Person):
    def __init__(self, name, brith_date, occupation, higher_edukation, status):
        Person.__init__(name, brith_date, occupation, higher_edukation)
        self.status = status
