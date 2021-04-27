"""
Tantalizing Trivia (Python3)

Tantalizing Trivia is a quiz application made using python3 and tkinter GUI framework. It makes the use of sqlite3 database to store the to-be saved information. The application serves the sole purpose of creating quizes and testing them. Each quiz created is saved as a table in the database.

Dependencies : tkinter (python3 module)

Author : Rishav Das (Github : https://github.com/rdofficial)

Created on : November 2, 2020
"""

# Importing the required functions and modules
from sqlite3 import *
import os, sys
try:
	# Importing the tkinter graphical module using the under the try..except.. block for the error free importing of the script
	from tkinter import *
	from tkinter import messagebox as mb
except Exception as e:
	if 'linux' in sys.platform:
		print('Install tkinter module using the command : sudo apt install python-tk')

class MenuOptions:
	""" The class for containing all the menu commands """

	def __init__(self):
		self.__version = 1.1
		self.__lastUpdated = '20/07/2020'

	def aboutAuthor():
		""" The menu command for showing the tkinter window with the about author information """

		win = Tk()
		win.title('TantalizingTrivia - About Author')
		win.resizable(0, 0)
			
		# Configuring the heading for the tkinter window
		Label(
			win,
			text = 'About Author',
			font = ('', 13, 'bold', 'italic'),
			padx = 5,
			pady = 5,
		).pack(padx = 5, pady = 10)
		
		# Configuring the content of the tkinter window
		content = """
The author of this project is Rishav Das, A student of class 12, Dayawati Modi Public School.
I have created this project under the guidance of our computer teacher Kavita Singh. I belong
to the Science group with subjects Physics, Chemistry, Mathematics and Computer Science. 
I am a programmer, scripter and a pentester. The programming languages and frameworks I know are : C, C++, Python,
JavaScript, PHP, Django, bash, NodeJS, LAMP stack, LEMP stack, MERN and MEAN stacks, Java and Kotlin.		
"""
		Label(
			win,
			text = content,
			font = ('', 11, ''),
		).pack(padx = 5, pady = 5)

		mainloop()

	def aboutProject():
		""" The menu command function for displaying the tkinter window with the about project information """

		win = Tk()
		win.title('TantalizingTrivia - About Project')
		win.resizable(0, 0)
			
		# Configuring the heading for the tkinter window
		Label(
			win,
			text = 'About Project',
			font = ('', 13, 'bold', 'italic'),
			padx = 5,
			pady = 5,
		).pack(padx = 5, pady = 10)
		
		# Configuring the content of the tkinter window
		content = """
The script named 'TantalizingTrivia' is written in Python3 and is a part of the computer project for class 12
boards.	The project as per its name is a quiz app which contains the features of answering the questions as well
as writing questions (i.e., creating new quiz questions). The questions are generally stored in a database file
named quizDB.db and maintained under the SQlite3 database management sever. The database file must remain in the
same folder as per the python3 script. The project includes other features like :- Pointing out results for each
correct answers and showing remarks at the end of the quiz, The quizes are generally saved in separate tables in
the database. The script uses a graphical interface with the help of the tkinter graphical interface framework.	
"""
		Label(
			win,
			text = content,
			font = ('', 11, ''),
		).pack(padx = 5, pady = 5)

		mainloop()

	def help():
		""" The menu command function for displaying the tkinter window with the helping information about the script """

		win = Tk()
		win.title('TantalizingTrivia - Help')
		win.resizable(0, 0)
			
		# Configuring the heading for the tkinter window
		Label(
			win,
			text = 'Help',
			font = ('', 13, 'bold', 'italic'),
			padx = 5,
			pady = 5,
		).pack(padx = 5, pady = 10)
		
		# Configuring the content of the tkinter window
		content = """
The project is quite simple to use and implement. The basics of the project is to create quizes and answering of
the questions with the grading systems. The main menu of the script contains the options to create a quiz, 
start / load a quiz, delete a quiz. As per the name, each of the option does the same work. When we click on the
create a quiz option, the question entering forms pop up. The fields information asked are the question names along
with the option name and the correct option (NOTE - The correct option should be given as the option number in the
numeric form). 	
"""
		Label(
			win,
			text = content,
			font = ('', 11, ''),
		).pack(padx = 5, pady = 5)

		mainloop()

