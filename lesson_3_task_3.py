from Adress import Adress
from Mailing import Mailing
to_address = Adress(index='000111', city='SomeCity', street='SomeStreet', house='22', flat='33')
from_address = Adress(index='222333', city='AnotherCity', street='AnotherStreet', house='44', flat='55')
track = "TRACK123456"
cost = 500.00
mailing = Mailing(to_address=to_address, from_address=from_address, cost=cost, track=track)

print(f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, {mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment} в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, {mailing.to_address.house} - {mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")
