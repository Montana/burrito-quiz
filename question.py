from colorama import *
init(autoreset=True)
import answer
import time
correct = 0
incorrect = 0
def printscore():
	global correct
	global incorrect
	total = correct + incorrect
	percent = (correct/total)*100.0
	print(str(percent) + "%")

def convert():
	global ans
	if ans in ("a", "a.", "A", "A."):
		ans = 0
		return ans
	elif ans in ("b", "b.", "B", "B."):
		ans = 1
		return ans
	elif ans in ("c", "c.", "C", "C."):
		ans = 2
		return ans
	elif ans in ("d", "d.", "D", "D."):
		ans = 3
		return ans
	else:
		print("Choose an actual answer.")
		ans = raw_input(">> ")
		ans = convert()
		return ans

def q1():
	global ans
	print "\n"
	print(Style.DIM + Fore.RED + "|-- Thinking of The Answer --|") 
	print(Fore.CYAN + "What is the definition of " + Style.BRIGHT + "question:") 
	dct = answer.q1() 
	anslst = dct.keys()
	a = anslst[0]
	b = anslst[1]
	c = anslst[2]
	d = anslst[3]
	print(Fore.YELLOW + "	a. " + a)
	print(Fore.YELLOW + "	b. " + b)
	print(Fore.YELLOW + "	c. " + c)
	print(Fore.YELLOW + "	d. " + d)
	print "\n"
	ans = raw_input(">> ")
	ans = convert() # Convert answer into an integer
	if dct[anslst[ans]] == True:
		global correct
		correct += 1
		print(Style.BRIGHT + Fore.GREEN + "Correct.")
		printscore()
		time.sleep(1) 
	else:
		global incorrect
		incorrect += 1
		print(Style.BRIGHT + Fore.RED + "Incorrect.")
		printscore()
		time.sleep(1) 
print "\n"

def q2(): 
	global ans
	print "\n"
	print(Style.DIM + Fore.RED + "|-- Thinking Queriouslly --|")
	print(Fore.CYAN + "This is the second question of questionable nature")
	dct = answer.q2()
	anslst = dct.keys()
	a = anslst[0]
	b = anslst[1]
	c = anslst[2]
	d = anslst[3]
	print(Fore.YELLOW + "	a. " + a)
	print(Fore.YELLOW + "	b. " + b)
	print(Fore.YELLOW + "	c. " + c)
	print(Fore.YELLOW + "	d. " + d)
	print "\n"
	ans = raw_input(">> ")
	ans = convert() 
	if dct[anslst[ans]] == True:
		global correct
		correct += 1
		print(Style.BRIGHT + Fore.GREEN + "Correct.")
		printscore()
		time.sleep(2)
	else:
		global incorrect
		incorrect += 1
		print(Style.BRIGHT + Fore.RED + "Incorrect.")
		printscore()
		time.sleep(2)
print "\n"

def q3():
	global ans
	print "\n"
	print(Style.DIM + Fore.RED + "|-- Thinking Ethically --|")
	print(Fore.CYAN + "This is the third question of questionable nature")
	dct = answer.q3()
	anslst = dct.keys()
	a = anslst[0]
	b = anslst[1]
	c = anslst[2]
	d = anslst[3]
	print(Fore.YELLOW + "	a. " + a)
	print(Fore.YELLOW + "	b. " + b)
	print(Fore.YELLOW + "	c. " + c)
	print(Fore.YELLOW + "	d. " + d)
	print "\n"
	ans = raw_input(">> ")
	ans = convert() 
	if dct[anslst[ans]] == True:
		global correct
		correct += 1
		print(Style.BRIGHT + Fore.GREEN + "Correct.")
		printscore()
		time.sleep(2)
	else:
		global incorrect
		incorrect += 1
		print(Style.BRIGHT + Fore.RED + "Incorrect.")
		printscore()
		time.sleep(2)