def restart():
	""" The function for restarting the main tkinter window of the app """

	try:
		win.destroy()
	except:
		pass
	main()
	
def appendQuizData(questionsList, answersList, optionsList, question, answer, options):
	""" The function which append per created questions to the global list and saves for later dumping into the database table """

	if len(question) == 0 or len(answer) == 0 or len(options[0]) == 0 or len(options[1]) == 0 or len(options[2]) == 0 or len(options[3]) == 0:
		mb.showerror('Error!', 'Do not leave any field blank')
	else:
		try:
			questionsList.append(question);answersList.append(int(answer)-1);optionsList.append(options)
			mb.showinfo('Question added!', 'A question added')
			questionVAR.set('');option1VAR.set('');option2VAR.set('');option3VAR.set('');option4VAR.set('');answerVAR.set('')
		except ValueError:
			mb.showerror('Error!', 'The correct answer should be the numeric option number.')

def dumpQuizData(questionsList, answersList, optionsList, tableName, frame1, tableNameWin):
	""" The function for dumping the created quiz data into the user defined named DataBase table """

	frame1.destroy()
	cursor = sqlCon.cursor()
	if len(tableName) == 0:
		# If the user has entered the quiz table name as empty
		mb.showerror('Error!', 'The table name cannot be empty')
	else:
		try:
			sqlCon.execute("CREATE TABLE {tableName} (question TEXT, option1 TEXT, option2 TEXT, option3 TEXT, option4 TEXT, answer TEXT);".format(tableName = tableName))
			for question in questionsList:
				answer = answersList[questionsList.index(question)]
				options = optionsList[questionsList.index(question)]
				if '"' not in question and "'" in question:
					# If the question statement has no double quotes but has single quotes
					cursor.execute('INSERT INTO `{tableName}` VALUES ("{question}", "{option1}", "{option2}", "{option3}", "{option4}", "{answer}");'.format(tableName = tableName, question = question, option1 = options[0], option2 = options[1], option3 = options[2], option4 = options[3], answer = answer))
				elif "'" not in question and '"' in question:
					# If the question statement has single quotes but no double quotes
					cursor.execute("INSERT INTO `{tableName}` VALUES ('{question}', '{option1}', '{option2}', '{option3}', '{option4}', '{answer}');".format(tableName = tableName, question = question, option1 = options[0], option2 = options[1], option3 = options[2], option4 = options[3], answer = answer))
				else:
					# If any other conditions
					cursor.execute("INSERT INTO `{tableName}` VALUES ('{question}', '{option1}', '{option2}', '{option3}', '{option4}', '{answer}');".format(tableName = tableName, question = question, option1 = options[0], option2 = options[1], option3 = options[2], option4 = options[3], answer = answer))
				sqlCon.commit()
			Button(win, text = 'GO BACK TO MAIN MENU', padx = 5, pady = 5, foreground = 'red', background = 'yellow', activebackground = 'red', activeforeground = 'yellow', font = ('', 13, 'bold'), relief = GROOVE, command = restart).pack(padx = 5, pady = 5)
			tableNameWin.destroy()

		except OperationalError:
			# If there is a table with same name exists
			if 'table' in e:
				mb.showerror('Error!', 'Quiz Table with same name exists')
			return 0

