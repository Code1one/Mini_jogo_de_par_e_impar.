from random import randint
print('_' * 35)
print('\033[1;34;40mBem-vindo(a) ou jogo de par ou impar\033[m')
print('_' * 35)
while True:
	player=int(input('Digite um número: '))
	bot= randint(0,10)
	tot=player + bot
	type= ' '
	while type not in 'PI':
		type=str(input(f'Par ou impar [P/I] ')).strip() .upper()[0]
	print( f'Você jogou {player} e o computador jogou {bot}  e o total foi {tot}')
	if type == "P":
		if player % 2 == 0:
			print('\033[32mVocê venceu!\033[m')
		else:
			print('\033[31mVocê perdeu!\033[m')
			break		
	elif type == "I":
		if bot % 2 == 1:
			print('\033[31mVocê perdeu!\033[m')
		else:
			print('\033[32mVocê venceu!\033[m')
			break
print('\033[4;31m;Game Over!\033[m Se deseja continuar coloque outra ficha.')
			
	 								