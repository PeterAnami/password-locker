import unittest
import pyperclip
from user import User, Credential

class TestUser(unittest.TestCase):
  '''
  Test class that defines test cases for the user class behaviors.
  Args:
      unittest.TestCase:helps in creating test cases
  '''
  def setUp(self):
    '''
    Function to create a user account before each test
    '''
    self.new _user = User('Peter','An\'am\'i','pswd100')

  def test__init__(self):
    '''
    Test to if check the creation of user instances is properly done
    '''
    self.assertEqual(self.new_user.first_name,'Peter')
    self.assertEqual(self.new_user.last_name,'An\'am\'i')
    self.assertEqual(self.new_user.password,'pswd100')