def dumpQuizData1(questionsList, answersList, optionsList, frame1):
	""" The function where we ask the user for entering the table name in the defined tkinter window """

	if len(questionsList) < 5:
		# If the user enters less than 5 questions for the database file
		mb.showerror('Error!', 'Please submit atleast 5 questions')
	else:
		# If the user has entered a good amount of the questions, then we define the window where we prompt the user to enteer the table name for newly created quiz 
		tableNameWin = Tk()
		tableNameWin.title('TantalizingTrivia - Question creator')
		tableNameWin.resizable(0, 0)

		# Defining the other widgets in the tkinter window
		frame = Frame(tableNameWin);frame.pack(expand = True, fill = BOTH, padx = 5, pady = 5)
		tableName = StringVar(tableNameWin)
		Label(frame, text = 'Enter the table (Quiz) name ', font = ('', 12, ''), foreground = 'black').pack(side = LEFT, padx = 5)
		Entry(frame, textvariable = tableName, font = ('', 12, '')).pack(side = RIGHT, padx = 5)
		Button(tableNameWin, text = 'CONTINUE', padx = 5, pady = 5, font = ('', 12, 'bold'), foreground = 'white', background = 'black', activeforeground = 'white', activebackground = 'green', relief = GROOVE, command = lambda : dumpQuizData(questionsList, answersList, optionsList, tableName.get(), frame1, tableNameWin)).pack(pady = 5, padx = 5)

def createQuiz():
	""" Creating a quiz table """

	# Preparing the form for entering the answers and questions
	global questionVAR, option1VAR, option2VAR, option3VAR, option4VAR, answerVAR
	questions = []
	answers = []
	options = []

	# Configuring the main tkinter window for the user to enter the questions, options and correct answers details for the newly created quiz and creating the required widgets
	win.config(background = 'white')
	frame1 = Frame(win, pady = 5, padx = 5);frame1.pack(pady = 5, padx = 5)
	questionFrame = Frame(frame1);questionFrame.pack(expand = True, fill = BOTH, pady = 5)
	quesLBL = Label(questionFrame, text = 'QUESTION -', foreground = 'black', font = ('', 11, ''));quesLBL.pack(pady = 5, padx = 5, side = LEFT)
	questionVAR = StringVar(win)
	Entry(questionFrame, textvariable = questionVAR, font = ('', 11, '')).pack(side = RIGHT, padx = 5)
	option1VAR = StringVar(win);option2VAR = StringVar(win);option3VAR = StringVar(win);option4VAR = StringVar(win)
	option1FRAME = Frame(frame1);option1FRAME.pack(expand = True, fill = BOTH, pady = (5,  1))
	option2FRAME = Frame(frame1);option2FRAME.pack(expand = True, fill = BOTH)
	option3FRAME = Frame(frame1);option3FRAME.pack(expand = True, fill = BOTH)
	option4FRAME = Frame(frame1);option4FRAME.pack(expand = True, fill = BOTH)
	Label(option1FRAME, text = 'OPTION-1-', font = ('', 11, ''), foreground = 'black').pack(side = LEFT, padx = 5)
	Entry(option1FRAME, textvariable = option1VAR, font = ('', 11, '')).pack(side = RIGHT, padx = 5)
	Label(option2FRAME, text = 'OPTION-2-', font = ('', 11, ''), foreground = 'black').pack(side = LEFT, padx = 5)
	Entry(option2FRAME, textvariable = option2VAR, font = ('', 11, '')).pack(side = RIGHT, padx = 5)
	Label(option3FRAME, text = 'OPTION-3-', font = ('', 11, ''), foreground = 'black').pack(side = LEFT, padx = 5)
	Entry(option3FRAME, textvariable = option3VAR, font = ('', 11, '')).pack(side = RIGHT, padx = 5)
	Label(option4FRAME, text = 'OPTION-4-', font = ('', 11, ''), foreground = 'black').pack(side = LEFT, padx = 5)
	Entry(option4FRAME, textvariable = option4VAR, font = ('', 11, '')).pack(side = RIGHT, padx = 5)
	answerFRAME = Frame(frame1,);answerFRAME.pack(fill = BOTH, expand = True, pady = 5)
	answerVAR = StringVar(win)
	Label(answerFRAME, text = 'Correct option - ', font = ('', 11, ''), foreground = 'black').pack(side = LEFT, padx = 5);Entry(answerFRAME, textvariable = answerVAR, font = ('', 11, '')).pack(side = RIGHT, padx = 5)

	# Defining the flow handling buttons
	btnFRAME = Frame(frame1,);btnFRAME.pack(expand = True, fill = BOTH, padx = 5, pady = 5)
	Button(btnFRAME, text = 'EXIT', foreground = 'red', background = 'black', activeforeground = 'black', activebackground = 'red', font = ('', 11, ''), command = win.destroy).pack(side = LEFT, padx = 5)
	Button(btnFRAME, text = 'SAVE', foreground = 'green', background = 'black', activeforeground = 'black', activebackground = 'green', font = ('', 11, ''), command = lambda : dumpQuizData1(questions, answers, options, frame1)).pack(side = LEFT, padx = 5)
	Button(btnFRAME, text = 'APPEND', foreground = 'yellow', background = 'black', activeforeground = 'black', activebackground = 'yellow', font = ('', 11, ''), command = lambda : appendQuizData(questions, answers, options, questionVAR.get(), answerVAR.get(), [option1VAR.get(), option2VAR.get(), option3VAR.get(), option4VAR.get()])).pack(side = LEFT, padx = 5)

