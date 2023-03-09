import time


print("whats your name: ")


nameStart=input()

while (len(nameStart) == 0):
	nameStart = input("\nPlease enter a name: ")


print("\nOkay welcome " + nameStart)

score = 0

my_name = ("Cynthia " + "Frye")

print("\nWelcome to this game let's see if you know me (it\'s okay if you don\'t you can just cheat and look at the code :)")



print("\nThere is a point system you\'ll know your score at the end of the game")

soCorrect = input("\nWhat\'s my name ")


if soCorrect == (my_name):
	print("\nThat's Correct, Your Smart, Your Loyal (+3 points)")
	score +=3

elif soCorrect != (my_name):
	print("\nIncorrect... I thought you knew me. :'( (-1 point)")
	score -=1


age = 25

myage=input("\nWhats my age ")

if myage == "26":
	print('\nYou spying on me (you get 3 points)')
	score += 3


elif "25" >= myage:
	print('\nI really look that young (you get a point just for being nice)')
	score +=1


elif "25" <= myage:
	print("\nI'm not that old yet... (>:( -1 point)")
	score -=1

#elif myage == str(myage):
	#print("No it needs to be a number")

print("\nOkay here a hard one")


favFood = "shrimp"

soupWrong = ''


def tryAgain():
	print("\nTry again (-1 point)")
	time.sleep(1)

def thanksPlaying():
	print("\nThanks for playing, your score is " + str(score) + ".")
	time.sleep(5)
	quit()

myFood = input("\nWhat\'s my fav food? ")


if myFood == (favFood):
	print('\ncorrect (5 points)')
	score +=5

	thanksPlaying()

elif myFood != (soupWrong):
	print("\nincorrect (Here\'s a hint it starts with a \'s\')")
	score -=1
	tryAgain()


	tryAgain1 = input("What\'s my fav food: ")

	if tryAgain1 == (favFood):
		print("\nCorrect (you get 4 point)")
		score +=4

		thanksPlaying()

	elif tryAgain1 != soupWrong:
		print("\nNo here\s another letter \'sh\'")
		score -=1
		tryAgain()

		try2 = input ("\nWhat's my fav food")


		if try2 == (favFood):
			print("\nCorrect (you get 3 points)")
			score += 3
			thanksPlaying()

		elif try2 != soupWrong:
			print("\nno lets try one more letter no way you can not guess it this time \'shr\' ")
			score -= 1
			tryAgain()

			try3 = input("\nWhat's my fav food")

			if try3 == (favFood):
				print("Correct, knew you could figure it out(you get 2 points)")
				score += 2
				thanksPlaying()

			elif try3 != soupWrong:
				print("\nNo here another letter it starts with \'shrim\' no way you can get it wrong this time")
				score -= 1
				tryAgain()

				lastChance = input ("Okay one more time, what\'s my fave food")

				if lastChance == (favFood):
					print("There you go knew you\'ll get it eventally (you get 1 point)")
					score +=1
					thanksPlaying()

				elif lastChance != soupWrong:
					print("\nNo it's shrimp...shrimp..")
					score -=1
					thanksPlaying()