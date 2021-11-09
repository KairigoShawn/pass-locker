import pyperclip
import random
import string


global users_list
class User:
	'''
	allows usto create new users and save their information for future usage
	'''

	users_list = []
	def __init__(self,first_name,last_name,password):
		'''
		defining properties
		'''

		# In variables
		self.first_name = first_name
		self.last_name = last_name
		self.password = password

	def save_user(self):
		'''
		saves new user created
		'''
		User.users_list.append(self)

class Credential:
	'''
	account to save passwords info and new info
	'''
	# Class Variables
	credentials_list =[]
	user_credentials_list = []
	@classmethod
