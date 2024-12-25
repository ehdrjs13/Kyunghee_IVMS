from Datas.Ticket.makeTicket import *
from Datas.makeDatabase import *


ticket = MakeTicket()

print('Wait for a Second...')

for i in range(ticket.qr.data.shape[1]):
    num_four = str(i+1).zfill(4)
    ticket.makeImage(num_four)
    print(num_four)

print('done.')