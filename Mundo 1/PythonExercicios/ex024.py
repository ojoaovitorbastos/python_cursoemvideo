# Sua cidade começa com RIO?
cidade = str(input('Em qual cidade você nasceu? ').strip())

TrueOrFalse = (cidade[:3].upper() == 'RIO')

print('Sua cidade começa com RIO? {}'.format(TrueOrFalse))
