#! /usr/bin/env python3.8 2021
import pyperclip
from user_credentials import User, Credential

def create_user(fname,lname,password):
	'''
	allows us to create a new user
	'''
	new_user = User(fname,lname,password)
	return new_user

def save_user(user):
	'''
	allows us to save the user if they are new
	'''
	User.save_user(user)

def verify_user(first_name,password):
	'''
	this allows to to clarify users before they enter information
	'''
	checking_user = Credential.check_user(first_name,password)
	return checking_user

def generate_password():
	'''

	'''
	gen_pass = Credential.generate_password()
	return gen_pass

def create_credential(user_name,site_name,account_name,password):
	'''
	Function to create a new information
	'''
	new_credential=Credential(user_name,site_name,account_name,password)
	return new_credential

