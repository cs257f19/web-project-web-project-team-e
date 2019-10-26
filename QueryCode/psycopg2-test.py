'''
psycopg2-test.py

Sample code demonstrating how to use the psycopg2 Python library to connect
to a database and execute a query.

author: Amy Csizmar Dalal
date: 22 October 2019
Adapted from code originally written by Jeff Ondich
'''
import getpass
import psycopg2


def connect(user, password):
	'''
	Establishes a connection to the database with the following credentials:
		user - username, which is also the name of the database
		password - the password for this database on perlman

	Returns: a database connection.

	Note: exits if a connection cannot be established.
	'''
	try:
		connection = psycopg2.connect(database=user, user=user, password=password)
	except Exception as e:
		print("Connection error: ", e)
		exit()
	return connection

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
		query = "SELECT COUNT(" + str(nameOfVariable) + ")  FROM ksdata WHERE '" + str(variableCondition) + "' = '" + str(varibaleConditionToMeet) + "';"
		cursor.execute(query)
		return cursor.fetchall()

	except Exception as e:
		print ("Something went wrong when executing the query: ", e)
		return None

def getRandomProject(connection):
	'''
	Gives the name of a random project in the kickstarter dataset

	PARAMETERS:
		connection - the connection to the database

	RETURNS:
		int ID of a random project, once the data is clean, we will produce the str name of the project
	'''

	try:
		cursor = connection.cursor()
		query = "SELECT ID FROM ksdata ORDER BY RAND() LIMIT 1"
		cursor.execute(query)
		return cursor.fetchall()

	except Exception as e:
		print ("Something went wrong when executing the query: ", e)
		return connection.cursor()


def main():

	# Replace these credentials with your own
	user = 'santosb'
	password = 'books347winter'

	# Connect to the database
	connection = connect(user, password)

	# Execute a simple query: how many earthquakes above the specified magnitude are there in the data?
	#results = getCountofFilteredCategory(connection, category, state, successful)
	results = getRandomProject(connection)

	if results is not None:
		print("Query results: ")
		for item in results:
			print(item)

	# Disconnect from database
	connection.close()

main()
