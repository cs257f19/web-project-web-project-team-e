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

def getProportionOfSuccess(connection, nameOfVariable, variableCondition):
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
		query = "SELECT COUNT(state) FROM ksdata WHERE state = 'successful' AND" + str(nameOfVariable) + "=" + str(filterName)

		return cursor.execute(query)/self.numberOfProjects

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
	results = getProportionOfSuccess(connection, category, Dance)

	if results is not None:
		print("Query results: ")
		for item in results:
			print(item)

	# Disconnect from database
	connection.close()

main()
