ZODIAC_1996_2008=(" a rat. Rat are intelligent, charming, quick-witted, practical, ambitious, and good at economizing as well as social activities. The weaknesses are that the Rats are likely to be timid, stubborn, wordy, greedy, devious, too eager for power and love to gossip.")
ZODIAC_1997_2009=(" an ox.Ox are usually hard working, honest, creative, ambitious, cautious, patient and handle things steadily. On the negative side, Ox people might be stubborn, narrow-minded, indifferent, prejudiced, slow and not good at communication.")
ZODIAC_1998_2010=(" a tiger.Tigers are the symbol of brave. People born in the year of the Tiger are friendly, brave, competitive, charming and endowed with good luck and authority. With indomitable fortitude and great confidence, the tiger people can be competent leaders. On the other side, they are likely to be impetuous, irritable, overindulged and love to boast to others.")
ZODIAC_1999_2011=(" a rabbit. Rabbit are kind-hearted, friendly, intelligent, cautious, skillful, gentle, quick and live long. They dislike fighting and like to find solutions through compromise and negotiation. On the negative side, Rabbit people have the potential to be superficial, stubborn, melancholy and overly-discreet.")
ZODIAC_2000_2012=(" a dragon.Dragon are powerful, kind-hearted, successful, innovative, brave, healthy courageous and enterprising. However, they tend to be conceited, scrutinizing, tactless, quick-tempered and over-confident.")
ZODIAC_2001_2002=(" a snake.Snake are wise, discreet, agile, attractive and full of sympathy. On the other hand, there is a tendency for them to be lazy, greedy, arrogant and indulging in self-admiration.")
ZODIAC_2003=(" a sheep.Sheep (also Goat or Ram) represents solidarity, harmony and calmness. People born in the year of the Sheep are polite, mild mannered, shy, imaginative, determined and have good taste. On the negative side, they are sometimes pessimistic, unrealistic, short-sighted and slow in behavior.")
ZODIAC_2004=(" a monkey.Monkey are wise, intelligent, confident, charismatic, loyal, inventive and have leadership. The weaknesses of the Monkeys are being egotistical, arrogant, crafty, restless and snobbish.")
ZODIAC_2005=(" a rooster.Rooster are beautiful, kind-hearted, hard-working, courageous, independent, humorous and honest. They like to keep home neat and organized. On the other side, they might be arrogant, self-aggrandizing, persuasive to others and wild as well as admire things or persons blindly.")
ZODIAC_2006=(" a dog. Dogs are honest, friendly, faithful, loyal, smart, straightforward, venerable and have a strong sense of responsibility. On the negative side, they are likely to be self-righteous, cold, terribly stubborn, slippery, critical of others and not good at social activities.")
ZODIAC_2007=(" a pig.Pig are happy, easygoing, honest, trusting, educated, sincere and brave. The possible dark sides the Pig people are stubbornness, naive, over-reliant, self-indulgent, easy to anger and materialistic. They are sometimes regarded as being lazy.")



def intro ():
	print("Hi, I am Yobot.")


def language():
	lang = input("Hi! Tell me if you speak: 1- English or 2- Bengali or 3- Hindi\n")
	

	if lang=="1":
		print("Hello")
	else:
		if lang=="2":
			print("Nomoskar")
		else:
			if lang=="3":
				print("Namaste")
			else:
				print("Sorry, you entered an invalid value.")



def zodiac():
	x=input("Now enter your birth year from 1996 - 2012.\n")
	print (x)
	for i in range(1):
		print(end="Your zodiac is")
	if x == "1996" or x=="2008":
		print(ZODIAC_1996_2008)
	else:
		if x=="1997" or x== "2009":
				print(ZODIAC_1997_2009)
		else:
				if x=="1998" or x=="2010":
						print(ZODIAC_1998_2010)
				else:
						if x=="1999" or x=="2011":
								print(ZODIAC_1999_2011)
						else:
								if x=="2000" or x=="2012":
										print(ZODIAC_2000_2012)
								else:
										if x=="2001" or x=="2002":
												print(ZODIAC_2001_2002)
										else:
												if x=="2003":
														print(ZODIAC_2003)
												else:
														if x=="2004":
															print(ZODIAC_2004)
														else:
															if x=="2005":
																print(ZODIAC_2005)
															else:
																if x=="2006":
																	print(ZODIAC_2006)
																else:
																	if x=="2007":
																		print(ZODIAC_2007)
																	else:
																		print("NA. Sorry, your age is not in the program.")



def test():
	print("\nThis is going to give you a couple scrambled words and you have to unscramble them.You will be provided with definitions to help you.Write the unscrambled word below it.If you get it correct, the question will move on.If false, the questions will stop and you will be given the option to leavee. If you stay, it will give you questions from the starting to get you some help on the concepts.")
	A=input("\ntrpaed is the word. The meaning is to leave.\n")
	if A=="depart":
		B=input("\niftss is the word. The meaning is to not be very bendable.\n")
		if B=="stiff":
			C=input("\n tkocpeo is the word. The meaning is small bag sewn into clothing.\n")
			if C=="pocket":
				D=input("\netedtna is the word. The meaning is part of an animal.\n")
				if D=="tentacle":
					E=input("\nraeudnenht is the word. The meaning is below\n")
					if E=="underneath":
						F=input("\nllavuaeb is the word.Important is the meaning.\n")
						if F=="valuable":
							G=input("\ndawrober is the word. Storagge for clothing is the meaning.\n")
							if G=="wardrobe":
								H=input("\nmug. The meaning is flesh aroud teeth.\n")
								if H=="gum":
									I=input("\ngelinf is the word. The meaning is emotion.\n")
									if I=="feeling":
										J=input("\nrlilap is the word. The meaning is tall upright structure.\n")
										if J=="pillar":
											K=input("\ngsint is the word. The meaning is minor injury.\n")
											if K=="sting":
												L=input("\ndledir is the word. The meaning is puzzling question\n")
												if L == "riddle":
													M==input("\ncylatxe is the word. The meaning is precisely.\n")
													if M == "exactly":
														N=input("\nlewej is the word.The meaning is precious stone.\n")
														if N=="jewel":
															O=input("\ndnsyyat is the word. The meaning is rulers that belong to the same family.\n")
															if O=="dynasty":
																P=input("\nchnarom is the word. The meaning is ruler.\n")
																if P== "monarch":
																	Q=input("\nbleramsc is the word. The meaning is move awkwardly.\n")
																	if Q=="scramble":
																		R=input("\nerpmohpos is the word. The meaning is 2nd yearer.\n ")
																		if R=="sophomore":
																			print("Well done! you are finished.")




							

x=2
x<1
while True:
	x=x+1
	intro()
	language()			
	zodiac()
	test()
	ABC=input("Would you like to continue? If yes, press B. If you want to only do the test, press G.")
	if ABC=="B"	:
		continue
	if ABC=="G":
		x=2
		x<1
		while True:
			x=x+1
			test()
			CDE=input("If you want to continue, press A.")
		if CDE=="A":
			continue
		else:
			break
	else:
		break