def calculateResult(userAnswers, correctAnswers):
	result = 0
	for index, answer in enumerate(correctAnswers):
		if int(answer) == int(userAnswers[index]):
			result += 1
		else:
			pass
	if (result/len(questions)) < 0.6:
		resultTEXT = 'Not good performance!'
	elif (result/len(questions)) < 0.8:
		resultTEXT = 'Good performance!'
	elif (result/len(questions)) > 0.8:
		resultTEXT = 'Excellent performance!'
	elif (result/len(questions)) < 0.33:
		resultTEXT = 'Extremely poor performance!'

	mb.showinfo('RESULT', '%s You have answered %d questions correct out of %d questions.' %(resultTEXT, int(result), len(questions)))
	quizWIN.destroy()
	restart()

# The user given answers are stored here (in this array / list)
userAnswers = []
questionNumber = 0

def selected(quesLBL, option1radio, option2radio, option3radio, option4radio, radiovar):
	global questionNumber
	userAnswers.append(radiovar)
	questionNumber += 1
	if questionNumber < len(questions):
		quesLBL.config(text = questions[questionNumber])
		option1radio.config(text = options[questionNumber][0])
		option2radio.config(text = options[questionNumber][1])
		option3radio.config(text = options[questionNumber][2])
		option4radio.config(text = options[questionNumber][3])
	else:
		calculateResult(userAnswers, answers)

def loadQuiz1(tableName):
	global questions, answers, options, questionNumber, quizWIN, userAnswers
	questions = [];answers = [];options = [];questionNumber = 0;userAnswers = []

	try:
		cursor = sqlCon.cursor()
		cursor.execute('SELECT * FROM {}'.format(tableName))
		res = cursor.fetchall()
		for i in res:
			questions.append(i[0])
			options.append([i[1], i[2], i[3], i[4]])
			answers.append(i[5])
		n = 1
	except OperationalError:
		mb.showerror('Error!', 'There is some error in loading the quiz.\nPlease check the quiz table name correctly.')
		n = 0

	if n == 1:
		win.destroy()
		quizWIN = Tk()
		quizWIN.title('QUIZ \t-\t %s' %(tableName));quizWIN.geometry('500x400')
		quesLBL = Label(quizWIN, text = questions[questionNumber], foreground = 'black', font = ('', 12, 'bold'))
		quesLBL.pack(padx = 5, pady = 5)
		radiovar = IntVar(quizWIN)
		option1radio = Radiobutton(quizWIN, text = options[questionNumber][0], value = 0, variable = radiovar, foreground = 'black', font = ('', 12, ''), command = lambda : selected(quesLBL, option1radio, option2radio, option3radio, option4radio, radiovar.get()));option1radio.pack(padx = 5, pady = 2.5)
		option2radio = Radiobutton(quizWIN, text = options[questionNumber][1], value = 1, variable = radiovar, foreground = 'black', font = ('', 12, ''), command = lambda : selected(quesLBL, option1radio, option2radio, option3radio, option4radio, radiovar.get()));option2radio.pack(padx = 5, pady = 2.5)
		option3radio = Radiobutton(quizWIN, text = options[questionNumber][2], value = 2, variable = radiovar, foreground = 'black', font = ('', 12, ''), command = lambda : selected(quesLBL, option1radio, option2radio, option3radio, option4radio, radiovar.get()));option3radio.pack(padx = 5, pady = 2.5)
		option4radio = Radiobutton(quizWIN, text = options[questionNumber][3], value = 3, variable = radiovar, foreground = 'black', font = ('', 12, ''), command = lambda : selected(quesLBL, option1radio, option2radio, option3radio, option4radio, radiovar.get()));option4radio.pack(padx = 5, pady = 2.5)
		mainloop()
	else:
		pass

