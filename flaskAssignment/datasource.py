import psycopg2
import getpass
import math

'''
AMY
Some of these implementations are works in progress, so please grade
getNumberOfProjects
getRandomProject
getMinimumValueOfVariable
'''

class DataSource:
	'''
	DataSource executes all of the queries on the database.
	It also formats the data to send back to the frontend, typically in a list
	or some other collection or object.
	'''

	def __init__(self):
		self.user = 'santosb'
		self.password = 'book347winter'

	def connect(self):
		'''
		Establishes a connection to the database with the following credentials:

		PARAMETERS:
		user - username, which is also the name of the database
		password - the password for this database on perlman

		RETURNS: a database connection.

		Note: exits if a connection cannot be established.
		Note: Code written by Amy Csizmar Dalal
		'''
		try:
			connection = psycopg2.connect(database=self.user, user=self.user, password= self.password)
		except Exception as e:
			print("Connection error: ", e)
			exit()
		return connection

	def getNumberOfProjects(self, connection):
		'''
		Gives the total number of projects(entries) in the data table. This is done to avoid having a 'magic number'

		PARAMETERS:
		connection - the connection to the database

		RETURNS:
		an int that is the total number of entries in the datatable.
		'''
		try:
			cursor = connection.cursor()
			query = "SELECT COUNT(ID) FROM ksdata"
			cursor.execute(query)
			numberOfProjects = int(cursor.fetchall()[0][0])
			return numberOfProjects

		except Exception as e:
			print ("Something went wrong when executing the query: ", e)
			return connection.cursor()

	def getRandomProject(self, connection):
		'''
        Returns all the information of a random project in list form from the Kickstarter dataset
        PARAMETERS:
            connection - the connection to the database

        RETURNS:
            list of variables for a project, once the data is clean, we will produce the str name of the project
        '''

		try:
			cursor = connection.cursor()
			query = "SELECT * FROM ksdata ORDER BY RANDOM() LIMIT 1"
			cursor.execute(query)
			return cursor.fetchall()

		except Exception as e:
			print ("Something went wrong when executing the query: ", e)
			return connection.cursor()

	#the method implemented via test cases
	def getCountOfVariableSuccess(self, connection, nameOfVariable, variableCondition):
		'''
        Returns the count (an integer) of all projects of one variable that meet a certain condition AND were successful.

        PARAMETERS:
			connection - the connection to the database
            nameOfVariable - the variable of the project we are counting from.
	    	variableCondition - the condition that needs to be met for the project to be counted. For example, if the name of variable is 'country',
			a condition to meet could be 'USA' or 'GB'


        RETURN:
            an integer that is a total of all the projects in the database that fit these two variables AND is successful (the count of successful Film & Video Projects)
		'''
		#work in progress - DO NOT GRADE
		try:
			cursor = connection.cursor()
			query = "SELECT COUNT(state) FROM ksdata WHERE state = 'successful' AND " + str(nameOfVariable) + " = '" + str(variableCondition) + "'"
			cursor.execute(query)
			count = int(cursor.fetchall()[0][0])
			return count

		except Exception as e:
			print ("Something went wrong when executing the query: ", e)
			return None

	def getMinimumValueOfVariable(self, connection, nameOfVariable):
		'''
		Returns the smallest value (a float) in the dataset for a given variable (filter)

		PARAMETERS:
			connection - the connection to the database
			nameOfVariable - the major variable from which the minimum value is being taken

		RETURN:
			a float that is the smallest value in the dataset for the variable provided

		'''

		try:
			cursor = connection.cursor()
			query = "SELECT MIN(" + str(nameOfVariable) + ") FROM ksdata"
			cursor.execute(query)
			smallestValue = float(cursor.fetchall()[0][0])
			return smallestValue

		except Exception as e:
			print ("Something went wrong when executing the query: ", e)
			return None

	def getMaximumValueOfVariable(self, connection, nameOfVariable):
		'''
		Returns the largest value (a float) in the dataset for a given variable (filter)

		PARAMETERS:
			connection - the connection to the database
			nameOfVariable - the major variable from which the maximum value is being taken

		RETURN:
			a float that is the largest value in the dataset for the variable provided

		'''

		try:
			cursor = connection.cursor()
			query = "SELECT MAX(" + str(nameOfVariable) + ") FROM ksdata"
			cursor.execute(query)
			largestValue = float(cursor.fetchall()[0][0])
			return largestValue

		except Exception as e:
			print ("Something went wrong when executing the query: ", e)
			return None

	def getAverageOfVariable(self, connection, nameOfVariable):
		'''
        Returns an average of all the entries for one variable in the data set.

        PARAMETERS:
		connection - the connection to the database
		nameOfVariable - the name of the variable we wish to calculate the average of.


        RETURN:
            an integer that is the average of the provided parameter

		RAISES:
			NeedQuantitaveVariableError - If parameter entered is a categorical variable

		'''
		try:
			cursor = connection.cursor()
			query = "SELECT AVG(" + str(nameOfVariable) + ") FROM ksdata"
			cursor.execute(query)
			averageValue = float(cursor.fetchall()[0][0])
			return averageValue

		except Exception as e:
			print ("Something went wrong when executing the query: ", e)
			return None

		return []

	def getProportionOfSuccess(self, connection, nameOfVariable, variableCondition):
		'''
        Calculates the proportion of successful projects based on the name of
        a column and the filter of that column.

        PARAMETERS:
            connection - the connection to the database
            nameOfVariable - the str variable of the project we are creating a proportion for
            variableCondition - a str attribute of the main variable (i.e category, country, currency)

        RETURNS:
            an int proportion between 0 and 1 inclusive
        '''
		try:
			cursor = connection.cursor()

			query = "SELECT COUNT(" + str(nameOfVariable) + ") FROM ksdata WHERE "  + str(nameOfVariable) + "= '" + str(variableCondition) +"'"
			cursor.execute(query)
			totalCount = float(float(cursor.fetchall()[0][0]))

			query = "SELECT COUNT(state) FROM ksdata WHERE state = 'successful' AND " + str(nameOfVariable) + "= '" + str(variableCondition) +"'"
			cursor.execute(query)
			successCount = float(cursor.fetchall()[0][0])

			proportionOfSuccess = successCount/totalCount
			return proportionOfSuccess


		except Exception as e:
			print ("Something went wrong when executing the query: ", e)
			return connection.cursor()

	def getMedianOfEntireColumn(self, connection, nameOfVariable):
		'''
        Returns the median of a quantitative variable.

        PARAMETERS:
			connection - the connection to the database
            nameOfVariable - the name of the variable we wish to calculate the median of.

        RETURN:
            a integer that is the median of the provided parameter

		RAISES:
			NeedQuantitativeVariableError - If parameter entered is a categorical variable
        '''
		return []

	def getMedianOfFilteredCategory(self, connection, nameOfVariable, variableCondition):
		'''
		Returns the median of a selected 'category' that is grouped by a quantitative variable.

        PARAMETERS
			connection - the connection to the database
			nameOfVariable - a selected category of projects (i.e Design)
			variableCondition - a filter that highlights one specific part of the category. This is typically the name ofa another category (i.e backers or USD goal).



        RETURN:
			an integer that is the median of the provided parameter grouped by the filter (i.e the median USD goal for Design projects)

		RAISES:
			NeedQuantitativeVariableError - If the filter parameter entered is a categorical variable
		'''
		return []

	def mainCategoryCoefficient(self,nameOfVariable):
		if str(nameOfVariable) == 'Arts':
			return 0
		elif str(nameOfVariable) == 'Comics':
			return 0.6494
		elif str(nameOfVariable) == 'Crafts':
			return -0.8739
		elif str(nameOfVariable) == 'Dance':
			return 0.9299
		elif str(nameOfVariable) == 'Design':
			return 0.2445
		elif str(nameOfVariable) == 'Fashion':
			return -0.5401
		elif str(nameOfVariable) == 'Film & Video':
			return 0.1279
		elif str(nameOfVariable) == 'Food':
			return -0.4783
		elif str(nameOfVariable) == 'Games':
			return 0.2531
		elif str(nameOfVariable) == 'Journalism':
			return -0.7870
		elif str(nameOfVariable) == 'Music':
			return 0.4117
		elif str(nameOfVariable) == 'Photography':
			return -0.3656
		elif str(nameOfVariable) == 'Publishing':
			return -0.3063
		elif str(nameOfVariable) == 'Technology':
			return -0.4427
		elif str(nameOfVariable) == 'Theater':
			return 0.8702
		else:
			return -1

	def currencyCoefficient(self, currency):
		if str(currency) == 'AUD':
			return 0
		elif str(currency) == 'CAD':
			return 0.0995
		elif str(currency) == 'CHF':
			return 0.2178
		elif str(currency) == 'DKK':
			return 0.3417
		elif str(currency) == 'EUR':
			return -0.0677
		elif str(currency) == 'GBP':
			return 0.3486
		elif str(currency) == 'HKD':
			return 0.7594
		elif str(currency) == 'JPY':
			return 0.1313
		elif str(currency) == 'MXN':
			return -0.3702
		elif str(currency) == 'NOK':
			return -0.1847
		elif str(currency) == 'NZD':
			return 0.1909
		elif str(currency) == 'SEK':
			return 0.1097
		elif str(currency) == 'SGD':
			return 0.4328
		elif str(currency) == 'USD':
			return 0.4391
		else:
			return -1


	def calculateProbabilityOfSuccess(self, nameOfVariable, currency, usd_goal):
		'''
        Returns the probability of success for a project given input values for the user's
        project idea. R software will be used to generate the formula

        PARAMETERS:
            connection - the connection to the database
            str and int variables that are shown to be statistically significant to determining
            success of a project

        RETURN:
            a probability of success between 0 and 1 inclusive
        '''
		categoryCoefficient = self.mainCategoryCoefficient(nameOfVariable)
		currencyCoefficient = self.currencyCoefficient(currency)
		if categoryCoefficient != -1 and currencyCoefficient != -1:
			probabilityOfSuccess = 1.652 + categoryCoefficient + currencyCoefficient + (-0.2872) * math.log(float(usd_goal))
			if probabilityOfSuccess > 1:
				return '100%'
			elif probabilityOfSuccess < 0.01:
				return 'Less than 1%'
			else:
				return str(round(probabilityOfSuccess*100,2))+'%'
		else:
			return 'Please Enter a Valid Parameters'


	def createRGraph(self, connection, typeOfGraph, tbdFilters):
		'''
        Creates a graph and return the graph onto the website given certain selected
        filters and the type of graph chosen

        PARAMETERS:
            connection - the connection to the database
            typeOfGraph - selected to be either a graph of counts or proportions
            We have yet to determine how varying number of filters can be added

        RETURN:
            a graph
        '''
		return []

	def mostSuccessfulProjects(self, connection, listLength, nameOfVariable, variableCondition):
		'''
        Returns a list of the given length of the most successful projects by success score

        PARAMETERS:
            listLength - int length of list the user wants
			nameOfVariable - the str variable of the project we are creating a proportion for
			variableCondition - a str attribute of the main variable (i.e category, country, currency)

        RETURN:
            A list of the most successful projects with the given length
        '''
		try:
			cursor = connection.cursor()
			query = "SELECT * FROM ksdata WHERE state = 'successful' AND " + str(nameOfVariable) + " = '" + str(variableCondition) + "' ORDER BY success_score DESC LIMIT " + str(listLength)
			cursor.execute(query)
			return cursor.fetchall()

		except Exception as e:
			print ("Something went wrong when executing the query: ", e)
			return connection.cursor()

	def getListOfAllProjectsOfOneCategory(self, connection, nameOfVariable, variableCondition):
		'''
        Returns a list of every project for a given category

        PARAMETERS:
            nameOfVariable - str of the chosen category in the dataset
            variableCondition - a str attribute of the main variable (i.e category, country, currency)

        RETURN:
            A list of each project for the user chosen category
        '''
		try:
			cursor = connection.cursor()
			query = "SELECT * FROM ksdata WHERE " + str(nameOfVariable) + " = '" + str(variableCondition) + "'"
			cursor.execute(query)
			return cursor.fetchall()

		except Exception as e:
			print ("Something went wrong when executing the query: ", e)
			return connection.cursor()

def main():
	ds = DataSource()
	connection = ds.connect()
	print(str(ds.calculateProbabilityOfSuccess('Fashion', 'USD', 10000)))
	#print(str(ds.calculateProbabilityOfSuccess('Music', 'USD', 5)))
	#print(str(ds.calculateProbabilityOfSuccess('Dance', 'US', 500)))
	#print(str(ds.getListOfAllProjectsOfOneCategory(connection,'category','Printing')))
	#print("The total number of projects is:" + str(ds.getNumberOfProjects(connection)))
	#print("A random project is:" + str(ds.getRandomProject(connection)))
	#print("The minimum value of the 'backers' is:" + str(ds.getMinimumValueOfVariable(connection,'backers')))
	#print("The average days for a project is: " + str(ds.getAverageOfVariable(connection, 'total_days')))
	#print("The proportion of Music projects that were successful is: " + str(ds.getProportionOfSuccess(connection, 'main_category', 'Music')))
	#print(ds.mostSuccessfulProjects(connection, 3, 'category', 'Music'))

main()