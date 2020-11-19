import datetime

# Se eu sair da minha casa às 6:52 e correr 1 quilômetro a um certo passo (8min15s por quilômetro), então 3 quilômetros a um passo mais rápido (7min12s por quilômetro) e 1 quilômetro no mesmo passo usado em primeiro lugar, que horas chego em casa para o café da manhã?

hora_saida = 6 * 60 * 60 + 52 * 60

primeirokm = 8 * 60 + 15

segundokm = 7 * 60 +12

cafe_da_manha = hora_saida + primeirokm * 2 + segundokm * 3 

print('hour: ' + str(datetime.timedelta(seconds=cafe_da_manha)))

