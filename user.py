import pyperclip 
import random
import string

#Global Variables

global users_list
class User:
  '''
  Class to create user accounts and save their information 
  '''
  # Class variables
  #global users_list
  users_list = []
  def __init__(self, first_name, last_name,password):
    '''
    method to define the properties for each user objective will hold
    '''
    # instance variables
    self.first_name = first_name
    self.last_name = last_name
    self.password = password
    def save_user(self):
      '''
      Function to save a newly created instance
      '''
      User.users_list.append(self)
class Credential:
  '''
  classs to create account credentials, generate passwords and save their information
  '''
  # Class variables
  credentials_list =[]
  user_credentials_list =[]
  @classmethod
  def check_user (Class,first_name,password):
    '''
    Method that checks if the name and password entered matches the entries in users_list
    '''
    current_user =''
    for user in User.users_list:
      if (user.first_name ==first_name and user.password == password):
        current_user = user.first_name
        return current_user
  def __init__(self,user_name,site_name,account_name,password):
    '''
    





