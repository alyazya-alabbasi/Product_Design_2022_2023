
#_________add color_______#
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


#_______________________________________________level 1
level1="tca"
level1Answers="act"
level1Answers2="cat"

play=True



while play==True:



	print(color.PURPLE,"\n"*50,level1,"\n")
	playerguess=input("make a word out of these letters= ")






	if playerguess==level1Answers or playerguess==level1Answers2:
		print("You Won!\n\n")
		play=False
		# while play==False





	else:
		playerguess=input("try again= ")
		if playerguess==level1Answers or playerguess==level1Answers2:
			print("You Won!\n\n")
			play=False



#_______________________________________________level 2

level1="alsef"
level1Answers="false"

play=True

while play==True:



	print(color.CYAN, "\n"*50,level1,"\n")
	playerguess=input("make a word out of these letters= ")






	if playerguess==level1Answers: 
		print("You Won!\n\n")
		play=False
		# while play==False





	else:
		playerguess=input("try again= ")
		if playerguess==level1Answers or playerguess==level1Answers2:
			print("You Won!\n\n")
			play=False

