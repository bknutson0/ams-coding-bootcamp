import   json        # uneven spacing
import os,sys; import re      # multiple imports on one line + stray semicolon
from   datetime  import datetime ,  timedelta as  td     # extra spacing
import    math, random   # unsorted, extra spaces
from   collections import  deque,    Counter  # spacing

X  =  42     # extra spaces around equals
Y=3.14       # missing spaces

def add(a,b):  # inconsistent spacing
	"""Add two numbers.

	Args:
		a (int | float): first number
		b (int | float): second number

	Returns:
		int | float: sum
	"""
	result=a  +b   # extra spaces
	return  (result)   # unnecessary parentheses and spaces

def greet(name  = "world" ,exclaim=True  ,  times =1):	# spaces around '=', missing after commas
	'''
	Say hello (NumPy style).

	Parameters
	----------
	name : str
		Name to greet.
	exclaim : bool, optional
		Whether to add exclamation marks.
	times : int, optional
		How many times to repeat.
	'''
	msg = "Hello, " + name + ("!" if exclaim==True else ".")	# compare to True
	long_line = "This is a ridiculously long line to demonstrate how a formatter wraps lines properly and handles spacing, commas, and other punctuation; it should definitely exceed one hundred and twenty characters in length so tools have something to do."  # very long line >120 chars
	for  i in   range(times):   print(msg)  # multiple statements on one line, extra spaces
	return msg



def is_even(n:int)->bool: # type hints stuck to arrows
	# reST style docstring
	"""Return True if *n* is even.

	:param n: Number to test.
	:returns: bool indicating evenness.
	"""
	if n%2==0 :	
		return True 
	else:
		return False;  # stray semicolon