def loadQuiz():
	""" Playing the quiz """

	win.config(background = 'white')
	frame1 = Frame(win, background = 'white');frame1.pack(pady = 5, padx = 5, expand = True, fill = BOTH)
	tableName = StringVar(win)
	Label(frame1, text = 'Enter the quiz table name ', foreground = 'black', font = ('', 12, ''), background = 'white').pack(side = LEFT, padx = 5)
	Entry(frame1, textvariable = tableName, font = ('', 12, '')).pack(side = RIGHT, padx = 5)
	frame2 = Frame(win, background = 'white');frame2.pack(pady = 5, padx = 5,)
	Button(frame2, text = 'BACK', foreground = 'red', background = 'black', activeforeground = 'black', activebackground = 'red', relief = GROOVE, padx = 5, pady = 5, font = ('', 12, 'bold'), command = restart).pack(side = LEFT, padx = 5)
	Button(frame2, text = 'LOAD', foreground = 'green', background = 'black', activeforeground = 'black', activebackground = 'green', relief = GROOVE, padx = 5, pady = 5, font = ('', 12, 'bold'), command = lambda : loadQuiz1(tableName.get())).pack(side = RIGHT, padx = 5)

def deleteQuiz1(tableName, window):
	""" The function to execute the SQL commands for deletion of the user specified quiz table """

	try:
		sqlCon.execute('DROP TABLE {};'.format(tableName))
		mb.showinfo('Success!', 'Requested quiz table deleted successfully.')
		window.destroy()
	except OperationalError:
		mb.showerror('Error!', 'There is an error in the deletion of the requested quiz table.')
		window.destroy();restart()
		
def deleteQuiz():
	""" The function to perform the deletion of a particular quiz. The function generally deletes the database table specified (the quiz table). This particular function opens up a new tkinter window with input options for entering the quiz table name. """

	delquizWIN = Tk()
	delquizWIN.title('Delete quiz')
	delquizWIN.resizable(0, 0)
	frame1 = Frame(delquizWIN,);frame1.pack(padx = 5, pady = 5, expand = True, fill = BOTH)
	frame2 = Frame(delquizWIN,);frame2.pack(padx = 5, pady = 5)
	Label(frame1, text = 'Name of the quiz table ', foreground = 'black', font = ('', 12, '')).pack(side = LEFT, padx = 5)
	tableName = StringVar(delquizWIN)
	Entry(frame1, textvariable = tableName, font = ('', 12, '')).pack(side = RIGHT, padx = 5)
	Button(frame2, text = 'BACK', font = ('', 12, 'bold'), foreground = 'red', background = 'black', activebackground = 'red', activeforeground = 'black', relief = GROOVE, padx = 5, pady = 5, command = delquizWIN.destroy).pack(side = LEFT, padx = 5)
	Button(frame2, text = 'DELETE', font = ('', 12, 'bold'), foreground = 'yellow', background = 'black', activebackground = 'yellow', activeforeground = 'black', relief = GROOVE, padx = 5, pady = 5, command = lambda : deleteQuiz1(tableName.get(), delquizWIN)).pack(side = LEFT, padx = 5)
	mainloop()

