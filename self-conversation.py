import Gollum.eliza
from Gollum.eliza import Eliza as Chatbot
import time

cbot1 = Chatbot()
cbot1.load('Gollum/doctor.txt')
last_message = cbot1.init()
print('1: ' + last_message)

time.sleep(3)

cbot2 = Chatbot()
cbot2.load('Gollum/doctor.txt')

last_message = cbot2.message(last_message)
print('2: ' + last_message)

time.sleep(3)

while True:
    last_message = cbot1.message(last_message)
    print('1: ' + last_message)

    time.sleep(3)

    last_message = cbot2.message(last_message)
    print('2: ' + last_message)
    
    time.sleep(3)
