from datetime import datetime

class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.__birth_date = birth_date
        self.__occupation = occupation
        self.__higher_education = higher_education

    @property
    def occupation(self):
        return self.__occupation

    @property
    def higher_education(self):
        return self.__higher_education

    @property
    def age(self):
        birth = datetime.strptime(self.__birth_date, "%d.%m.%Y")
        today = datetime.today()
        return today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))

    def introduce(self):
        return (f'Имя - {self.name}\n'
                f'День рождения - {self.__birth_date}\n'
                f'Профессия - {self.__occupation}\n'
                f'Высшее образование - {self.__higher_education}')


class Friend(Person):
    def __init__(self, name, birth_date, occupation, higher_education, time_friend):
        super().__init__(name, birth_date, occupation, higher_education)
        self.time_friend = time_friend

    def introduce(self):
        return (f'Имя - {self.name}\n'
                f'Возраст - {self.age}\n'
                f'Профессия - {self.occupation}\n'
                f'Высшее образование - {self.higher_education}\n'
                f'Сколько лет дружим - {self.time_friend}')


class Classmate(Person):
    def __init__(self, name, birth_date, occupation, higher_education, status):
        super().__init__(name, birth_date, occupation, higher_education)
        self.status = status

    def introduce(self):
        return (f'Имя - {self.name}\n'
                f'Возраст - {self.age}\n'
                f'Профессия - {self.occupation}\n'
                f'Высшее образование - {self.higher_education}\n'
                f'Статус в классе - {self.status}')



fr1 = Friend('Бектан', '01.06.2008', 'футболист', 'среднее', 7)
fr2 = Friend('Султан', '12.09.2009', 'боксер', 'среднее', 5)

print(fr1.introduce())
print(fr2.introduce())

cl1 = Classmate('Марьям', '02.03.2008', 'модель', 'среднее', 'отличница')
cl2 = Classmate('Улукбек', '25.11.2008', 'математик', 'неполное среднее', 'отличник')

print(cl1.introduce())
print(cl2.introduce())