def mainMenuChoosed(n, frame1):
	try:
		frame1.destroy()
	except:
		pass
	if n == 1:
		loadQuiz()
	elif n == 2:
		createQuiz()
	elif n == 3:
		deleteQuiz()
	elif n == 4:
		win.destroy();quit()

def main():
	global win, sqlCon
	quizDB = 'database.sqlite3'
	try:
		sqlCon = connect(quizDB)
	except:
		return 0
	win = Tk()
	win.title('TantalizingTrivia\t-\t1.0')
	win.resizable(0, 0)
	win.config(background = 'black')

	# Configuring the menu for the app
	menubar = Menu(win)
	win.config(menu = menubar)

	# Adding the submenus to the menubar
	fileMenu = Menu(menubar, tearoff = 0, font = ('', 10, ''))
	aboutMenu = Menu(menubar, tearoff = 0, font = ('', 10, ''))
	# Adding commands to the file menu
	fileMenu.add_command(label = 'Restart', command = restart)
	fileMenu.add_separator()
	fileMenu.add_command(label = 'Exit', command = exit)
	# Adding the commands to the aboutMenu
	aboutMenu.add_command(label = 'About author', command = MenuOptions.aboutAuthor)
	aboutMenu.add_command(label = 'About project', command = MenuOptions.aboutProject)
	aboutMenu.add_separator()
	aboutMenu.add_command(label = 'Help', command = MenuOptions.help)

	# Addding the sub menus to the menubar
	menubar.add_cascade(label = 'File', menu = fileMenu)
	menubar.add_cascade(label = 'About', menu = aboutMenu)

	userChoice = IntVar()  # Variable for storing the user chosen option's value
	frame1 = Frame(win, background = 'black')
	frame1.pack(pady = 5, padx = 5)
	Label(frame1, text = 'Tantalizing-Trivia', font = ('', 15, 'bold', 'italic'), foreground = 'green', background = 'black', pady = 5, padx = 5,).pack(pady = 5, padx = 5)
	Radiobutton(frame1, text = 'Load a quiz        ', foreground = 'white', border = None, background = 'black', font = ('', 12), pady = 5, padx = 5, variable = userChoice, value = 1, command = lambda : mainMenuChoosed(userChoice.get(), frame1)).pack(padx = 5, pady = 5, anchor = W)		
	Radiobutton(frame1,	text = 'Create a quiz table', foreground = 'white', background = 'black', font = ('', 12), pady = 5, padx = 5, variable = userChoice, value = 2, command = lambda : mainMenuChoosed(userChoice.get(), frame1)).pack(padx = 5, pady = 5, anchor = W)
	Radiobutton(frame1,	text = 'Delete a quiz table', foreground = 'white', background = 'black', font = ('', 12), variable = userChoice, value = 3, command = lambda : mainMenuChoosed(userChoice.get(), frame1), padx = 5, pady = 5).pack(padx = 5, pady = 5, anchor = W)
	Radiobutton(frame1,	text = 'Exit               ', foreground = 'white', background = 'black', font = ('', 12), variable = userChoice, value = 4, command = lambda : mainMenuChoosed(userChoice.get(), frame1), padx = 5, pady = 5).pack(padx = 5, pady = 5, anchor = W)
	mainloop()
	sqlCon.close()

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		# Quiting the script when the user presses CTRL+C key
    
		quit()
  except Exception as e:
    # If there are any errors encountered during the process, then we display the error on the console screen
    
    print('[ Error : {} ]'.format(e))
    input('Press enter key to continue...')
