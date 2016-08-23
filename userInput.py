# Python program that will generate a .tex file
# It asks for input


# Asks for Inputs
def firstFunction():
	# first inputs
	antwortName = raw_input("Your Name: ")
	antwortJahr = raw_input("Year: ")
	antwortFD = raw_input("First Date: ")
	antwortSD = raw_input("Second Date: ")

	laTEX = """
	\\begin{center}
		\\begin{tabular}{ | m{15em} | m{21em} | }
		\hline
		Name des/der Auszubildenden: & %s \\\\ \hline
		Ausbildungsjahr: & %s Jahr \\\\ \hline
		Ausbildungswoche vom & %s bis %s \\\\ \hline
		\end{tabular}
	\end{center}""" % (antwortName, antwortJahr, antwortFD, antwortSD)

	# check if correct
	print "------------------------\nCheck if correct:"
	print "Name: " + antwortName
	print "Year: " + antwortJahr
	print "First Date: " + antwortFD
	print "Second Date: " + antwortSD
	antwortCor = raw_input("Everything correct? (Y/N): ")
	print "------------------------"

	# get answer if correct or not
	if antwortCor.lower() == "y":
		print "Nice!"
		print "Your File has been created."
		print "------------------------"
		# creates new file in read/write mode
		file = open('inputs/firstT.tex', 'w+')
		# what the file will contain
		file.write(laTEX)
		file.close()
	else:
		print "try again!"
		print "------------------------"
		#do function
		firstFunction()

# fancy "Welcome Message"
print "------------------------\nWelcome!\nThis is Berichtsheft 1.0\n------------------------"
firstFunction()