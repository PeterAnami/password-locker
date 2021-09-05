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

