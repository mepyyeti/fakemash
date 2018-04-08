#!usr/bin/env python3
#fakemash0.py

import sys
from functools import partial

def askme(question,type,errmsg):
	while True:
		user_input = input(question)
		if user_input != '':
			try:
				user_input == type(user_input)
			except ValueError:
				print(f'{user_input} is insufficient. Please read:')
				print(errmsg)
			else:
				print(f'enteries --{user_input}-- are acceptable.')
				return user_input
		else:
			continue

q_words= partial(askme,type=str,errmsg='must be in words...')
q_numbers= partial(askme,type=int, errmsg='must be in numbers...')

def mash():
	while True:
		
		print('''the categories:\n
		M\tA\tS\tH
		[1]\tPartner
		[2]\tNo. of kids
		[3]\tCar
		''')
		
		main_dict = {'title':'M','title':'A','title':'S','title':'H'}
		
		while True:
			q_partners=q_words('please enter 4 first names. Separate these names using spacebar.\t'  )
			q_rules=input('did you follow directions? \'y\' to continue...')
			if q_rules != 'n':
				break
		
		partners_list = q_partners.split(' ')
		
		for i in partners_list:
			main_dict['partners']=partners_list[i]
	
		while True:
			q_kids=q_numbers('please enter 4 possibilities of how many children you expect to have.\n\tIE -- 1 2 3 4')
			q_rules=input('did you follow directions? \'y\' to continue...')
			if q_rules != 'n':
				break
		
		kids_list = q_kids.split(' ')
		for i in kids_list:
			main_dict['kids']=kids_list[i]
		
		while True:
			q_car=q_words('please enter 4 possible vehicle options...')
			q_rules=input('did you follow directions? \'y\' to continue...')
			if q_rules != 'n':
				break
		
		car_list = q_car.split(' ')
		for i in car_list:
			main_dict['car']=car_list[i]
		
		secret_word = q_word('please enter the first word that comes to your mind...')
		circles=len(secret_word.strip())
		if circles >=15:
			circle = circles/15
		else:
			circle = circles
	
		final_dict = {}
	
		#unable to find better alternative to 'eliminate' used categories
		#this method obv screws up the count, among other shortcomings(?)
		while len(main_dict) != 0:
			if circle >len(main_dict):
				circle /= len(main_dict)
			while circle <= len(main_dict):
				chosen_value = main_dict[circle]
				if chosen_value in main_dict.values():
					for category, chosen_value in main_dict:
						final_dict[category]=chosen
						del main_dict[category]
	
		print('your results:')
		for k,v in final_dict:
			print(k,']',v)
		keep_going = q_words('play again? [y/n]')
		if keep_going.lower() == 'y' or keep_going.lower() == 'yes':
			continue
		else:
			print('\n\t\t**thanks for playing**')
			sys.sleep(2)

if __name__=='__main__':
	mash()

