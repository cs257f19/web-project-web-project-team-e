import psycopg2
import getpass

class DataSource:
	'''
	DataSource executes all of the queries on the database.
	It also formats the data to send back to the frontend, typically in a list
	or some other collection or object.
	'''

    def __init__(self):
    	self.numberOfProjects = 378661
        pass

    def connect(user, password):
	'''
	Establishes a connection to the database with the following credentials:
		user - username, which is also the name of the database
		password - the password for this database on perlman

	Returns: a database connection.

	Note: exits if a connection cannot be established.
	Note: Code written by Amy Csizmar Dalal
	'''
	try:
		connection = psycopg2.connect(database=user, user=user, password=password)
	except Exception as e:
		print("Connection error: ", e)
		exit()
	return connection

    def getRandomProject(connection):
        '''
        Gives the name of a random project in the kickstarter dataset 
        
        PARAMETERS:
            connection - the connection to the database
            
        RETURNS:
            the ID of a random project, once the data is clean, we will produce the name of the project
        '''
        
        try:
            cursor = connection.cursor()
            query = "SELECT ID FROM ksdata ORDER BY RAND() LIMIT 1"
            cursor.execute(query)
            return cursor.fetchall()

        except Exception as e:
            print ("Something went wrong when executing the query: ", e)
            return Nonecursor = connection.cursor()

    #ben - how many projects where there in the us
    #IMPLEMENT
    def getCountofFilteredCategory(nameOfVariable, variableCondition, varibaleConditionToMeet):
        '''
        Returns the count (an integer) of all of projects of one variable grouped by another variable (filter)

        PARAMETERS:
            nameOfVariable - the variable of the project we are counting from.
            variableCondition - an attribute of the main variable (i.e category, country, currency)
	    varibaleConditionToMeet - the condition that needs to be met for the project to be counted


        RETURN:
            an integer that is a total of all the projects in the database that fit these two variables (the count of successful Film & Video Projects)

        '''
		try:
			cursor = connection.cursor()
			query = "SELECT COUNT(" + str(nameOfVariable) + ")  FROM ksdata WHERE  " + str(variableCondition) + "=" + str(varibaleConditionToMeet) + ";"
			cursor.execute(query)
			return cursor.fetchall()

		except Exception as e:
			print ("Something went wrong when executing the query: ", e)
			return None

    #Kenyon IMPLEMENT
    def getMinimumValueOfVariable(nameOfVariable):

    #Kenyon IMPLEMENT
    def getMaximumValueOfVariable(nameOfVariable):

    #Ben
    def getAverageOfVariable(nameOfVariable):
        '''
        Returns an average of all the entries for one variable in the data set.

        PARAMETERS:
		nameOfVariable - the name of the variable we wish to calculate the average of.


        RETURN:
            an integer that is the average of the provided parameter

		RAISES:
			NeedQuantitaveVariableError - If parameter entered is a categorical variable

		'''

    #Elisa
    #IMPLEMENT
    def getProportionOfSuccess(nameOfVariable, filter):

    #Ben  - median for a variable
    def getMedianOfEntireColumn(nameOfVariable):
		'''
        Returns the median of a quantitave variable.

        PARAMETERS:
            nameOfVariable - the name of the variable we wish to calculate the median of.

        RETURN:
            a integer that is the median of the provided parameter

		RAISES:
			NeedQuantitaveVariableError - If parameter entered is a categorical variable
        '''

    #Ben - median success rate for poetry projects. Median of one variable grouped by another ie. median of Food Project USD goal
    def getMedianOfFilteredCategory(filter, category):
		'''
		Returns the median of a selected 'category' that is grouped by a quantitave variable.

        PARAMETERS
            category - a selected category of projects (i.e Design)
			filter - a filter that highlights one specific part of the category. This is typically the name ofa another category (i.e backers or USD goal).



        RETURN:
            a integer that is the median of the provided parameter grouped by the filter (i.e the median USD goal for Design projects)

		RAISES:
			NeedQuantitaveVariableError - If the filter parameter entered is a categorical variable

		'''

    #Elisa
    def calculateProbabilityOfSuccess(tbd after analysis):

    #Elisa
    def calculateSuccessScore(tbd):

    #Elisa
    def createRGraph(tbd):

    #Kenyon - Uses calculated success score and give a list based on user input of most successful projects
    def mostSuccessfulProjects(listLength, nameOfVariable, filter):

    #Kenyon - creates a list of all projects of one category
    def getListOfAllProjectsOfOneCatergory(category):





















    def getMagnitudesInRange(self, start, end=10.0):
        '''
        Returns a list of all of the magnitudes from the specified starting magnitude until the specified ending magnitude.

        PARAMETERS:
            start - the low end of the magnitude range
            end - the high end of the magnitude range (default: 10.0)

        RETURN:
            a list of all of the earthquake events with magnitudes in the specified range
        '''
        return []

    def getQuakesOnContinent(self, continent):
        '''
        Returns a list of all of the earthquakes that occurred on the specified continent.

        PARAMETERS:
            continent

        RETURN:
            a list of all of the earthquake events that occurred on this continent
        '''
        return []

    def getQuakesInDateRange(self, start, end):
        '''
        Returns a list of all of the earthquakes that occurred within the range of specified dates.

        PARAMETERS:
            start - the starting date of the range
            end - the ending date of the range

        RETURN:
            a list of all of the earthquake events that occurred within this date range.
        '''
        return []
