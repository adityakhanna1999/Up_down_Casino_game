import numpy as np


def roll():
	x = np.random.choice([0, 1, 2], p=[5/12, 1/6, 5/12])
	return x
def select_A():
	return np.random.choice([0,2], p = [1/2,1/2])
def select_B():
	return np.random.choice([2], p = [1])

total_money = 5000
total_moves = 100

def play_A(total_money,total_moves, inital_bet):
	cur_moves = -1
	win = 0
	cur_bet = inital_bet
	while True:
		# print(total_money)
		x = select_A()
		y = roll()
		if x==y:
			win = 1
		else:
			win = 0
		cur_moves += 1
		if win==1:
			total_money += cur_bet
			if(cur_moves > total_moves):
				print(" A exit with ", total_money)
				return total_money
				break	

		else:
			total_money -= cur_bet
			if(total_money < 0):

				print(" A bankrupt in ", cur_moves)
				return 0

def play_B(total_money,total_moves, inital_bet):
	cur_moves = -1
	win = 0
	cur_bet = inital_bet
	while True:
		# print(total_money)
		x = select_A()
		y = roll()
		if x==y:
			win = 1
		else:
			win = 0
		cur_moves += 1
		# print(win)
		if win==1:
			total_money += cur_bet
			cur_bet  = inital_bet
			if(cur_moves > total_moves):
				print(" B exit with ", total_money)
				return total_money
				break	

		else:
			total_money -= cur_bet
			if(total_money < 0):
				print(" B bankrupt in ", cur_moves,"with amount" ,total_money+cur_bet)
				return total_money + cur_bet
				break
			cur_bet = cur_bet*2


play_A(10000,10,100)
play_B(10000,10,100)

