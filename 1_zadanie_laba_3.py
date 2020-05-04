import logpy
from logpy.core import lall

people = logpy.var()
rules = lall(
	(logpy.eq, (logpy.var(), logpy.var(), logpy.var(), logpy.var(), logpy.var()), people),
	(logpy.membero, ('Англичанин', logpy.var(), logpy.var(), logpy.var(), 'красный'), people),
	(logpy.membero, ('Швед', logpy.var(), logpy.var(), 'собака', logpy.var()), people),
	(logpy.membero, ('Датчанин', logpy.var(), 'чай', logpy.var(), logpy.var()), people),
	(logpy.membero, (logpy.var(), logpy.var(), 'кофе', logpy.var(), 'зеленый'), people),
	(logpy.membero, (logpy.var(), 'Pall Mall', logpy.var(), 'птицы', logpy.var()), people),
	(logpy.membero, (logpy.var(), 'Dunhill', logpy.var(), logpy.var(), 'желтый'), people),
	(logpy.membero, (logpy.var(), 'Rothmans', logpy.var(), logpy.var(), logpy.var()), people),
	(logpy.membero, (logpy.var(), logpy.var(), 'молоко', logpy.var(), logpy.var()), people),
	(logpy.membero, (logpy.var(), 'Philip Morris', 'пиво', logpy.var(), logpy.var()), people),
	(logpy.membero, (logpy.var(), logpy.var(), 'вода', logpy.var(), logpy.var()), people),
	(logpy.membero, (logpy.var(), logpy.var(), logpy.var(), 'лошади', 'синий'), people),
	(logpy.membero, (logpy.var(), logpy.var(), logpy.var(), 'кошки', logpy.var()), people),
	(logpy.membero, ('Немец', 'Marlboro', logpy.var(), logpy.var(), logpy.var()), people),
	(logpy.membero, (logpy.var(), logpy.var(), logpy.var(), 'рыбки', logpy.var()), people)
)
solution = logpy.run(0, people, rules)
for item in solution[0]:
	print(item)


