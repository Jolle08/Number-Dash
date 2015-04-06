"""
	Created on Sun Apr 5 21:10:00 2015
	
	@author Joel Eriksson

	===============================================================================

	The MIT License (MIT)

	Copyright (c) 2015 Joel Eriksson

	Permission is hereby granted, free of charge, to any person obtaining a copy
	of this software and associated documentation files (the "Software"), to deal
	in the Software without restriction, including without limitation the rights
	to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
	copies of the Software, and to permit persons to whom the Software is
	furnished to do so, subject to the following conditions:

	The above copyright notice and this permission notice shall be included in all
	copies or substantial portions of the Software.

	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
	IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
	FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
	AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
	LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
	OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
	SOFTWARE.
"""
import sys, os, subprocess, time
from random import randint

def clear():
	if os.name == "nt":
		os.system('cls')
	else:
		subprocess.call(['clear'])
	pass

def startscreen():
	clear()
	print "                                        .         .                                                         "
	print "b.             8 8 8888      88        ,8.       ,8.          8 888888888o   8 8888888888   8 888888888o.   "
	print "888o.          8 8 8888      88       ,888.     ,888.         8 8888    `88. 8 8888         8 8888    `88.  "
	print "Y88888o.       8 8 8888      88      .`8888.   .`8888.        8 8888     `88 8 8888         8 8888     `88  "
	print ".`Y888888o.    8 8 8888      88     ,8.`8888. ,8.`8888.       8 8888     ,88 8 8888         8 8888     ,88  "
	print "8o. `Y888888o. 8 8 8888      88    ,8'8.`8888,8^8.`8888.      8 8888.   ,88' 8 888888888888 8 8888.   ,88'  "
	print "8`Y8o. `Y88888o8 8 8888      88   ,8' `8.`8888' `8.`8888.     8 8888888888   8 8888         8 888888888P'   "
	print "8   `Y8o. `Y8888 8 8888      88  ,8'   `8.`88'   `8.`8888.    8 8888    `88. 8 8888         8 8888`8b       "
	print "8      `Y8o. `Y8 ` 8888     ,8P ,8'     `8.`'     `8.`8888.   8 8888      88 8 8888         8 8888 `8b.     "
	print "8         `Y8o.`   8888   ,d8P ,8'       `8        `8.`8888.  8 8888    ,88' 8 8888         8 8888   `8b.   "
	print "8            `Yo    `Y88888P' ,8'         `         `8.`8888. 8 888888888P   8 888888888888 8 8888     `88. "
	print ""                                                                    
	print "8 888888888o.            .8.            d888888o.   8 8888        8 "
	print "8 8888    `^888.        .888.         .`8888:' `88. 8 8888        8 "
	print "8 8888        `88.     :88888.        8.`8888.   Y8 8 8888        8 "
	print "8 8888         `88    . `88888.       `8.`8888.     8 8888        8 "
	print "8 8888          88   .8. `88888.       `8.`8888.    8 8888        8 "
	print "8 8888          88  .8`8. `88888.       `8.`8888.   8 8888        8 "
	print "8 8888         ,88 .8' `8. `88888.       `8.`8888.  8 8888888888888 "
	print "8 8888        ,88'.8'   `8. `88888.  8b   `8.`8888. 8 8888        8 "
	print "8 8888    ,o88P' .888888888. `88888. `8b.  ;8.`8888 8 8888        8 "
	print "8 888888888P'   .8'       `8. `88888. `Y8888P ,88P' 8 8888        8 "
	print ""
	print ""
	print ""
	print "    _                                   _             ____                                             "
	print "   / \      __ _  __ _ _ __ ___   ___  | |__  _   _  |  _ \ __ _ _ __ ___   ___  _ __ __ _ _ __   __ _ "
  	print "  / _ \    / _` |/ _` | '_ ` _ \ / _ \ | '_ \| | | | | |_) / _` | '_ ` _ \ / _ \| '__/ _` | '_ \ / _` |"
 	print " / ___ \  | (_| | (_| | | | | | |  __/ | |_) | |_| | |  __/ (_| | | | | | | (_) | | | (_| | | | | (_| |"
	print "/_/   \_\  \__, |\__,_|_| |_| |_|\___| |_.__/ \__, | |_|   \__,_|_| |_| |_|\___/|_|  \__,_|_| |_|\__,_|"
	print "           |___/                              |___/                                                    "
	print ""
	print "Coded by Joel Eriksson at Pamorana (joel@fam-ericsson.se)."
	print "Copyright (C) 2015 Joel Eriksson. Licensed under The MIT License (MIT)"
	print ""

	time.sleep(3)
	clear()
	start(0,0)

def start(rand,maxguess):
	maxrand = 1000
	if rand == 0:
		rand = randint(1, maxrand)
		maxguess = 12

	print "Guess a number between 1 and %s.\nYou have %s guesses to get it right." % (maxrand,maxguess)
	print "====================================================================="
	guess = raw_input("Your guess:> ")
	while not guess.isdigit():
		print "====================================================================="
		print "\"%s\" is not an integer." % (guess)
		print "====================================================================="
		guess = raw_input("Try again:> ")

	guess = int(guess)

	testinput(rand,guess,maxrand,maxguess)

def testinput(rand,guess,maxrand,maxguess):
	if guess > 0 and guess < maxrand + 1:
		gameif(rand,guess,maxrand,maxguess)
	else:
		clear()

		error = "Please guess a number which is between 1 and %s!" % (maxrand)
		print error.upper()

		time.sleep(3)
		clear()
		start(rand,maxguess)

def gameif(rand,guess,maxrand,maxguess):
	if guess == rand:
		maxguess = maxguess - 1
		clear()

		print "You won!"
		print "Guesses left: " + str(maxguess)
		print "====================================================================="

		time.sleep(3)
		clear()
		start(0,0)
	elif guess > rand:
		maxguess = maxguess - 1
		clear()

		print "Smaller than %s!" % (guess)
		print "Guesses left: " + str(maxguess)
		print "====================================================================="

		gamelose(rand,guess,maxrand,maxguess)

	elif guess < rand:
		maxguess = maxguess - 1
		clear()

		print "Bigger than %s!" % (guess)
		print "Guesses left: " + str(maxguess)
		print "====================================================================="

		gamelose(rand,guess,maxrand,maxguess)

def gamelose(rand,guess,maxrand,maxguess):
	if maxguess == 0:
		clear()

		print "Game over!"
		print "The random number was %s." % (rand)
		print "====================================================================="

		time.sleep(3)
		clear()
		start(0)
	else:
		guess = raw_input("Your guess:> ")
		while not guess.isdigit():
			print "====================================================================="
			print "\"%s\" is not an integer." % (guess)
			print "====================================================================="
			guess = raw_input("Try again:> ")

		guess = int(guess)
		testinput(rand,guess,maxrand,maxguess)

startscreen()