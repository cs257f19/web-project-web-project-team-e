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
        
    #our methods/ideas 
    
    #maybe working implementation - Elisa
    def getRandomProject():
    	cursor = connection.cursor()
    	query = "SELECT ID FROM ksdata ORDER BY RAND() LIMIT 1"
    	cursor.execute(query)
		return cursor.fetchall()
    
    #ben - how many projects where there in the us
    #IMPLEMENT   
    def getCountofVariables(nameOfVariable, filter):
    
    #Kenyon IMPLEMENT
    def getMinimumValueOfVariable(nameOfVariable):
    
    #Kenyon IMPLEMENT
    def getMaximumValueOfVariable(nameOfVariable):
    
    #Ben
    def getAverageOfVariable(nameOfVariable):
    
    #Elisa
    #IMPLEMENT
    def getProportionOfSuccess(nameOfVariable, filter):
    
    #Ben  - median for a variable  
    def getMedianOfEntireColumn(nameOfVariable):
    
    #Ben - median success rate for poetry projects. Median of one variable grouped by another
    def getMedianOfFilteredColumn(nameOfVariable, filter,???):
    
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

