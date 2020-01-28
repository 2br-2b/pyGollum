import Gollum.eliza
from Gollum.eliza import Eliza as Chatbot

cbot = Chatbot()
cbot.load('Gollum/doctor.txt')
print(cbot.init())

while True:
    sent = input('> ')

    output = cbot.message(sent)
    if output is None:
        break

    print(output)

print(self.final())