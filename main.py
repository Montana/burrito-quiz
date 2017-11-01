import random
import time
from colorama import init
init(autoreset=True) 
from colorama import Fore, Back, Style
import question

def intro():
	print(Fore.RED + "Hello program, what burrito's did my brother purchase today?")
	print(Fore.RED + "This is a multiple-choice quiz designed to test you on your knowledge on my brother's purchasing habits of burritos.")
	print(Fore.CYAN + "This is the end of the introduction.")
	print(Fore.GREEN + "Good luck!")

intro() 
question.q1() 
question.q2() 
question.q3() 

# Written by Montana Mendy 
