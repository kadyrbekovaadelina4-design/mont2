class Person:
    def __init__(self,name,brith_date,occupation,higher_eduktation):
      self.name = name
      self.brith_date = brith_date
      self.occupaton = occupation
      self.higher_edukation = higher_eduktation
      person1 = Person("Алихан","2006-`12-09","Курсант","True")
      person2 = Person("Адэлина","2007-21-03","Экономист-аналитик",False)
      person3 = Person("Айгерим","2003-01-23","Призидент",False )

      print("Алихан,2006-12-09,Курсант,True:")
      print(f"Имя: {person1.name}")
      print(f"Дата рождения: {person1.birth_date}")
      print(f"Профессия: {person1.occupation}")
      print(f"Высшее образование: {person1.higher_education}")
      print("-" * 20)

      print("Айгерим,2006-01-23,Призидент,Fals:")
      print(f"Имя: {person2.name}")
      print(f"Дата рождения: {person2.birth_date}")
      print(f"Профессия: {person2.occupation}")
      print(f"Высшее образование: {person2.higher_education}")
      print("-" * 20)
