from Ticket.makeTicket import MakeTicket

ticket = MakeTicket()

print('Wait for a Second...')

for i in range(ticket.qr.data.shape[1]):
    num_four = str(i+1).zfill(4)
    ticket.makeImage(num_four)

print('done.')