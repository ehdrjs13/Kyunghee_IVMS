from Ticket.makeTicket import makeTicket

ticket = makeTicket()

print('Wait for a Second...')

for i in range(ticket.qr.data.shape[1]):
    num_four = str(i+1).zfill(4)
    ticket.makeImage(num_four)

print('done')